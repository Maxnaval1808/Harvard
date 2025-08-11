# Unpacks a list

with open("Harvard/Files IO/students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
