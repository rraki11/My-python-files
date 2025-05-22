value = input("enter any value: " )
print(value)
print(type(value))

"""
even though if you entered a number its data type will be a String data type cause whenever python takes an input from the keyboard it will take that input in a String format
"""

# to take the input as in other data type format we need to type cast

value2 = int(input("enter a number: "))
print(type(value2), value2)