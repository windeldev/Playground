def check_prime(n):
    ctr = 0
    msg = ""
    for i in range(1, n+1):
        if n % i == 0:
            ctr += 1
            msg += f"{i}\n"
    if ctr == 2:
        return f"{n} is prime!\nThe factors of {n}:\n" + msg
    else:
        return f"{n} is not a prime!\nThe factors of {n}:\n" + msg

num = int(input("Enter number to check if prime? "))
print(check_prime(num))