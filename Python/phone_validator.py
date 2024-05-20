import re

#your code goes here
patt = r'\A[189]\d{7}\Z'
inp = str(input())
if re.match(patt,inp):
    inp = "Valid"
else:
    inp = "Invalid"    

print(inp)
