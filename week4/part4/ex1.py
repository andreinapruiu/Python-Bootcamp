import re

print("1. Match strings with 'a' followed by zero or more 'b's")
pattern1 = r"ab*"
print(re.findall(pattern1, "ab abb abbb a b aaabbb"))

print("\n2. Match strings with 'a' followed by one or more 'b's")
pattern2 = r"ab+"
print(re.findall(pattern2, "ab abb abbb a b aaabbb"))

print("\n3. Match any word containing 'z'")
pattern3 = r"\b\w*z\w*\b"
print(re.findall(pattern3, "zebra buzz puzzle crazy lazy amazing apple"))

print("\n4. Match strings containing only letters, numbers, underscores")
pattern4 = r"^\w+$"
print("Valid_123:", bool(re.match(pattern4, "Valid_123")))
print("Invalid-123:", bool(re.match(pattern4, "Invalid-123")))

print("\n5. Match numbers of length between 1 and 3 digits")
pattern5 = r"\b\d{1,3}\b"
print(re.findall(pattern5, "3 25 456 7890 12345 7"))

print("\n6. Match all 3, 4, and 5 letter words")
pattern6 = r"\b\w{3,5}\b"
print(re.findall(pattern6, "this list has both big small and mid words"))

print("\n7. Match any URL")
pattern7 = r"https?://[^\s]+"
text7 = "Visit https://openai.com or http://example.org for info"
print(re.findall(pattern7, text7))

print("\n8. Match any email address")
pattern8 = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
text8 = "Contact: hello@example.com, admin@test.org"
print(re.findall(pattern8, text8))

print("\n9. Match a Romanian phone number (starting with 07 and 10 digits)")
pattern9 = r"\b07\d{8}\b"
text9 = "Call me at 0712345678 or 0734567890, not 0612345678"
print(re.findall(pattern9, text9))

print("\n10. Match all floating point numbers")
text10 = (
    "Speed of light in vacuum 299792458 m/s Standard atmosphere 101325 Pa "
    "Earth to sun distance 149600000 km Acceleration of gravity 9.80665 m/s^2 "
    "Circumference to diameter ratio 3.141592 Gas constant 8.3144621 J/mol*K"
)
pattern10 = r"\d+\.\d+"
print(re.findall(pattern10, text10))

print("\n11. Match movies released before 1990")
text11 = (
    "1 The Shawshank Redemption (1994) 2 The Godfather (1972) "
    "3 The Godfather: Part II (1974) 4 Pulp Fiction (1994) "
    "5 The Good, the Bad and the Ugly (1966) 6 The Dark Knight (2008) "
    "7 12 Angry Men (1957) 8 Schindler's List (1993) "
    "9 The Lord of the Rings: The Return of the King (2003) "
    "10 Fight Club (1999)"
)
pattern11 = r"\b\d+\s(.+?)\((19[0-8]\d)\)"
old_movies = re.findall(pattern11, text11)
print(["{} ({})".format(title.strip(), year) for title, year in old_movies])
