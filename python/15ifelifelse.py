age = int(input("enter your age: "))

if (age >= 18):
    print("you can vote")
    print("you can drive")
elif (age < 18):
    print("you cant drive")
    print("you cant vote")
else:
    print("something went wrong")