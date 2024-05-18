import re

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "stingray"):
    print("Match 3")

word = input()
#your code goes here

ptrn = r"^m..e$"
if re.match(ptrn, word):
    print("Match")
else:
    print("No match")