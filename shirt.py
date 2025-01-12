import sys
from os.path import splitext
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    file1 = splitext(sys.argv[1])
    file2 = splitext(sys.argv[2])

    if not check_extension(file1[1]):  
        sys.exit("Invalid input")
    if not check_extension(file2[1]):  
        sys.exit("Invalid input")
    if file1[1].lower() != file2[1].lower():  
        sys.exit("Input and output have different extensions")

    try:
        imagefile = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")  

    try:
        shirtFile = Image.open("shirt.png")
    except FileNotFoundError:
        sys.exit("Shirt file (shirt.png) not found")  

    size = shirtFile.size
    muppet = ImageOps.fit(imagefile, size)  
    muppet.paste(shirtFile, shirtFile)  
    muppet.save(sys.argv[2])

def check_extension(file):
    if file.lower() in [".jpg", ".jpeg", ".png"]:  
        return True
    return False

if __name__ == "__main__":
    main()
