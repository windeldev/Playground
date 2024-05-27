def item_swap(ilist):
    if ilist:
        pos1 = int(input("Enter which position to swap from: "))
        pos2 = int(input("Enter which position to swap to: "))
        if isinstance(pos1,int) and isinstance(pos2,int):
            ilist = ilist.split(",")
            if len(ilist) > 0:
                ilist[pos1], ilist[pos2] = ilist[pos2], ilist[pos1]
                print(f"Modified list {ilist}")

def sum_items(ilist):
    if ilist:
        ilist = ilist.split(",")
        tot = 0
        for i in ilist:
            tot += int(i)
        print(f"Sum: {tot}")

lst = input("Enter list: ")
print(f"Original list {lst}")
item_swap(lst)
sum_items(lst)
