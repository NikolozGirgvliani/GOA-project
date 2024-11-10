# 1. შექმენით ფუნქცია, სადაც გექნებათ 5 სიტყვიანი სია, შემდეგ მომხმარებელს შემოატანინეთ 0-იდან 5-მდე რიცხვი,
# და დაუპრინტეთ ეგ index თქვენი შექმნილი სიიდან.
def vending_machine():
    items = ['Coca-Cola', 'Sprite', 'Fanta', 'Burger', 'Kubdari']

    print("Available items:")
    print(items)

    user_choice = int(input('Enter a number between 0-4: '))
        
    if 0 <= user_choice < 4:
        print(f'Excellent! Your item: {items[user_choice]}')
    else:
        print('Invalid choice, please select a number between 0 and 4.')


vending_machine()




