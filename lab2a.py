def search(lis,a):
    print(lis)
    if a in lis:
        return True
    else:
        return False
lis=[]
while True:
    a=int(input("Enter the list elements"))
    if a!=-1:
        lis.append(a)
    else:
        break
b=int(input("enter teh element to search"))
res=search(lis,b)
if res:
    print("Element is present")
else:
    print("element is not present")
