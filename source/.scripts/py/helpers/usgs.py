import csv
import argparse
import sys
from pathlib import Path
from datetime import datetime

def parse_usgs_data(input_file_path: Path):
    """
    Reads a USGS water flow CSV, extracts 'time' and 'value' columns,
    and writes them to a new CSV in the same directory.
    """
    
    if not input_file_path.exists():
        print(f"Error: The input file '{input_file_path}' does not exist.")
        sys.exit(1)

    if not input_file_path.is_file():
        print(f"Error: The path '{input_file_path}' is not a file.")
        sys.exit(1)

    output_file_path = input_file_path.parent / f"{input_file_path.stem}_parsed.csv"

    try:
        with open(input_file_path, mode='r', encoding='utf-8') as infile, \
             open(output_file_path, mode='w', encoding='utf-8', newline='') as outfile:
            
            reader = csv.DictReader(infile)
            writer = csv.writer(outfile)
            
            writer.writerow(['Timestamp', 'CFS'])
            
            for row in reader:
                raw_timestamp = row.get('time')
                cfs = row.get('value')
                
                if raw_timestamp is not None and cfs is not None:
                    try:
                        # Parse the ISO timestamp and format to strip the timezone offset
                        dt = datetime.fromisoformat(raw_timestamp)
                        formatted_timestamp = dt.strftime('%Y-%m-%d %H:%M:%S')
                    except ValueError:
                        # Fallback to simple string slicing if it fails to parse
                        formatted_timestamp = raw_timestamp.split('+')[0]

                    writer.writerow([formatted_timestamp, cfs])

        print(f"Successfully processed. Output written to:\n{output_file_path}")

    except Exception as e:
        print(f"An error occurred during processing: {e}")
        sys.exit(1)

if __name__ == "__main__":
    script_dir = Path(__file__).resolve().parent
    default_input_path = script_dir / "usgs_data.csv"

    parser = argparse.ArgumentParser(
        description="Parse a USGS CSV file to extract Timestamp and CFS columns."
    )
    
    parser.add_argument(
        "file",
        type=Path,
        nargs="?",
        default=default_input_path,
        help=f"Absolute path to the input CSV file. Defaults to: {default_input_path}"
    )

    args = parser.parse_args()
    absolute_input_path = args.file.resolve()

    parse_usgs_data(absolute_input_path)