# Improved Python Code
# Student Marks and Grade Calculator

def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 75:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "D"


name = input("Enter your name: ")

marks = []

for i in range(1, 4):
    mark = int(input(f"Enter marks in Subject {i}: "))
    marks.append(mark)

total = sum(marks)
percentage = total / len(marks)
grade = calculate_grade(percentage)

print("\nStudent Details")
print("Name:", name)
print("Total Marks:", total)
print("Percentage:", percentage)
print("Grade:", grade)