# Ask for a word
word = input("Enter a word: ")

# Print True if it is a plaindrome
is_palindrome = word == word[::-1]
print(f"The word '{word}' is a palindrome: {is_palindrome}")