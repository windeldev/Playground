def vowel_count(txt):
    vowels = ['a','e','i','o','u']
    out = "Vowel Count:\n"
    txt = txt.lower()
    ntot = 0
    for x in vowels:
        n = txt.count(x)
        ntot += int(n)
        out += f"{x} - {n}\n"
    out += f"Total: {ntot}"
    return out

txt = input("Count vowels for which word? ")
if txt:
    print(vowel_count(txt))
else:
    print("Invalid input!")