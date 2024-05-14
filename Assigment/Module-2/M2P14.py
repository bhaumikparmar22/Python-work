def count_word_occurrences(sentence):
    # Split the sentence into words
    words = sentence.split()

    # Initialize a dictionary to store word frequencies
    word_frequency = {}

    # Iterate through each word in the list and update the dictionary
    for word in words:
        # Remove punctuation and convert to lowercase for better matching
        cleaned_word = word.strip(".,?!").lower()
        # Increment the count for each word in the dictionary
        word_frequency[cleaned_word] = word_frequency.get(cleaned_word, 0) + 1

    # Print the word frequencies
    for word, count in word_frequency.items():
        print(f"{word}: {count}")

# Example usage
input_sentence = "This is a simple example sentence. This sentence is for counting word occurrences."
count_word_occurrences(input_sentence)
