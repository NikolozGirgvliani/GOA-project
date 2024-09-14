# 1. შექმენით სია, სადაც დაამატებთ 5 ელემენტს, შემდეგ კი გამოიტანე მესამე და მეოთხე ელემენტები

list = ['Doner', 'Kebab', 'Nacho', 'Alejandro', 'Garnacho']

print(list[2:4])

# 2. შექმენით სია, სადაც დაამატებთ 5 ელემენტს, შემდეგ მომხმარებელს შემოატანინეთ რიცხვი
#  და რომელ რიცხსაც შემოიტანთ მისი ინდექსი დაპრინტეთ

items = ['Kit-Kat', 'Sprite', 'Snickers', 'Coca-Cola', 'Fanta']

print(items)

user_input = int(input("Choose an item: "))
if 0 <= user_input < len(items):
    print(f"You selected: {items[user_input]}")
else:
    print("Invalid item. Please choose an item.")


