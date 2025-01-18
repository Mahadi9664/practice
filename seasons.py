from datetime import datetime, date
import re
import sys
import inflect

def main():
    today = date.today()
    birth_date = input("Date of Birth: ")
    year, month, day = check_birthday(birth_date)

    date_of_birth = date(int(year), int(month), int(day))

    days_lived = (today - date_of_birth).days
    p = inflect.engine()
    
    days_in_words = p.number_to_words(days_lived, andword='')
    print(days_in_words)


    

def check_birthday(birth_date):
    if re.search(r"^[0-9]{4}-(0[1-9]|1[0-2])-[0-9]{2}$", birth_date):
        year,month,day = birth_date.split("-")
        return year,month,day
    else:
        sys.exit("Invalid date")



if __name__ == "__main__":
    main()