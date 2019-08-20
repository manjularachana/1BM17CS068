lis=[]
while True:
    a=input("enter the list elements and -1 to stop")#accepting string input
    if a!="-1":
        lis.append(a)
    else:
        break
reslis=[]
for i in lis:
    if lis.index(i)%2==0:
        reslis.append(i)
print(reslis)
