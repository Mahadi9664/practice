import re


def main():
    print(count(input("Text: ").strip()))


def count(s):
    x = re.findall(r"\bum\b", s, re.IGNORECASE)

    num = 0
    for i in x:
        num += 1
    return num


if __name__ == "__main__":
    main()