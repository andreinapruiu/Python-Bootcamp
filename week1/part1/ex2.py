# Ask for age in years
years = int(input("Enter your age in years: "))

# Ask how many months passed since last birthday
months_since_birthday = int(input("How many months have passed since your last birthday? "))

# Calculate total months since birth
total_months = years * 12 + months_since_birthday

print("Total months since you were born:", total_months)
