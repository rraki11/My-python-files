# arithmetic operators

a = 19 # "=" is an assignment operator. in this case 19 is assigned to a
b = 7 # "=" is an assignment operator. in this case 7 is assigned to b

print(a + b) # addition
print(a - b) # substraction/difference
print(a * b) # muliplication/product
print(49 / 7) # division
print(49 % 7) # division but returns remainder (called as modulo)
print(2 ** 5) # returns a^b

# relational operators

print(a == b) # returns boolean value by comparing those both the variable's values i.e, False in our case
print(a != b) # returns boolean value, "!=" is said as "not equal to" operator. It is the opposite of "equal to operator =="
print(a >= b) # returns True because 19 is greater than 7
print(a > b)
print(a < b)
print(a <= b) # returns False because 19 is not smaller than 7

# assignment operator

x = 17
y = 18

x += y # this means, x = x + y
print(x)
x -= y # this means, x = x - y, now x value will be 35 due to its above operation
print(x)

"""
other assignment operators
-   *= (it means, z = z * y)
-   %= (it means, z = z % y)
-   /= (it means, z = z / y)
-   **= (it means, z = z ** y i.e, z = z^y)
"""

# logical operators (these works on the boolean values)

print(not (a > b)) # even though 19 is greaters than 7 it will print False cause we used "not" operator which will make the conditon reverse
val1 = True
val2 = True
print(val1 and val2) # it will return "True" only when both the boolean values are True
print(val1 or val2) # it will return "True" when one of both the boolean values are True