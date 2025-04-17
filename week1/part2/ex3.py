my_list = [1, 2, [1, 2, 3], 3, 4, [4, 5, 6, 7, 8], 4, 5, 6]

# Print the length of the list
print("The length of the list is:", len(my_list))
# The length of the list is 9 because each single element is counted as one, being a part of the list
# and also the nested list are counted only as one element so it's like having a list of 9 numbers

# Recreate the list but the elements from the nested list being inside the parent list
new_list =[]

for element in my_list:
	if isinstance(element, list):
		new_list.extend(element)
	else:
		new_list.append(element)

print("The new list is:", new_list)

# Print the number of occurences of the number 4
print("The number of occurences of the number 4 is:", new_list.count(4))