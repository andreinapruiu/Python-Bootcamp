def check_number():
    try:
        input_str = input("Enter a number: ")
        num = float(input_str)
    except ValueError:
        print("Invalid character")
    else:
        print("No errors")
    finally:
        print("Exit")

check_number()
