total_cost = 0
while True:
    price = input("Enter price: ")
    if price == "":
        break
    try:
        price = float(price)
    except ValueError:
        print("Invalid price:", price)
        continue
    total_cost += price
print("Total cost:", total_cost)
pennies = int(round(total_cost * 100, 0))
remainder = pennies % 5
if remainder < 2.5:
    cash_payment = total_cost - (remainder / 100)
else:
    cash_payment = total_cost + (5 - remainder) / 100
print("Cash payment:", cash_payment)