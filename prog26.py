def check_prefix_suffix(text, prefix, suffix):
    starts_with_prefix = text.startswith(prefix)
    ends_with_suffix = text.endswith(suffix)

    return starts_with_prefix, ends_with_suffix

def main():
    text = input("Enter a string: ")
    prefix = input("Enter the prefix to check: ")
    suffix = input("Enter the suffix to check: ")

    starts_with_prefix, ends_with_suffix = check_prefix_suffix(text, prefix, suffix)

    if starts_with_prefix:
        print(f"The string '{text}' starts with the prefix '{prefix}'.")
    else:
        print(f"The string '{text}' does not start with the prefix '{prefix}'.")

    if ends_with_suffix:
        print(f"The string '{text}' ends with the suffix '{suffix}'.")
    else:
        print(f"The string '{text}' does not end with the suffix '{suffix}'.")

if __name__ == "__main__":
    main()
