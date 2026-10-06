with open("sample.txt", "w") as file:
    file.write("Python Day 2 Internship Training\n")
    file.write("File handling practice")

with open("sample.txt", "r") as file:
    content = file.read()

print(content)