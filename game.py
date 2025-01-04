import random

def positive_integer():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl > 0:
                return lvl
            else:
                pass
        except ValueError:
            pass

def guess_integer():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                return guess
            else:
                pass
        except ValueError:
            pass



def main():
    n = positive_integer()
    r = random.randint(0,n)
    
    while True:
        guess = guess_integer()

        if(guess < r):
            print("Too small!")

        elif(guess > r):
            print("Too large!")

        else:
            print("Just right!")
            break


        



if __name__ == "__main__":
    main()