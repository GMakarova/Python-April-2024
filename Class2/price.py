# > $100 - 10%
# > $200 - 20%
# tax - 8%

discount=0

def calculate_tax(price):
    tax = price * 0.08
    return tax

def apply_discount(price, discount_percentage):
    discount = price * discount_percentage/100
    return discount

product_price=float(input("Enter price: "))

tax=calculate_tax(product_price)

if product_price > 100 and product_price <= 200:
    discount=apply_discount(product_price, 10)

elif product_price > 200:
    discount=apply_discount(product_price, 20)

total_price = product_price - discount + tax

print(f"Your price is {total_price} :) ")