unit = int(input("จำนวนสินค้า"))
price = float(input())
member = input("Member? y or n")
total = unit * price
discount = 0
amount = 0

if member == "y":
    if total <= 500:
        discount = total * 0.1

    elif total > 500 and total < 1000:
        discount = total * 15 / 100

    else:
        discount = total * 20 / 100

elif member == "n":
    if total <= 500:
        discount = total * 0.05

    elif total > 500 and total < 1000:
        discount = total * 10 / 100

    else:
        discount = total * 15 / 100

amount = total - discount
print("Total %0.2f"% total)
print("Discount %0.2f"% discount)
print("Amount %0.2f"% amount)

