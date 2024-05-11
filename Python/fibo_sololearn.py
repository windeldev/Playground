import sys

if sys.argv[1]:
	num=int(sys.argv[1])
else:
	num=int(input("Fibo nth? "))

def fibonacci(n):
	print(n)
	if n <= 1:
		return n
	else:
		return fibonacci(n-1) + fibonacci(n-2)

for i in range(num):
	print("i=",i)
	print(">>>",fibonacci(i))

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
8
"""
