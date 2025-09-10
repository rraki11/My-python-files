dict = {
    "name" : "Rakesh",
    "age" : 18,
    "subjects_marks" : {        #we can also add dictionary inside a dictionary
        "phy" : 19,
        "chem" : 19,
        "java" : 19,
        "python" : 19
    },
    "topics" : ("dictionary", "sets"),
    "is_adult" : True
}
print("\n")

print(type(dict))
print("----------------------------------------------------------------------------------------------------------------")
print(dict)
print("----------------------------------------------------------------------------------------------------------------")
print(dict["name"])
print("----------------------------------------------------------------------------------------------------------------")
dict["name"] = "Shubham"    #modified name, python overwrites the value and modifies 
dict["surname"] = "Routray" #added new element
print(dict)
print("----------------------------------------------------------------------------------------------------------------")
print(dict["subjects_marks"])   #prints the whole nested values
print("----------------------------------------------------------------------------------------------------------------")
print("marks obtained in java: " + str(dict["subjects_marks"]["java"]))   #prints the specific value from the nested values

#methods used for dictionary
print(dict.keys()) #prints the keys present in the dictionary
print("----------------------------------------------------------------------------------------------------------------")
print(list(dict.keys())) #we can also type cast the dictionary
print("----------------------------------------------------------------------------------------------------------------")
print(len(list(dict.keys()))) #prints the lenght of the dictionary
print("----------------------------------------------------------------------------------------------------------------")
print(dict.values()) #prints only the dictionary values 
print("----------------------------------------------------------------------------------------------------------------")
print(dict.items()) #returns all (keys, values) pairs as tuples
print("----------------------------------------------------------------------------------------------------------------")
print(dict["name"])
print(dict.get("name"))
#both of them work same but, dict.get() method will not give error when an element is not present in the dictionary, instead of giving the error it returns "none".. the dict.get() method is useful when we write a large code, if we mistakenly gave the nonexisting element name it will run without error but returns "none"
print("----------------------------------------------------------------------------------------------------------------")
dict.update({"city" : "Hanamakonda"}) #inserts specific item into the dictionary
print(dict)


print("\n")