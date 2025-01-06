def main():
    greeting = input("Greeting: ")
    print(value(greeting))


def value(greeting):
    greeting = greeting.lower().strip()
    if "hello" in greeting:
        return (f"$0")
    elif "h" == greeting[0]:
        return (f"$20")
    else:
        return (f"$100")

if __name__ == "__main__":
    main()