class qtyError(Exception):
    pass

available_products_in_kg = {
    "rice": {"quantity_in_kg": 100, "price_per_kg": 50},
    "musor dal": {"quantity_in_kg": 100, "price_per_kg": 120},
    "muger dal": {"quantity_in_kg": 100, "price_per_kg": 140},
    "cholar dal": {"quantity_in_kg": 100, "price_per_kg": 110},
    "arohor dal": {"quantity_in_kg": 100, "price_per_kg": 130},
    "jira": {"quantity_in_kg": 50, "price_per_kg": 200},
    "sugar": {"quantity_in_kg": 100, "price_per_kg": 40},
    "salt": {"quantity_in_kg": 50, "price_per_kg": 20},
    "black pepper": {"quantity_in_kg": 50, "price_per_kg": 300},
    "red mirchi": {"quantity_in_kg": 60, "price_per_kg": 250},
}

print("Available Products:", available_products_in_kg)

Add_cart = {}

first_item_name = input("Enter the 1st item to cart: ")
if first_item_name in available_products_in_kg:
    first_item_qty = input("Enter quantity of 1st item in kg: ")
    try:
        available_qty = available_products_in_kg[first_item_name]["quantity_in_kg"]
        requested_qty = int(first_item_qty)
        if requested_qty > available_qty:
            raise qtyError("Your given quantity is out of stock.")
        Add_cart[first_item_name] = {
            "quantity": requested_qty,
            "price": requested_qty * available_products_in_kg[first_item_name]["price_per_kg"],
        }
        print("Item added to cart:", Add_cart)
    except qtyError as var:
        print(var)
else:
    print("Item not available.")


x = input("Do you want to add more items? (yes / no): ")
if x.lower() == "yes":
    second_item_name = input("Enter the 2nd item to cart: ")
    if second_item_name in available_products_in_kg:
        second_item_qty = input("Enter quantity of 2nd item in kg: ")
        try:
            available_qty = available_products_in_kg[second_item_name]["quantity_in_kg"]
            requested_qty = int(second_item_qty)
            if requested_qty > available_qty:
                raise qtyError("Your given quantity is out of stock.")
            Add_cart[second_item_name] = {
                "quantity": requested_qty,
                "price": requested_qty * available_products_in_kg[second_item_name]["price_per_kg"],
            }
            print("Item added to cart:", Add_cart)
        except qtyError as var:
            print(var)
    else:
        print("Item not available.")
else:
    print("Thank you for shopping!")
    x = "no"  


if x.lower() == "yes":
    x = input("Do you want to add more items? (yes / no): ")
    if x.lower() == "yes":
        third_item_name = input("Enter the 3rd item to cart: ")
        if third_item_name in available_products_in_kg:
            third_item_qty = input("Enter quantity of 3rd item in kg: ")
            try:
                available_qty = available_products_in_kg[third_item_name]["quantity_in_kg"]
                requested_qty = int(third_item_qty)
                if requested_qty > available_qty:
                    raise qtyError("Your given quantity is out of stock.")
                Add_cart[third_item_name] = {
                    "quantity": requested_qty,
                    "price": requested_qty * available_products_in_kg[third_item_name]["price_per_kg"],
                }
                print("Item added to cart:", Add_cart)
            except qtyError as var:
                print(var)
        else:
            print("Item not available.")
    else:
        print("Thank you!")

y = input("Do you want to remove any item? (yes / no): ")
if y.lower() == "yes":
    def remove():
        item_to_remove = input("Enter the item you want to remove: ")
        if item_to_remove in Add_cart:
            del Add_cart[item_to_remove]
            print("Updated Cart:", Add_cart)
        else:
            print("The entered item does not exist in the cart.")
    remove()



print("Final cart is:", Add_cart)
z = sum(item["price"] for item in Add_cart.values())
print("Your total bill is:", z)

print("THANK YOU FOR SHOPPING!")



