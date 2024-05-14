def count_characters(input_string):
    # Create an empty dictionary to store character frequencies
    char_frequency = {}

    # Iterate through each character in the input string
    for char in input_string:
        # Increment the count for each character in the dictionary
        char_frequency[char] = char_frequency.get(char, 0) + 1

    # Print the character frequencies
    for char, count in char_frequency.items():
        print(f"{char}: {count}")

# Example usage
input_string = input("Enter the siring :")
count_characters(input_string)
