set1 = {1,2,3,4}
print(set)
print(type(set))
print("----------------------------------------------------------------------------------------------------------------")
set2 = {1,1,2,2,3,3, "rakesh", "shubham", "rakesh"} #set stores only unquie value, so it will not repeat the values even if we did
print(set2)
print(len(set2)) #we stored 9 value, but set will remove the extra part and returns the lenght as 5
print("----------------------------------------------------------------------------------------------------------------")
empty_set = set() #empty set is initialized by "set()" method
empty_set.add(19)
empty_set.add(7)
empty_set.add(19) #ignores this value, cuz, it has occured 2nd time
empty_set.add(18)
print(empty_set)
empty_set.remove(18)
print(empty_set.add((1,2,3))) #sets can also store lists 
print("----------------------------------------------------------------------------------------------------------------")
print(empty_set)
print(len(empty_set))
print("----------------------------------------------------------------------------------------------------------------")
empty_set.clear() #set cleared
print(empty_set)
print("----------------------------------------------------------------------------------------------------------------")
collection = {"hi", "rakesh", "how", "are", "you"}
print(collection.pop()) #remvoes a random element and returns to us
print(collection.pop())
print("----------------------------------------------------------------------------------------------------------------")
set3 = {17, 18, 19, 20}
set4 = {18, 19, 21, 22}
print("----------------------------------------------------------------------------------------------------------------")
#sety.union(setx) <- it combines both sets value and returns a new set. and also it does removes the repeated values
print(set3.union(set4)) #new set = {17, 18, 19, 20, 21, 22}
print("----------------------------------------------------------------------------------------------------------------")
#sety.intersection(setx) <- it combines the both sets values and returns the common values
print(set3.intersection(set4)) #new set = {18, 19}