def count_substring_occurrences(main_string, substring):
    # Initialize a counter for substring occurrences
    count = 0

    # Iterate through the main string and check for occurrences of the substring
    index = main_string.find(substring)
    while index != -1:
        count += 1
        index = main_string.find(substring, index + 1)

    # Print the result
    print(f"Occurrences of '{substring}' in '{main_string}': {count}")

# Example usage
main_string = input("Enter the Main string :")
substring = input("Enter the substring :")
count_substring_occurrences(main_string, substring)
