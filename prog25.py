def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as f_source:
            contents = f_source.read()

        with open(destination_file, 'w') as f_dest:
            f_dest.write(contents)

        print(f"Successfully copied from '{source_file}' to '{destination_file}'.")

    except FileNotFoundError:
        print("Error: One or both files not found.")
    except IOError:
        print("Error: An error occurred while copying the file.")
    except Exception as e:
        print(f"Error: {str(e)}")

def main():
    source_file = input("Enter the source file name: ")
    destination_file = input("Enter the destination file name: ")

    copy_file(source_file, destination_file)

if __name__ == "__main__":
    main()
