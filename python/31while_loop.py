i = 1
j = 100

#q1
print("ans 1: ")
while i <= 100 :
    print(i)
    i+=1

print("\n")

#q2
print("ans 2: ")
while j >= 1 :
    print(j)
    j-=1

print("\n")

#q3
print("ans 3: ")
n = int(input("enter any number: "))
i =1
while i <= 10 :
    print(n*i)
    i+=1

print("\n")

#q4
print("ans 4: ")
nums = [1,4,9,16,25,36,49,64,81,100]
r =0
while r < len(nums) :   #called as traverse
    print(nums[r])
    r+=1

print("\n")

#q5
print("ans 5: ")
nums = (1,4,9,16,25,36,49,64,81,100)
search = int(input("enter number from squares of 1-10: "))
r =0
while r < len(nums) :
    if(search == nums[r]):
        print(str(search) + " found at " + "nums[",r,"]")
        break
    else: 
        print(str(search) + " not found at nums[",r,"]")
    r+=1