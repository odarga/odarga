import sys
from PIL import Image, ImageOps

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
else:
    try:
        input_extension = sys.argv[1].split(".")[1]
        output_extension = sys.argv[2].split(".")[1]
    except IndexError:
        sys.exit("Invalid input")
    else:
        if input_extension.lower() not in ("jpg", "jpeg", "png") or output_extension.lower() not in ("jpg", "jpeg", "png"):
            sys.exit("Invalid input")
        elif input_extension != output_extension:
            sys.exit("Input and output have different extensions")
        else:
            try:
                muppet = Image.open(sys.argv[1])
            except FileNotFoundError:
                sys.exit("Input does not exist")
            else:
                shirt = Image.open("shirt.png")
                size = shirt.size
                muppet = ImageOps.fit(muppet, size)
                muppet.paste(shirt, shirt)
                muppet.save(sys.argv[2])

