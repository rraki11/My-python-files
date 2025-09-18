num = int(input("enter a range for finding sum of that range: "))

i=1
sum = 0
while i <= num:
    sum = i+sum
    i+=1
print("total sum:",sum)