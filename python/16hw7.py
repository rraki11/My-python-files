marks = float(input("enter you marks (<=100): "))

if (marks >= 90):
    grade='A'
elif (marks >= 80 and marks < 90):
    grade='B'
elif (marks >= 70 and marks < 80):
    grade='C'
else:
    grade='D'

print("grade of the student: " + grade)