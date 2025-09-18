r = int(input("enter the range to find the factorial: "))

fact=1
i=1
for i in range(1,r):
    i+=1
    fact*=i

print("factorial:",fact)