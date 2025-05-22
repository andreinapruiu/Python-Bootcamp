user_input = input("Enter a string: ")

for char in user_input:
    if char.isdigit():
        print("String contains a number. Exiting...")
        break
else:
    print("There are no numbers in the string.")

print("Finish")
