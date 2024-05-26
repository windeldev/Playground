def print_even_indexed(txt):
    print("Printing only even index chars")
    for i, val in enumerate(txt):
        if i % 2 ==0:
            print(val)

def remove_n_chars(txt):
    print(f"Removing N..{i} characters from string")
    i = int(input("Enter number of chars to remove: "))
    print(txt[i:])
    
txt = input("Enter string: ")
print(f"Original string is {txt}")
print_even_indexed(txt)
print("-"*10)
remove_n_chars(txt)