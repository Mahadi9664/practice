import emoji

x = input("Input: ")

# Ensure `use_aliases` is specified if needed
print(emoji.emojize(f'Output: {x}', language="alias"))
