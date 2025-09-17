# break example
i = 0
while i <= 5:
    print(i)
    if i == 3:
        break
    i += 1
print("loop end (break example)\n")

# continue example
i = 0
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
print("loop end (continue example)")
