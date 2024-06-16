def read_from_file(file_name):
    try:
        with open(file_name, "r") as file:
            content = file.read()
            print("Content of the file:")
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

# Prompt the user to enter the file name
file_name = input("Enter the name of the file to read: ")

# Read and print the content of the file
read_from_file(file_name)
