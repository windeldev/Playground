import re

#your code goes here
patt = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
inp = str(input())
m = re.search(patt,inp)
if m:
    inp = m.group()

print(inp)
