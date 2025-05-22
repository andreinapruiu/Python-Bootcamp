def get_even_numbers_up_to(n):
    return [i for i in range(n + 1) if i % 2 == 0]

num = int(input("Enter an integer: "))
print("Even numbers:", get_even_numbers_up_to(num))
