limit = int(input("Enter a number: "))
a, b = 0, 1
fibonacci = []

while a <= limit:
    fibonacci.append(a)
    a, b = b, a + b

print("Fibonacci sequence:", fibonacci)
