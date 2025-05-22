import csv
from collections import defaultdict

# Load the employees.csv once for reuse
with open("employees.csv", newline="") as f:
    reader = list(csv.reader(f))
    headers = reader[0]
    rows = reader[1:]

# Task 1: Print each row as-is
print("1. Raw content of employees.csv:")
for row in rows:
    print(row)

# Task 2: Read as list of lists
print("\n2. Content as list of lists:")
content_as_lists = [row for row in rows]
print(content_as_lists)

# Task 3: First & last name of the person with the highest salary
print("\n3. Person with highest salary:")
salaries = [int(row[4]) for row in rows]
max_index = salaries.index(max(salaries))
print(rows[max_index][0], rows[max_index][1])

# Task 4: Person with smallest salary
print("\n4. Person with smallest salary:")
min_index = salaries.index(min(salaries))
print(rows[min_index][0], rows[min_index][1])

# Task 5: Average salary
print("\n5. Average salary:")
avg_salary = sum(salaries) / len(salaries)
print(f"${avg_salary:.2f}")

# Task 6: Members in each department
print("\n6. Number of members per department:")
dept_count = defaultdict(int)
for row in rows:
    dept_count[row[3]] += 1
print(dict(dept_count))

# Task 7: Overwrite telephone numbers with ***
print("\n7. Overwriting telephone numbers with ***...")
updated_rows = [headers[:]]  # copy headers
for row in rows:
    modified = row[:]
    modified[5] = "***"
    updated_rows.append(modified)

with open("employees_anonymized.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(updated_rows)

# Task 8: Create a new.csv file with 5 rows and selected columns
print("\n8. Creating new.csv with selected columns and 5 rows...")
new_data = [["First name", "Last name", "Job Title", "Age"]] + [
    [row[0], row[1], row[2], row[6]] for row in rows[:5]
]
with open("new.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(new_data)
