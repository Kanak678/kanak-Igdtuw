def read_multiple_lines():
    lines = []
    while True:
        line = input("Enter a line (or press Enter to finish): ")
        if line == "":
            break
        lines.append(line)
    return lines

input_lines = read_multiple_lines()
print("You entered the following lines:")
for line in input_lines:
    print(line)
