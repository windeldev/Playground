def show_curr_prev(num):
    curr = 0
    prev = 0
    print(f"Printing current and previous number sum in a range({num})")
    for x in range(num):
        curr = x
        sum = curr + prev
        print(f"Current Number {curr} Previous Number {prev} Sum: {sum}")
        prev = curr

n = int(input("Enter range to sum: "))

show_curr_prev(n)