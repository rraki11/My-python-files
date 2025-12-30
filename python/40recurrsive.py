def nums_show(x):
    if (x == 0):
        return
    print(x, end=" ")
    nums_show(x-1)

nums_show(10)

#factorial function
def factorial(x):
    if(x == 0 or x == 1):
        return 1
    return x*factorial(x-1)
print("\n")
innum = int(input("enter a number to find its factorial: "))
print("factorial of",innum,"is:",factorial(innum))