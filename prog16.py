def count_character_frequency(input_string):
    char_frequency = {}
    for char in input_string:
        if char in char_frequency:
            char_frequency[char] += 1
        else:
            char_frequency[char] = 1

    return char_frequency
input_string = input("Enter a string: ")
character_frequency = count_character_frequency(input_string)
print("Frequency of each character in the string:")
for char, frequency in character_frequency.items():
    print(f"{char}: {frequency}")
