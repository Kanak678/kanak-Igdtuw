def find_min_max(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    return minimum, maximum

numbers = input("Enter a list of numbers separated by spaces: ").split()

numbers = [int(num) for num in numbers]
minimum, maximum = find_min_max(numbers)
print("Minimum value:", minimum)
print("Maximum value:", maximum)  
