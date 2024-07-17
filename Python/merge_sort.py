import sys
def halve(_in_list, st, ed):
    half_len = int(len(_in_list) / 2)
    if half_len > 1:
        return halve(_in_list[:half_len])
    else:
        return _in_list[0]

def merge_sort(in_list):








    lst_len = len(in_list)
    for i in range(lst_len):
        for j in range(i+1, lst_len):
            tmp = ''
            if in_list[i] > in_list[j]:
                tmp = in_list[i]
                in_list[i] = in_list[j]
                in_list[j] = tmp
    return in_list

print("Merge Sort:")
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
print("After:",",".join(merge_sort(_input.split(","))))

