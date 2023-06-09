# Complete the exercises at the bottom of today's lecture notes.

# Recreate your shopping cart program with OOP:

# The user should be able to :
# add items,
# delete items,
# check their cart, 
# quit

# When the user selects quit it should break our of the program and display the items in their cart.



class ShoppingCart():
    def __init__(self):
        self.items = {}
    
    # add item/price function
    def add_item(self, item, price):
        self.items[item] = self.items.get(item, 0) + price
        print(f"{item} has been added to your cart for ${price}.")

    # remove item function
    def del_item(self, item):
        if item in self.items:
            del self.items[item]
        print(f"{item} has been removed from your cart.")

    # view cart function
    def view_cart(self):
        if self.items:
            for item, price in self.items.items():
                print(f"Your cart has the following items: {item} | ${price} ")
   
    def run(self):

        print("""
                <<-----Shopping Menu----->>
                1. Add item
                2. Delete Item
                3. View Shopping Cart
                4. Quit
                """)
        
        while True:
            option = input("Choose your option: ")
            if option == "1":
                item = input("Add item to your shopping list: ")
                price = int(input("Enter the price of the item: $"))
                self.add_item(item, price)
            elif option == "2":
                item = input("Which item(s) do you want to delete? ")
                self.del_item(item)
            elif option == "3":
                self.view_cart()
            elif option == "4":
                print("<===The Final List===>")
                for item, price in self.items.items():
                    print(f"{item} | ${price}")
                    total = sum(self.items.values())
                    print(f"Your total bill is ${total}")
                    print("Thank you for shopping at V-Mart!")
                    break
            else:
                print("That is not a valid choice!")

cart = ShoppingCart()
cart.run()