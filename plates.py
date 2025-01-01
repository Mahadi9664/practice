def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)

    if length < 2 or length > 6:
        return False

    if not s[0:2].isalpha():
        return False

    if not s.isalnum():
        return False

    found_digit = False
    for char in s:
        if char.isdigit():
            if not found_digit and char == '0':
                return False
            found_digit = True
        elif found_digit:
            return False
        
    return True


if __name__ == "__main__":
    main()
