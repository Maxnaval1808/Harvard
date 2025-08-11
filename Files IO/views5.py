import csv
import numpy as np
from PIL import Image


def main():
    with open("Harvard/Files IO/views.csv", "r", encoding="utf-8") as views, open("Harvard/Files IO/analysis.csv", "w", encoding="utf-8") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()

        for row in reader:
            row["brightness"] = round(calculate_brightness(f"Harvard/Files IO/{row['id']}.jpeg"), 2)
            writer.writerow(row)


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()
