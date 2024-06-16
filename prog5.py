def write_to_file(text):
    with open("output.txt", "w") as file:
        file.write(text)
    print("String has been written to output.txt successfully.")

# Take string input from the user
input_string = input("Enter a string: ")

# Write the input string to a text file
write_to_file(input_string)
