def add_numbers():
    val1 = 1
    val2 = 2
    result = val1 + val2
    return result

print(add_numbers())
print("-------------------------------------------------------------------------------------------------------------------------")

def add_numbers_with_params(a,b):
    sum = a + b
    print(sum)

add_numbers_with_params(7,19)
print("-------------------------------------------------------------------------------------------------------------------------")

def default_params(a,b=7): #dafault values of a and b is 1 and 7, even if we dont pass any values, we will not get any error
    mul = a*b
    print(mul)

default_params(19)
print("-------------------------------------------------------------------------------------------------------------------------")

print("rakesh", end="_")
print("routray")
print("-------------------------------------------------------------------------------------------------------------------------")

