# Messy Python Code

name=input("Enter your name:")
marks1=int(input("Enter marks in Subject 1:"))
marks2=int(input("Enter marks in Subject 2:"))
marks3=int(input("Enter marks in Subject 3:"))

total=marks1+marks2+marks3
percentage=total/3

print("Name:",name)
print("Total Marks:",total)
print("Percentage:",percentage)

if percentage>=90:
 print("Grade: A")
elif percentage>=75:
 print("Grade: B")
elif percentage>=60:
 print("Grade: C")
else:
 print("Grade: D")