import argparse
from datetime import datetime

def parse_adi_file(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def filter_adi_data(data, start_datetime):
    filtered_data = []
    for line in data:
        if '<CALL:' in line:
            qso_date = line.split('<QSO_DATE:')[1].split('>')[1].strip()
            time_on = line.split('<TIME_ON:')[1].split('>')[1].strip()
            try:
                qso_datetime = datetime.strptime(qso_date + time_on, '%Y%m%d%H%M%S')
            except ValueError:
                continue
            if qso_datetime >= start_datetime:
                filtered_data.append(line)
        else:
            filtered_data.append(line)
    return filtered_data

def write_cleaned_adi_file(data, original_file_path):
    cleaned_file_path = original_file_path + '.clean'
    with open(cleaned_file_path, 'w') as file:
        file.writelines(data)

def main():
    parser = argparse.ArgumentParser(description='ADIF Cleaner Tool')
    parser.add_argument('-st', '--start-time', required=True, help='UTC date in the format: YYYY-MM-DDTHH:MMZ')
    parser.add_argument('-f', '--file', required=True, help='Path to the file to be parsed')
    args = parser.parse_args()

    start_datetime = datetime.strptime(args.start_time, '%Y-%m-%dT%H:%MZ')
    data = parse_adi_file(args.file)
    filtered_data = filter_adi_data(data, start_datetime)
    write_cleaned_adi_file(filtered_data, args.file)

if __name__ == '__main__':
    main()
