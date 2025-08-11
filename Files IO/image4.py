from PIL import Image
from PIL import ImageFilter


def main():
    with Image.open("Harvard/Files IO/in.jpeg") as img:
        img = img.rotate(180)
        img = img.filter(ImageFilter.BLUR)
        img.save("Harvard/Files IO/out.jpeg")


main()
