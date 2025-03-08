text = input("Enter a text:")

with open("textFile.txt", "w") as file:
    file.write(text)

with open("textFile.txt", "r") as file:
    print("Content:")
    print(file.read())

lines = []
for i in range(5):
    line = input(f"Enter a {i+1}. line:")
    lines.append(line)

with open("textFile.txt","w") as file:
    for line in lines:
        file.write(line + "\n")

with open("textFile.txt", "r") as file:
    print("Contents of the file:")
    for line in file:
        print(line)