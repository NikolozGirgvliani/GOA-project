# 1. სიაში შეინახეთ 5 რიცხვი, შემდეგ კი დარპინტეთ პირველი და მეოთხე ელემენტების ნამრავლი.

numbers = [2, 4, 6, 8, 10]

product = numbers[0] * numbers[3]

print("Product of the first and fourth numbers:", product)

# 2. სიაში შეინახეთ 7 სტრინგი, შემდეგ დაპრინტეთ შუა სტრინგი.

strings = ["Html", "Pyhton", "css", "javascript", "java", "sololearn", "Keyboard"]

middle_str = len(strings) // 2

print("Middle string:", strings[middle_str])

# 3. ცვლადში შეინახეთ სტრინგი, შემდეგ კი დაპრინტეთ ამ სტრინგის მხოლოდ მეორე ასო.

my_string = "Gamarjoba"

print("Second letter:", my_string[1])

# 4. შექმენით ვენდინგ მანქანის თამაში პითონის მეშვეობით, როგორც გაკვეთილზე გავაკეთე, უნდა გქონდეთ პროდუქტები,
# მომხმარებელს უნდა შეეძლოს არჩევა რიცხვის მიხედვით, შემდეგ კი უნდა დაუპრინტოს ის პროდუქტი, რომელიც ამოირჩია, პროდუქტები შეინახეთ სიაში.

def vending_machine():

    products = ["Koka-Kola", "Chips", "Snickers", "Banani", "Gum"]

    print("Welcome to the Vending Machine!")
    print("Please select a product by number:")
    
    for i, product in enumerate(products):
        print(f"{i + 1}. {product}")
    
    choice = int(input("Enter the number of the product you want: ")) - 1
    
    if 0 <= choice < len(products):
        print(f"You selected: {products[choice]}")
    else:
        print("Invalid selection. Please choose a number from the list.")

# Run the vending machine game
vending_machine()

