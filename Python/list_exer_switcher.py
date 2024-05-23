def swap_via_ind(lst):
    if lst:
        lst[0] , lst[-1] = lst[-1] , lst[0]
    return lst

def swap_via_unpack(lst):
    if lst:
        a, *b, c = lst
        lst = [c, *b, a]
    return lst

def swap_via_slice(lst):
    if lst:
        lst = [lst[-1], *lst[1:-1], lst[0]]
    return lst


sample = ['1','7','4','2','8','9']
sample2 = [6, 5, 8, 0, 1, 3, 3]
sample3 = ['5', '1']

print(f"indices {swap_via_ind(sample)}")
print(f"unpacking {swap_via_unpack(sample3)}")
print(f"unpacking {swap_via_slice(sample2)}")