import sys
def merge_sort(in_list):
    # 9,2,3,1
    if len(in_list) <= 1:
        return in_list
    
    mid = len(in_list) // 2
    left = merge_sort(in_list[:mid])
    right = merge_sort(in_list[mid:])

    print(f'left {left}')
    print(f'right {right}')

    return merge(left, right)

def merge(left, right):
    res = []
    i = j = 0

    print('start merge')

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])
    print(f'Left:{left},right:{right},Left[i:]:{left[i:]},Right:{right[j:]},merge:{res}')

    return res

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

