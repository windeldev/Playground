size = int(input("Size? "))

if size % 2 > 0:
	low = size // 2
	upp = low + 1
else:
	low = upp = size // 2
adj=upp-1
adj2=1
for x in range(upp):
	out=""
	for x in range(adj):
		out+=" "
	for y in range(adj2):
		out+="*"
	adj-=1
	adj2+=2
	print(out)
adj=upp-low+1-1
adj2=size-(((upp-low)*2) or 1)
for x in range(low):
	out=""
	for x in range(adj):
		out+=" "
	for y in range(adj2):
		out+="*"
	adj+=1
	adj2-=2
	print(out)

"""
///*
//***
/*****
//***
///*
"""
