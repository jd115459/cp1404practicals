price_total = 0
number_of_items = int(input("Number of Items: "))
while number_of_items < 0:
    print("Invalid number of Items!")
    number_of_items = int(input("Number of Items: "))

for i in range(number_of_items):
    price = float(input("Price of Item: "))
    price_total += price

if price_total > 100:
    price_total = price_total - (price_total * 0.1)

print(f"Total price for {number_of_items} items is: {price_total}")