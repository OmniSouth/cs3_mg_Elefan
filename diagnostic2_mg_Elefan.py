def calculate_total(topping_count):
    price = 10 + (topping_count*1.5)
    return price

Pizza = {"P": 0, "M": 0, "C": 0}

topping_count = 0
mult = 1
while True:
    print(f"Current Toppings: {Pizza["P"]} Peperoni| {Pizza["M"]} Mushrooms| {Pizza["C"]} Extra Cheese ")
    topping_input = str(input("\nEnter Toppings (Only Peperoni, Mushrooms and Extra Cheese are on stock! Say 'Done' to end): "))
    if topping_input == "Peperoni" or topping_input == "peperoni":
        topping_count = topping_count + 1
        Pizza["P"] = Pizza["P"] + 1
    elif topping_input == "Mushroom" or topping_input == "mushroom":
        topping_count = topping_count + 1
        Pizza["M"] = Pizza["M"] + 1
    elif topping_input == "Extra Cheese" or topping_input == "extra cheese":
        topping_count = topping_count + 1
        Pizza["C"] = Pizza["C"] + 1
    elif topping_input == "Done" or topping_input == "done":
        break
    elif topping_input == "PYTHON20":
        print("VIP Discount, -20% (Activates Once)")
        mult = 0.8
    else:
        print("Not in Menu")

print(f"${(calculate_total(topping_count)*mult)}")
