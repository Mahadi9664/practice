due = 50

while due>0:
    print("Amount Due: ", due)
    x = int(input("Insert coin: "))
    if x in [25, 10, 5]:
        due -= x

change = abs(due)
print("Change Owed: ", change)

    