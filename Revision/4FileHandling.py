# Chapter 5: File Handling

# Reading and Writing Files

# Writing to a text file
with open("example.txt", "w") as file:
    file.write("Hello, this is a sample file.\n")
    file.write("Python is a powerful language!\n")

# Reading from a text file
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:\n", content)

# Appending to a text file
with open("example.txt", "a") as file:
    file.write("Appending more content to the file.\n")

# Reading the updated file
with open("example.txt", "r") as file:
    updated_content = file.read()
    print("\nUpdated File Content:\n", updated_content)

# Exception Handling in File Operations

try:
    # Trying to open a non-existent file for reading
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found!")

# Using the 'with' statement for file handling

try:
    # Using 'with' statement to open a file
    with open("example.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            print("Line:", line.strip())
except FileNotFoundError:
    print("File not found!")

# Writing and reading binary files

# Writing binary data to a file
with open("binary_data.bin", "wb") as file:
    file.write(b'\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64')

# Reading binary data from a file
with open("binary_data.bin", "rb") as file:
    binary_content = file.read()
    print("\nBinary Content:", binary_content)
