# Appends to a file

name = input("What's your name? ")

file = open("Harvard/Files IO/names.txt", "a")
file.write(f"{name}\n")
file.close()
