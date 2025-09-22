import sys
import csv
import os
import re


def parse_log_line(line):
    """
    Parse a doxygen log line and extract file name, line number, and message.
    Expected format: <file_path>:<line_number>: <message_type>: <message>
    """
    line = line.strip()
    if not line:
        return None
    
    # Use regex to match the pattern: file_path:line_number: rest_of_message
    match = re.match(r'^(.+):(\d+):\s*(.+)$', line)
    if match:
        file_path = match.group(1)
        line_number = match.group(2)
        message = match.group(3)
        
        # Extract just the filename from the full path
        file_name = os.path.basename(file_path)
        
        return {
            'line_number': line_number,
            'file_name': file_name,
            'message': message
        }
    return None


def is_standard_line(line):
    """Check if the line follows the expected doxygen log format."""
    return parse_log_line(line) is not None


def main():
    if len(sys.argv) < 2:
        print("Usage: python parse_log_to_csv.py <log_file_path>")
        sys.exit(1)
    
    log_path = sys.argv[1]
    if not os.path.isfile(log_path):
        print(f"File not found: {log_path}")
        sys.exit(1)

    # Parse the log file and extract standard lines
    parsed_lines = []
    ignored_lines = 0
    
    with open(log_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            parsed = parse_log_line(line)
            if parsed:
                parsed_lines.append(parsed)
            else:
                ignored_lines += 1

    if not parsed_lines:
        print("No standard lines found in the log file.")
        sys.exit(1)

    # Write to CSV with the specified columns
    with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['line_number', 'file_name', 'message']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        # Write header
        writer.writeheader()
        
        # Write data rows
        for parsed_line in parsed_lines:
            writer.writerow(parsed_line)

    print(f"Successfully parsed {len(parsed_lines)} lines to output.csv")
    print(f"Ignored {ignored_lines} non-standard lines")

if __name__ == "__main__":
    main()