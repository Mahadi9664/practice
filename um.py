import re


def main():
    print(count(input("Text: ")))


def count(s):
    x = re.findall(r"\bum\b", s)

    num = 0
    for i in x:
        num += 1
    return num


if __name__ == "__main__":
    main()