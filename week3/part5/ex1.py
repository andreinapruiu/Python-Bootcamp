# Method 1: String slicing
num = input("Enter an integer: ")
reversed_str = num[::-1]
print("Reversed (method 1):", reversed_str)

# Method 2: Using math
n = int(num)
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10
print("Reversed (method 2):", rev)
