import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    line_count = 0

    try:
        with open(sys.argv[1]) as file:
            lines = file.readlines()

        for line in lines:
            if line.isspace():
                continue
            elif line.lstrip().startswith('#'):
                continue
            else:
                line_count += 1

    except FileNotFoundError:
        sys.exit("File does not exist")
    
    print(line_count)

if __name__ == "__main__":
    main()
