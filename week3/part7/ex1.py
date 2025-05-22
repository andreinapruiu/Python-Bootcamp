my_string = "Practice Problems to Drill List Comprehension in Your Head."

div_by_8 = [n for n in range(1, 1001) if n % 8 == 0]

contains_6 = [n for n in range(1, 1001) if '6' in str(n)]

space_count = sum(1 for char in my_string if char == ' ')

no_vowels = ''.join([c for c in my_string if c.lower() not in 'aeiou'])

short_words = [word for word in my_string.split() if len(word) < 5]

word_lengths = {word: len(word) for word in my_string.split()}

print("1. Numbers divisible by 8 (1–1000):")
print(div_by_8, end="\n\n")

print("2. Numbers that contain the digit '6':")
print(contains_6, end="\n\n")

print("3. Number of spaces in the string:")
print(space_count, end="\n\n")

print("4. String with all vowels removed:")
print(no_vowels, end="\n\n")

print("5. Words with fewer than 5 letters:")
print(short_words, end="\n\n")

print("6. Word lengths dictionary:")
print(word_lengths)
