# Adds context manager

name = input("What's your name? ")

with open("Harvard/Files IO/names.txt", "a") as file:
    file.write(f"{name}\n")
