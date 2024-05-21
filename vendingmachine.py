class vendingmachine():
    def __init__(self) -> None:
        # Initialize drinks with their prices and quantities
        self.drinks = {
            'Soda': [2, 5],
            'Bottled Water': [1, 5],
            'Energy Drinks': [3, 5],
            'Iced Tea': [2, 5],
            'Juices': [3, 5]
        }
        self.changes = 5  # Maximum change the machine can return
        self.total_sales = 0  # Total sales counter
        self.order = {}  # Customer's order
        self.totalprice = 0  # Total price of the order

    def showsmenu(self):
        # Display the available drinks and their quantities
        for key in self.drinks:
            print(f"Drinks: {key},\t Quantity: {self.drinks[key][1]}")

    def buydrink(self):
        # Display the drink menu and prompt the user to select drinks
        userdrink = ''
        self.showsmenu()
        while userdrink != 'Continue':
            userdrink = input("Please choose your drinks or type 'Continue', if you want to cancel or continue to pay\n")
            if not userdrink:
                print("Please insert your drink")
            elif userdrink in list(self.drinks.keys()):
                # Handle quantity input and ensure it's valid
                try:
                    quantity = int(input("How much do you want?\n"))
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
                    continue
                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue
                # Add selected drink and quantity to the order
                self.order[userdrink] = quantity
                if self.drinks[userdrink][1] >= quantity:
                    self.totalprice += (self.drinks[userdrink][0] * quantity)
                    print("\nThis is your current order:")
                    for key in self.order:
                        print(f"Drinks: {key},\t Quantity: {self.order[key]}")
                # If the drinks is out of stock
                else:
                    print("The drink is out of stock\n")
            elif userdrink == 'Continue':
                continue
            else:
                print('Your drink is not in the list. Try again')

    def getchanges(self):
        # Handle the payment and change dispensing logic
        currentmoney = 0
        while True:
            try:
                # Prompt the user to insert money
                money = int(input("Insert your money or type '0' to cancel the drinks:"))
            except ValueError:
                print("Invalid input. Please enter a valid amount.")
                continue
            if money < 0:
                print("Money cannot be negative. Please enter a valid amount.")
                continue
            # Accumulate the inserted money
            currentmoney += money
            changes = currentmoney - self.totalprice
            if changes >= 0:
                if changes <= self.changes:
                    # If there is sufficient change, dispense the change and complete the transaction
                    print("This is your change: " + str(changes) + "\nEnjoy your drink")
                    break
                else:
                    # If the machine cannot provide change, return the inserted money
                    print("I'm very sorry as we don't have any changes now. This is your " + str(currentmoney) + " back")
                    break
            else:
                # If more money is needed, prompt the user to insert the remaining amount
                print("Please insert another RM" + str(abs(changes)) + " to buy the drinks")

    def main(self):
        print('Hello, What do you like for drinks?')
        self.buydrink()
        print(f'This is your order:')
        for key in self.order:
            print(f"Drinks: {key},\t Quantity: {self.order[key]}")
        print('The total price is ' + str(self.totalprice))
        if input("Do you want to modify the order? Yes or No").strip().lower() == 'yes':
            self.buydrink()
        self.getchanges()

if __name__ == "__main__":
    machine = vendingmachine()
    machine.main()
