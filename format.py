import re
name = input("what's your name? ").strip()

if matches := re.search(r"^(.+), *(.+)?", name):

    last , first = matches.groups()
    name = f"{first} {last}"

print(f"hello, {name}")