def count_occurrences(lst, element):
    return lst.count(element)

numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
element_to_count = int(input("Enter the element to count: "))
occurrences = count_occurrences(numbers, element_to_count)
print(f"The element {element_to_count} occurs {occurrences} time(s) in the list.")
