def print_even_indexed(txt):
    print(f"Original string is {txt}")
    print("Printing only even index chars")
    for i, val in enumerate(txt):
        if i % 2 ==0:
            print(val)


txt = input("Enter string: ")
print_even_indexed(txt)
