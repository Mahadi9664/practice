grocery = {}

while True:
    try:
        item = input().upper()
        if item in grocery:
            grocery[item] += 1
        elif item == "":
            for item in grocery:
                print(f"{grocery[item]} {item}")
            break
        else:
            grocery[item] = 1
    except KeyError:
        break
