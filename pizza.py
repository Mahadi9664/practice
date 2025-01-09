import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    

    try:
        reader = {}
        with open(sys.argv[1]) as csvfile:
            reader = csv.DictReader(csvfile)
            table = list(reader)

            if not table:
                sys.exit("CSV file empty")
            
            print(tabulate(table))

        

    except FileNotFoundError:
        sys.exit("File does not exist")
    

if __name__ == "__main__":
    main()
