def dec_to_bin(n):
    lst = []
    while n >= 1 :
        lst.append(str(n % 2))
        n = int(n / 2)
    lst.reverse()
    return " ".join(lst)

num = int(input("Give a decimal number? "))
print(dec_to_bin(num))


#65
#8
#9
#128 64 32 16 8 4 2 1
#           1 1 0 0 0
#9 % 2 = 1
#4 % 2 = 0
#2 % 2 = 0
#1 % 2 = 1




