def print_even_indexed(txt):
    print("Printing only even index chars")
    for i, val in enumerate(txt):
        if i % 2 ==0:
            print(val)

def remove_n_chars(txt):
    i = int(input("Enter number of chars to remove: "))
    print(f"Removing N..{i} characters from string")
    print(txt[i:])

def count_substr(txt):
    sub = input("Enter substring to find: ")
    print(f"Counting {sub} substring from {txt}")
    print(txt.count(sub))

txt = input("Enter string: ")
print(f"Original string is {txt}")
print_even_indexed(txt)
print("-"*10)
remove_n_chars(txt)
print("-"*10)
count_substr(txt)