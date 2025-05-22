def even_or_odd():
    value = input("3. Enter a number: ")
    if value.isdigit():
        num = int(value)
        return "It's even" if num % 2 == 0 else "It's odd"
    else:
        print("Wrong input")
        return even_or_odd()

print(even_or_odd())
