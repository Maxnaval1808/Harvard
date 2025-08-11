from PIL import Image


def main():
    with Image.open("Harvard/Files IO/in.jpeg") as img:
        print(img.size)
        print(img.format)


main()
