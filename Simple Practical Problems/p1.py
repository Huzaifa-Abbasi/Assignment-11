'''Design a Python program that calculates the total cost of items purchased by a customer based 
on the provided unit price and quantity, applying a discount of 10% if the total cost exceeds 
$1000.'''

items = []
total_cost = 0
while True:
    item = input("Enter the name of items ")
    items.append(item)
    price = int(input("Enter the price of items "))
    units = int(input("Enter the units of items "))
    cost = price * units
    total_cost += cost
    user_input = input("Do you want to add more items yes/no ").lower()
    if user_input == "no":
        break

if total_cost >= 1000:
    discount = total_cost * 0.9

    print(f" you Got the discount to Your times are {items} total Cost {discount}" )
else:
    print(items,total_cost)


