# writing to a file
with open("sample.txt", "w") as file:
    file.write("Hello, Python!\n")
    file.write("File handling is easy")

# Reading from a file
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# Appending to a File
with open("sample.txt", "a") as file:
    file.write("\nAppending a new line.")
