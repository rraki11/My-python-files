#recursive function to calculate sum of first n natural numbers
def n_natural_sums(x):
    if(x==0):
        return 0
    return n_natural_sums(x-1)+x

print(n_natural_sums(3))

#recursie function to print all the elements of a list
lliisstt = [1,2,3,4,5]
def list_show(list,idx=0):
    if(idx==len(list)):
        return
    print(list[idx], end=" ")
    list_show(list,idx+1)

list_show(lliisstt)