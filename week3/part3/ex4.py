import string

def is_valid_password(password):
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    return 6 <= len(password) <= 16 and has_lower and has_upper and has_digit and has_special

pwd = input("Enter a password: ")
print("Password is valid." if is_valid_password(pwd) else "Password is invalid.")
