my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Ask for a number
number = int(input("Enter a number: "))

# Append the number to the end of the list
my_list.append(number)

# Delete the 4th element
del my_list[3]

# Append the index of the element '9' to the end of the list
my_list.append(my_list.index(9))

# Delete the element with the highest value
highest_value = max(my_list)
my_list.remove(highest_value)

# Reverse the list
my_list.reverse()

# Put the sum of the first 5 elements in a variable
sum_of_first_5 = sum(my_list[:5])
print("The sum of the first 5 elements is:", sum_of_first_5)

# Put the average of the last 5 elements in a variable
average_of_last_5 = sum(my_list[-5:]) / 5
print("The average of the last 5 elements is:", average_of_last_5)

# Print the difference between the first and last elements
difference = my_list[0] - my_list[-1]
print("The difference between the first and last elements is:", difference)