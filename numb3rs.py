import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if not re.match(r"^(\d+\.\d+\.\d+\.\d+)$",ip):
        return False
    

    numbers = ip.split(".")

    for num in numbers:
        if not num.isdigit() or not 0 <= int(num) <=255:
            return False
        
    return True
       
   




if __name__ == "__main__":
    main()