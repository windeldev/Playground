import re

#your code goes here
patt = r'00'
inp = str(input())
if re.match(patt,inp):
    inp = re.sub(patt,"+",inp,1)

print(inp)
