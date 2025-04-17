# Ask for 3 numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Calculate the sum
sum_result = num1 + num2 + num3

# Print True if the sum is a whole number and print the sum
print(f"Is this: {sum_result} a whole number?", sum_result.is_integer())