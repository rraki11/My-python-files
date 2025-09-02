str1 = "Shubham"
str2 = 'Rakesh'
str3 = '''Shubham'''
print(str1)
print(str2)
print(str3)

#those many types of string declaration is used for below purposes
str4 = "Shuhbam's sister name is Supriya"
str5 = 'Supriys"s brother name is Shubham'
print("\n"+str4)
print(str5)

#operations on strings 
str6 = "Shubham"
str7 = "Routray"
final_len = str6 + " " + str7

#concatenation str1 + str2
print("\n"+str6+str7)

#lenght of a string len(str1)
len1 = len(str6)
print(len1)
len2 = len(str7)
print(len2)

print(final_len + "=" + str(len(final_len)))
print(f"{final_len}={len(final_len)}")  # print(f"") <- method used when we try to concatenate str + int
print("{}={}".format(final_len,len(final_len))) # print("{},{}".formate()) <- method for concatenation of str + int

#slicing str[starting_idx : ending_idx]
print("\n" + str6[ :7]) #same as print(str6[0:7])
print(str6[3:7])
print(str7[:]) #from starting index to ending
print(str7[3:]) #same as print(str7[3:len(str7)])

#negative slicing str[starting_idx : ending_idx]
str8 = "apple"  #apple <- -5 -4 -3 -2 -1
print("\n"+str8[-5:3])

#string.endswith("test text")
print(str8.endswith("LE."));
#string.captalize() , captalizes only the first character 
print(str8.capitalize()) #it doesn't make changes in original string i.e, str8
#string.replace("old","new")
str9 = "Im Shubham Routray from Warangal"
print("original text = " + str9)
print("replaced text = " + str9.replace("Warangal","Telengana"))