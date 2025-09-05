student = ["Rakesh", 17, 18, 19]
print("student = " + str(student))
print("student[2] = " +str(student[2]))

student[3]=7
print("student[3] = " + str(student[3]))

# list slicing, list_name [starting_idx : ending_idx]
marks = [1,2,3,4,5]
print(marks[1:3])
print(marks[:3])
print(marks[1:])
print(marks[-5:])
print(marks[-5:-3])

print(marks.append(7)) #adds in last of the list
print(marks)
print(marks.sort()) #sorts in ascending order
print(marks)
print(marks.sort(reverse=True)) #sorts in descending order
print(marks)
print(marks.reverse()) #reverses the list
print(marks)
print(marks.insert(3,19)) #insert value at specific index
print(marks)
print(marks.remove(1)) #removes the specifed element which first occured from the list
print(marks)
print(marks.pop(2)) #list.pop(idx) prints and removes the specific element at the specified index