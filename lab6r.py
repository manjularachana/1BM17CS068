inputs=input("enter the string of brackets")
lisi=list(inputs)
flag=-1
class validity:
    global flag
    ou=[]
    def __init__(self,s):
        self.lisin=s
    def checkval(self):
        for i in self.lisin:
            if i=='(' or i=='[' or i=='{':
                self.ou.append(i)
            elif i==')':
                ele=self.ou.pop()
                if ele=='(':
                    continue
                else:
                    break
            elif i==']':
                ele=self.ou.pop()
                if ele=='[':
                    continue
                else:
                    break
            elif i=='}':
                ele=self.ou.pop()
                if ele=='{':
                    continue
                else:
                    break
a=validity(lisi)
print(lisi)
a.checkval()
print(a.ou)
if(len(a.ou)!=0):
    print("it is not valid")
else:
    print("valid")
