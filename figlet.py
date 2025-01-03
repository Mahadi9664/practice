import sys
import random
from pyfiglet import Figlet

figlet = Figlet()

fonts = figlet.getFonts()


text = input("Input: ")

if(len(sys.argv)) == 1:
    random_font = random.choice(fonts)
    figlet.setFont(font=random_font)
    print(figlet.renderText(text))
elif(len(sys.argv)) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    s_font = sys.argv[2]
    if s_font in fonts:
        figlet.setFont(font = s_font)
        print(figlet.renderText(text))
    else:
        sys.exit("Invalid usage")
    
else:
    sys.exit("Invalid usage")