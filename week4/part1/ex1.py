def get_average_from_grades():
    try:
        grades_input = input("Enter grades separated by commas: ")
        grades = [float(g.strip()) for g in grades_input.split(",")]
        avg = sum(grades) / len(grades)
        print(f"Average: {avg:.2f}")
    except ValueError:
        print("One or more inputs are not valid numbers.")

get_average_from_grades()
