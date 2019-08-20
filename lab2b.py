def reverse1(lis):
    lis2=lis.split(" ")
    lis2.reverse()
    a=" "
    lis=a.join(lis2)
    print(lis)
def reverse2(lis):
    lis1=lis.split(" ")
    res=""
    for i in lis1:
        res+=i[::-1]
        res+=" "
    print(res)
str1=input("enter the string")
reverse1(str1)
reverse2(str1)
        
