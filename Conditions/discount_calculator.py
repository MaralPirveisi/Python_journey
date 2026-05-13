price = float(input("Enter total price:"))
if price < 100:
    discount = 0

elif price < 500:
    discount = 10

elif price < 1000:
    discount = 20

else:
    discount = 30

discount_amount = price * (discount / 100)
final_price = price - discount_amount

print(f"Discount: {discount}%")
print(f"Final price: {final_price}")
