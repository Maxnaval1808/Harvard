from PIL import Image


def main():
    with Image.open("Harvard/Files IO/in.jpeg") as img:
        img = img.rotate(180)
        img.save("Harvard/Files IO/out.jpeg")


main()
