import argparse
from datetime import datetime
import re

def parse_adi_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def filter_adi_data(data, start_datetime, end_datetime=None, dedup=False):
    filtered_data = []
    seen_callsigns = set()
    for line in data:
        if '<CALL:' in line:
            try:
                qso_date = re.search(r'<QSO_DATE:\d+>(\d+)', line).group(1)
                time_on = re.search(r'<TIME_ON:\d+>(\d+)', line).group(1)
                qso_datetime = datetime.strptime(qso_date + time_on, '%Y%m%d%H%M%S')
                callsign = re.search(r'<CALL:\d+>(\w+)', line).group(1)
                if qso_datetime >= start_datetime and (end_datetime is None or qso_datetime <= end_datetime):
                    if dedup:
                        if callsign not in seen_callsigns:
                            filtered_data.append(line)
                            seen_callsigns.add(callsign)
                    else:
                        filtered_data.append(line)
            except (IndexError, ValueError, AttributeError) as e:
                print(f"Error parsing line: {line}\nError: {e}")
    return filtered_data

def write_cleaned_adi_file(data, original_file_path):
    cleaned_file_path = original_file_path + '.clean'
    with open(cleaned_file_path, 'w') as file:
        file.writelines(data)

def main():
    parser = argparse.ArgumentParser(description='ADIF Cleaner Tool')
    parser.add_argument('-st', '--start-time', required=True, help='UTC date in the format: YYYY-MM-DDTHH:MMZ')
    parser.add_argument('-et', '--end-time', required=False, help='UTC date in the format: YYYY-MM-DDTHH:MMZ')
    parser.add_argument('-f', '--file', required=True, help='Path to the file to be parsed')
    parser.add_argument('-d', '--dedup', action='store_true', help='Remove duplicate entries')
    args = parser.parse_args()

    start_datetime = datetime.strptime(args.start_time, '%Y-%m-%dT%H:%MZ')
    end_datetime = datetime.strptime(args.end_time, '%Y-%m-%dT%H:%MZ') if args.end_time else None

    data = parse_adi_file(args.file)
    filtered_data = filter_adi_data(data, start_datetime, end_datetime, args.dedup)
    write_cleaned_adi_file(filtered_data, args.file)

if __name__ == '__main__':
    main()
