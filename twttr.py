x = input("type something: ")

print("Output: ", end= "")

vowels = {'a','e','i','o','u','A','E','I','O','U'}
for char in x:
    if char not in vowels:
        print(char,end= "")

print()

