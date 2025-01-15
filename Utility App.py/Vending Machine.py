#SA2} CodeLab 1} Vending Machine.py

class VendingMachine:
    def __init__(self):
        # Setting up the products categories, Stocks, and the prices
        self.menu = {
            "Snacks": {
                11: ("Lays Classic", 1.5),
                12: ("Pringles", 5.5),
                13: ("Ruffle Original", 20.0),
                14: ("Doritos Nacho", 2.5),
                15: ("Cheetos Crunchy", 1.5),
                16: ("Safari Chips", 7.5),
                17: ("Sohar Chips", 3.25),
                18: ("Oman Chips", 1.75),
                19: ("kurekure", 1.25),
                20: ("Bugles Chips", 2.0),
            },
            "Candies": {
                21: ("Astor", 2.5),
                22: ("Skittles", 2.75),
                23: ("Fruitella", 2.0),
                24: ("Lollipop", 1.0),
                25: ("Mentos", 2.5),
                26: ("GummyBears", 5.0),
                27: ("Marshmallows", 2.0),
                28: ("Chewing Gum", 1.0),
            },
            "Drinks": {
                29: ("Pepsi", 5.0),
                30: ("Fanta", 5.0),
                31: ("Dr.Pepper", 6.5),
                32: ("Lemon Soda", 2.0),
                33: ("Monster", 10.0),
                34: ("Coca Cola", 5.0),
            },
            "Others": {
                35: ("Water", 2.0),
            },
            "Chocolates": {
                36: ("Kitkat", 5.0),
                37: ("Flutes", 2.0),
                38: ("Quanta Flori", 1.5),
                39: ("Kinder Bueno", 5.0),
                40: ("Lindt", 5.0),
                41: ("Ferrero Rocher", 6.5),
                42: ("Milka Chocolate", 4.0),
                43: ("Snickers", 6.5),
                44: ("Bounty", 5.7),
                45: ("Rafaello", 8.0),
            },
        }
        # Setting the stock quantity for items
        self.stock = {code: 6 for category in self.menu.values() for code in category}

    def display_menu(self):
    # Organizing and displaying the menu by type in a table format
     print("""\nWelcome to Haifa's Vending Machine! Please explore our menu:
____________________________________________________________""")
             
     print(f"{'Category':<10} {'Code':<5} {'Item':<15} {'Price (AED)':<10} {'Stock':<6}")
     print("-" * 60)
     for category, items in self.menu.items():
        # Displaying the category name
        print(f"\n{category}:")  
        for code, (name, price) in items.items():
            stock_status = "Out of stock" if self.stock[code] == 0 else self.stock[code]
            print(f"{'':<10} {code:<5} {name:<15} {price:<10.2f} {stock_status:6}")


    def suggest_items(self, selected_code):
        """Recommend more items based on the user's choice."""
        # Setting the recommendations for the specific products
        suggestions = {
            # If a drink is selected, suggest Snickers or Kitkat
            30: [43, 36], 
            # If Lindt is selected, suggest Pepsi or Water 
            40: [29, 35],  
            # If Lays Classic is selected, suggest Marshmallows or Mentos
            11: [27, 25],  
            # If Monster is selected, suggest Oman chips or Safari Chips
            33: [18, 16], 
             # If Lollipop is selected, suggest Water or Fanta 
            24: [35, 30], 
        }
        if selected_code in suggestions:
            print("\nYou might be also insterested in these:")
            for suggestion in suggestions[selected_code]:
                # Suggest only available items in stock
                if suggestion in self.stock and self.stock[suggestion] > 0:
                    name, price = self.get_item_details(suggestion)
                    print(f"  {suggestion} - {name} ({price:.2f} AED)")

    def get_item_details(self, code):
        """Getting details of the item based on its code."""
        for items in self.menu.values():
            if code in items:
                return items[code]
        return None, None

    def purchase(self):
        """Process the purchase, supporting multiple item orders."""
        while True:
            self.display_menu()
            try:
                 code = int(input("\nPlease enter the item code you wish to purchase (or 0 to quit): "))
                 if code == 0:
                     print("Thanks for checking us out!")
                     break

                 # Finding the item within the menu.
                 selected_item = None
                 for category, items in self.menu.items():
                      if code in items:
                        selected_item = items[code]
                        break

                 if not selected_item:
                    print("Oops! Invalid code. Try again.")
                    continue

                 name, price = selected_item
                 if self.stock[code] <= 0:
                     print("Unfortunately, this item is out of stock.")
                     continue

                 print(f"You selected: {name} ({price:.2f} AED)")
                 money = float(input("Insert money (AED): "))

                 if money < price:
                    print("Insufficient balance. Please insert additional cash.")
                    continue

                 change = money - price
                 self.stock[code] -= 1
                 print(f"Dispensing {name}...")
                 print(f"Change returned: {change:.2f} AED")

                 another = input("Do you wish to buy anything else? (yes/no): ").strip().lower()
                 if another != "yes":
                    print("Thanks for your purchase! Have a great day!")
                    break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
if __name__ == "__main__":
    # Generate an instance of this class.
    vm = VendingMachine()  
    # Call the function to process the purchase.
    vm.purchase()          
