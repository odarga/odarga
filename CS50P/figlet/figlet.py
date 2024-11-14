import sys
from random import randint
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    font = fonts[randint(0, 549)]
elif len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in fonts:
       sys.exit("Invalid Usage")
    else:
        font = sys.argv[2]
else:
    sys.exit("Invalid Usage")

s = input("Input: ")
figlet.setFont(font = font)
print(figlet.renderText(s))


