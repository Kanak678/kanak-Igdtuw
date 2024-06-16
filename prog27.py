def string_to_list(s):
    return list(s)

def main():
    input_string = input("Enter a string: ")
    characters_list = string_to_list(input_string)
    
    print(f"The string '{input_string}' converted into a list of characters is:")
    print(characters_list)

if __name__ == "__main__":
    main()
