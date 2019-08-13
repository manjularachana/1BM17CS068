a,b=0,1
fibo=[]
n=int(input("enter the number of terms you want in fibonacci series:"))
while n>0:
	fibo.append(a)
	a,b=b,a+b
	n=n-1
print(fibo)
