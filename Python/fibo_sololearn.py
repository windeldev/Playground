import sys

if sys.argv[1]:
	num=int(sys.argv[1])
else:
	num=int(input("Fibo nth? "))

f0=0
f1=1
def fibonacci(n):
	global f0,f1
	#complete the recursive function
	if n<=1:
		print(f0)
		print(f1)
		return f0,f1
	else:
		f0,f1 = (fibonacci(n-1))
		f3=f0+f1
		print(f3)
		f0=f1
		f1=f3
		return f0,f1

fibonacci(num-1)

"""
Sample Input
6

Sample Output
0
1
1
2
3
5
4
"""