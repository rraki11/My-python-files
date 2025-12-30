#hw22
def list_param(x):
    print(len(x))

list1 = [1,2,3,4,5]

list_param(list1)

#hw23
def print_list(y):
    for el in y:
        print(el, end=" ")

print_list(list1)
print("\n")

#hw24
def factorial_param(x):
    fact=1
    i=1
    for i in range(1,x+1):
        fact*=i
    print(fact)

num = int(input("enter any number: "))
factorial_param(num)

#hw25
def curruncy_convert(rs):
    convert=rs*87.83
    print(rs, "USD =",convert,"INR")

rupee = float(input("enter dollars: "))
curruncy_convert(rupee)

eo = int(input("enter any number: "))
def odd_even_check(x):
    if (x%2 == 0):
        print("even")
    else:
        print("odd")

odd_even_check(eo)