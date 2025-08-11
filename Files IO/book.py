def main():
    with open("Harvard/Files IO/alice.txt", "r") as f:
      contents = f.readlines()
      chapter1 = contents[52:272]
     
    with open("Harvard/Files IO/chapter1.txt", "w") as f:
      f.writelines(chapter1)

main()
