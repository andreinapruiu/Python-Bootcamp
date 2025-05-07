total_classes = int(input("Total number of classes: "))
attended = int(input("Number of classes attended: "))
percentage = (attended / total_classes) * 100

print(f"Attendance: {percentage:.2f}%")
print("Greater than 75%" if percentage >= 75 else "Less than 75%")
