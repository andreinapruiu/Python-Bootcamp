def all_even_digits(n):
    return all(int(d) % 2 == 0 for d in str(n))

even_digit_numbers = [str(n) for n in range(100, 501) if all_even_digits(n)]

print("Even-digit numbers:", ", ".join(even_digit_numbers))
