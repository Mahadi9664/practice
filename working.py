import re


def main():
    try:
        print(convert(input("Hours: ").lower().strip()))
    except ValueError:
        print("Format incorrect")


def convert(s):
    if  x := re.search(r"^([0-9]+):?([0-9]+)? (am|pm) to ([0-9]+):?([0-9]+)? (am|pm)$", s):
        hour1 = int(x.group(1))
        minute1 = int(x.group(2) or 0)
        period1 = x.group(3)

        hour2 = int(x.group(4))
        minute2 = int(x.group(5) or 0)
        period2 = x.group(6)


        if hour1 > 12:
            raise ValueError
        if period1 == 'pm' and hour1 != 12:
            hour1 += 12
        if period1 == 'am' and hour1 == 12:
            hour1 == 0
        left = f"{hour1:02}:{minute1:02}"


        if hour2 > 12:
            raise ValueError
        if period2 == 'pm' and hour2 != 12:
            hour2 += 12
        if period2 == 'am' and hour2 == 12:
            hour2 == 0
        right = f"{hour2:02}:{minute2:02}"

        return(f"{left} to {right}")
    
    else:
        raise ValueError


if __name__ == "__main__":
    main()