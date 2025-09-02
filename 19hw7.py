a = int(input("enter your 1st number: "))
b = int(input("enter your 2nd number: "))
c = int(input("enter your 3rd number: "))

if (a==b and b==c):
    print("all are equal")
elif (a>=b and a>=c):
    print(str(a) +" is the largest")
elif (b>=a and b>=c):
    print(str(b) +" is the largest")
else:
    print(str(c) +" is the largest")