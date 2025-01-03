import inflect


def main():
    p = inflect.engine()

    names = []
    try:
        while True:
            name = input("Name: ")
            names.append(name)

            if(name==""):
                names.remove(name)
                break
                


    except EOFError:
        pass

    print("Adiue,adieu, to " + p.join(names))

if __name__ == "__main__":
    main()