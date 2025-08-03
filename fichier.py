
with open("test.txt", "w") as f:
    f.write("Hello\n")
    f.write("C'est Assane\n")


with open("test.txt", "r") as f:
    print(f.read())


with open("test.txt", "a") as f:
    f.write("Ligne ajoutée\n")
