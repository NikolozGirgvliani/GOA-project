def vending_machine(products, prices, user_balance):
    print("Welcome to the vending machine! Here are some products:")
    print(products)

    user_choice = int(input("Please select product number 0-3: "))

    if 0 <= user_choice < len(products):
        if user_balance >= prices[user_choice]:
            print(f"You have selected {products[user_choice]} for ${prices[user_choice]}.")
            user_balance -= prices[user_choice]  # Deduct the price from the balance
            print(f"Remaining balance: ${user_balance}")
        else:
            print("Not enough money. Please select a cheaper product.")
    else:
        print("Invalid selection. Please try again.")

products = ["Water", "Soda", "Chips", "Candy"]
prices = [1.0, 1.5, 2.0, 1.25]
user_balance = 2.0

vending_machine(products, prices, user_balance)
