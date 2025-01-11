import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    line_count = 0

    output = []
    try:
        with open(sys.argv[1], 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:

                if "name" not in row or "house" not in row:
                    sys.exit("Missing columns in input CSV")

                split_name = row["name"].split(",")

                if len(split_name) != 2:
                    sys.exit("Invalid name format in input CSV")

                output.append({'first': split_name[1].strip(), 
                               'last': split_name[0].strip(), 
                               'house': row ["house"]})
            

    except FileNotFoundError:
        sys.exit("File does not exist")

    try:
        with open(sys.argv[2], "w", newline="") as file:  # Include 'newline=""'
            writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            writer.writerows(output)  # Write all rows at once

    except Exception as e:
        sys.exit(f"Error writing to file: {e}")
    
    

if __name__ == "__main__":
    main()
