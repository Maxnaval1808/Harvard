# Reads from a file, one line at a time

with open("Harvard/Files IO/names.txt") as file:
    for line in file:
        print("hello,", line.rstrip())
