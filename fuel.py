while True:
    try:
        x, y = map(int,input("Fraction (X/Y): ").split('/'))
        if y == 0:
            raise ZeroDivisionError
        if x>y:
            raise ValueError
        
        percentage = round((x/y)*100)

        if percentage <= 1:
            print("E")
        elif percentage >=99:
            print("F")
        else:
            print(f"Fraction: {percentage}%")
        break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass


        
    