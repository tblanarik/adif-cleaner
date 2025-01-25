# adif-cleaner

`adif-cleaner` is a tool for cleaning ADIF (Amateur Data Interchange Format) files by filtering QSOs (contacts) based on date and time, and optionally removing duplicate entries.

## Features

- Filter QSOs by start and end date/time.
- Optionally remove duplicate QSOs based on callsign.
- Output cleaned ADIF files with a `.clean` extension.

## Requirements

- Python 3.6 or higher

## Usage

Run the script with the required arguments:

    python src/adifcleaner.py -st <start-time> -f <file> [-et <end-time>] [-d]

### Arguments

- `-st`, `--start-time`: Required. UTC date in the format `YYYY-MM-DDTHH:MMZ`.
- `-et`, `--end-time`: Optional. UTC date in the format `YYYY-MM-DDTHH:MMZ`.
- `-f`, `--file`: Required. Path to the ADIF file to be parsed.
- `-d`, `--dedup`: Optional. Remove duplicate entries based on callsign.

### Example

Filter QSOs from `2025-01-12T00:00Z` to `2025-01-12T23:59Z` and remove duplicates:

    python src/adifcleaner.py -st 2025-01-12T00:00Z -et 2025-01-12T23:59Z -f data/test1.adi -d

## Sample Run

Here is a sample run of the script:

    $ python src/adifcleaner.py -st 2025-01-12T00:00Z -et 2025-01-12T23:59Z -f data/test1.adi -d

This will filter the QSOs in `data/test1.adi` from `2025-01-12T00:00Z` to `2025-01-12T23:59Z` and remove duplicate entries based on callsign. The cleaned data will be saved to `data/test1.adi.clean`.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.