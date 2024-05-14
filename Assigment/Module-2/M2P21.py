def find_longest_word_length(word_list):
    # Check if the list is not empty
    if not word_list:
        return 0

    # Find the length of the longest word
    longest_word_length = max(len(word) for word in word_list)

    return longest_word_length

# Example usage
words = ["apple", "banana", "kiwi", "strawberry"]
result = find_longest_word_length(words)
print(result)
