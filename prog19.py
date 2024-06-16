import string

def remove_punctuation(input_string):
   
    translator = str.maketrans('', '', string.punctuation)
    return input_string.translate(translator)

input_string = input("Enter a string: ")
string_without_punctuation = remove_punctuation(input_string)
print("String without punctuation:", string_without_punctuation)
