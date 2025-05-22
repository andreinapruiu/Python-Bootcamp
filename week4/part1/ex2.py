def divide_ten_by_user_input():
    try:
        num = float(input("Enter a number: "))
        result = 10 / num
        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter a number.")
    except ZeroDivisionError:
        print("Cannot divide by zero.")

divide_ten_by_user_input()
