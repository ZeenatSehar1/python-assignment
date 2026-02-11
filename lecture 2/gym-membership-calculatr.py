reg_fee = int(input("Enter registration fee: "))
monthly_fee = int(input("Enter monthly fee: "))
months = int(input("Enter number of months: "))

total = reg_fee + (monthly_fee * months)

coupon = input("Do you have a discount coupon? (yes/no): ")

# apply 10% discount using assignment operator
total *= 0.9 if coupon == "yes" else 1

print("Final amount to be paid:", total)
