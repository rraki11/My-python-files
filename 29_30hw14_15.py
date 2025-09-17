marks = {}

phym = int(input(("enter your phy marks: ")))
marks.update({"phy" : phym})

chemm = int(input(("enter your chem marks: ")))
marks.update({"chem" : chemm})

maths = int(input(("enter your maths marks: ")))
marks.update({"maths" : maths})
print(marks)

num1 = {9, "9.0"}
print(num1)

# or 

num2 = {
    ("float", 9.0),
    ("int", 9)
}
print(num2)