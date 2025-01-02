month = {

    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12

}

while True:
    try:
        x = input("Date: ").title().strip()
        if x[0].isalpha():
            x = x.replace(",","")
            w,y,z = x.split()

            if w in month: 
                w = month[w]

            print(f"{int(z):04}-{w:02}-{int(y):02}")
            break
        else:
            m,n,o = map(int,x.split(sep="/"))

            print(f"{o:04}-{m:02}-{n:02}")
            break
    except (ValueError, EOFError):
        pass

