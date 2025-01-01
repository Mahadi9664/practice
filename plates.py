def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)

    # Check length
    if length < 2 or length > 6:
        return False

    # Check first two characters are letters
    if not s[:2].isalpha():
        return False

    # Check for only alphanumeric characters
    if not s.isalnum():
        return False

    found_digit = False
    for char in s:
        if char.isdigit():
            # Check for leading '0' in numbers
            if not found_digit and char == '0':
                return False
            found_digit = True
        elif found_digit:
            # Return False if letter appears after number
            return False
        
    return True


if __name__ == "__main__":
    main()
