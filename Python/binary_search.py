import sys

def binary_search(search_list, search_item):
    def check_list(l):
        nonlocal n, found, msg
        n += 1
        mid_index = int((len(l)-1)/2)
        mid_index_value = l[mid_index]
        if mid_index_value == search_item:
            msg += f"Found {search_item} after {n}"
            found = True
        else:
            if search_item > mid_index_value:
                return l[mid_index+1:]
            else:
                return l[:mid_index]

    msg = "Search list is empty!"
    if search_list:
        msg = f"Search list:\n{' '.join(search_list)}\n"
        found = False
        n = 0
        rl = search_list
        for i in range(len(search_list)):
            if not found and rl:
                rl = check_list(rl)
            else:
                break
            i += 1
        if not found:
            msg += f"{search_item} not found in list!"
    return msg

ilist = []
while True:
    input1 = input("Provide the search list(delimited by comma): ")

    if input1 == "bye": sys.exit()
    else:
        if input1.count(",") == 0: print("Invalid input list!")
        else:
            ilist = input1.split(",")
            if ilist.count("") == len(ilist):  print("Invalid input list!")
            else: break

while True:
    item = input("Provide the search item: ")

    if item == "bye": sys.exit()
    else:
        if item:
            break
        else:
            print("Invalid search item! Please try again.")

print(binary_search(ilist, item))

"""Binary search (requires sorted list)
1. Get mid index(MI) [int(len / 2)]
2. Check mid index value(MIV) = search item(SI) -> end if true
3. if false check if SI > MIV -> proceed to step 5
4. if SI > MIV is false -> proceed to step 7
5. Update list to contain MI+1 : len(list)
6. Use new list and repeat steps 1 - 4
7. Update list to contain 0 : MI-1
8. Use new list and repeat steps 1 - 4
 
"""
