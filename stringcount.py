from collections import Counter
import string as str_lib

# Given string
string = "To change the overall look of your document. To change the look"

# Normalize the string by converting it to lowercase and removing punctuation
normalized_string = string.translate(str_lib.str.maketrans('', '', str_lib.punctuation)).lower()

# Split the string into words
words = normalized_string.split()

# Use Counter to count occurrences of each word
word_count = Counter(words)

# Print the word count
for word, count in word_count.items():
    print(f"'{word}': {count}")