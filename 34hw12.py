list = [1,4,9,16,25,36,49,64,81,100]
for values in list:
    print(values)

print("\n")

tup = (1,4,9,16,25,36,49,64,81,100)
x = int(input("enter any number to find(from 1 to 10 sq): "))
for val in tup:
    if(val == x):
        print(x,"found")
        break
    print(val)
else:
    print("END")

print("\n")

for i in range(10): #range(10) = from 0-10 and defaultly increase by 1
    print(i)

print("\n")

for j in range(1,10,2): #range(1,10,2) = starts from 1, goes till 10, with a increament of 2
    print(j)

print("\n")

for k in range(1,101):
    print(k)

print("\n")

for l in range(100,0,-1):
    print(l)

print("\n")

num = int(input("enter any number form multiplication table: "))
for m in range(1,11):
    print(m*num)