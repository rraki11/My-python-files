def nums_show(x):
    if (x == 0):
        return
    print(nums_show(x-1))

nums_show(5)