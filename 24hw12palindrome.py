pal1 = [1,2,3,2,1]
pal2 = [1,"abc","abc",1]

cp_pal1 = pal1.copy()
cp_pal1.reverse()
cp_pal2 = pal2.copy()
cp_pal2.reverse()

if (pal1 == cp_pal1):
    print("YES ! pal1 is a palindrome")
    if(pal2 == cp_pal2):
        print("YES ! pal2 is a palindrome")
    else:
        print("NO, pal2 is not a palindrome")
else: 
    print("NO, pal1 is not a palindromes")