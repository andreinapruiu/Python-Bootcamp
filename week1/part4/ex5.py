my_dict = {
    "student_1": {
        "math": [4, 4, 5, 5],
        "physics": [4, 5, 5, 6],
        "english": [8, 9, 9, 10]
    },
    "student_2": {
        "math": [8, 10, 10, 7],
        "physics": [8, 10, 10, 10],
        "english": [7, 5, 1, 8]
    },
    "student_3": {
        "math": [9, 9, 9, 10],
        "physics": [8, 7, 10],
        "english": [10, 10, 9, 10]
    }
}

# Average of each subject for each student
for student, subjects in my_dict.items():
	print(f"\nAverage for {student}:")
	for subject, grades in subjects.items():
		average = sum(grades) / len(grades)
		print(f"  {subject}: {average:.2f}")

# Round up the averages
for student, subjects in my_dict.items():
	print(f"\nRounded average for {student}:")
	for subject, grades in subjects.items():
		average = sum(grades) / len(grades)
		rounded_average = round(average)
		print(f"  {subject}: {rounded_average}")

# Average of each student of all subjects
for student, subjects in my_dict.items():
	print(f"\nAverage for {student}:")
	average = sum(sum(grades) for grades in subjects.values()) / sum(len(grades) for grades in subjects.values())
	print(f"  Overall: {average:.2f}")

# Round up the averages
for student, subjects in my_dict.items():
	print(f"\nRounded average for {student}:")
	average = sum(sum(grades) for grades in subjects.values()) / sum(len(grades) for grades in subjects.values())
	rounded_average = round(average)
	print(f"  Overall: {rounded_average}")

def passed(grades):
    return sum(grades) / len(grades) >= 5

s1_math = passed(my_dict["student_1"]["math"])
s2_math = passed(my_dict["student_2"]["math"])
s3_english = passed(my_dict["student_3"]["english"])

print("Student 1 passed Math:", s1_math)
print("Student 2 passed Math:", s2_math)
print("Student 3 passed English:", s3_english)
