# Reads from a file

with open("Harvard/Files IO/names.txt") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())
