import csv

def read_csv_file(file_name):
    try:
        with open(file_name, 'r') as file:
            csv_reader = csv.reader(file)
            print("Data from CSV file:")
            for row in csv_reader:
                print(', '.join(row))
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")

file_name = input("Enter the name of the CSV file to read: ")

read_csv_file(file_name)
