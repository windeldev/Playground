#change the function
def adder(x, y, *args, **kwargs):
    sum = x+y
    for i in args+tuple(kwargs.values()):
        sum += i
    print(sum)

adder(2, 3)
adder(2, 3, 4)
adder(1, 2, 3, 7, 1, a=4, b=5)