import string

def is_pangram(text):
    return set(string.ascii_lowercase).issubset(set(text.lower()))

print("7. is_pangram (The quick brown fox jumps over the lazy dog):", is_pangram("The quick brown fox jumps over the lazy dog"))  # → True
print("7. is_pangram (Hello World):", is_pangram("Hello World"))  # → False
