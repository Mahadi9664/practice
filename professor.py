import random


def main():
    level = get_level()

    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        
        attempts = 0
        while attempts <3:
            try:
                ans = int(input(f"{x} + {y} = "))
                if(ans == x + y):
                    score += 1
                    break
                else:
                    print("EEE")
                    attempts += 1
            except ValueError:
                print("EEE")
                attempts += 1
        
        if attempts == 3:
            print(f"{x} + {y} = {x+y}")

    print(f"Score: {score}")



def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if (1>level>3 ):
                raise ValueError
            else:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()