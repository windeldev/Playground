import sys

def linear_sort(in_list):
    lst_len = len(in_list)
    for i in range(lst_len):
        for j in range(i+1, lst_len):
            tmp = ''
            if in_list[i] > in_list[j]:
                tmp = in_list[i]
                in_list[i] = in_list[j]
                in_list[j] = tmp
    return in_list

print("Linear Sort:")
print("Enter comma-delimited list of items to sort:")
print("Or enter bye to exit:")
while True:

    _input = input("Input:")
    if _input.strip().lower() == "bye": sys.exit()
    else:
        if _input.find(",") > -1: break
        else:
            print("Enter comma-delimited list of items to sort")
print("Before:",_input)
print("After:",",".join(linear_sort(_input.split(","))))

