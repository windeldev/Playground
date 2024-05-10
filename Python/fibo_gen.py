import sys

if sys.argv[1]:
	n=int(sys.argv[1])
else:
	n=int(input("Fibo nth? "))
	
f0=0
f1=1

#0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144
out=[]

if n < 0:
	out="Invalid input."
elif n==0:
	out.append(f0)
elif n==1:
	out.extend([f0,f1])
else:
	out.extend([f0,f1])
	for i in range((n-1) or 1):
		f3=f0+f1
		out.append(f3)
		f0=f1
		f1=f3
print("Fibo series",",".join([str(x) for x in out]))
print("Sum",sum(out))
