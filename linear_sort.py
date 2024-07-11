import sys

def linear_sort(in_list):
    out_list = []
    for i in in_list.split(","):
        pass

print("Linear Sort:")
print("Enter comma-delimited list of items to sort:")
print("Or enter bye to exit:")
while true:

    _input = input("Input:")
    if _input.strip().lower() == "bye": sys.exit()
    else:
        if _input.find(",") > -1: break
        else:
            print("Enter comma-delimited list of items to sort")

linear_sort(_input)

