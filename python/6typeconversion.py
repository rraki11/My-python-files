# type conversion

a = 25 # integer data type
b = 5.5 # float data type <- and it is the superior
sum = a + b

print(sum) # python automatically converts to the superior data type, here that is "float" data type

# type casting

x = "2"
print(type(x)) # now x is the string data type

y = int("2")
print(type(y)) # now y is converted to string data type to integer data type

'''
if we did the type casting in this form -> y = float("rakesh") then we will get an error cause we cant convert a string data type into float data type 

we should always keep the above situation in caution and proceed in a correct way
'''