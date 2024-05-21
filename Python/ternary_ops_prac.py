balance = int(input())
to_cash = int(input())

#change the code
money_left = balance-to_cash if balance>=to_cash and to_cash>=500 else "Error"

print(money_left)