def swap_via_ind(lst):
    if lst:
        lst[0] , lst[-1] = lst[-1] , lst[0]
    return lst

def swap_via_unpack(lst):
    if lst:
        a, *b, c = lst
        lst = [c, *b, a]
    return lst


sample = ['1','7','4','2','8','9']
sample2 = [6, 5, 8, 0, 1, 3, 3]

print(f"indices {swap_via_ind(sample)}")
print(f"unpacking {swap_via_unpack(sample2)}")