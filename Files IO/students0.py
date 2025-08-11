# Reads a CSV file

with open("Harvard/Files IO/students0.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
