# 1. შექმენით ცვლადი სახელად name, სადაც მომხმარებელს input-ის მეშვეობით შემოატანინებთ სახელს,
#  შემდეგ კი მისალმების მესიჯი, მაგალითად 'hello ' + (სახელი). 

name = input()
print(name)

print(f'Hello My King {name}')

# 2. შექმენით სამი ცვლადი, სამივეში შეინახეთ განსხვავებული ინფორმაციის ტიპები, შემდეგ კი დაპრინტეთ ისინი.

player = "Nikoloz"
Game = "Fifa"
Drink = "Fanta"

print(f'{player} is playing {Game} and he is drinking {Drink}')

# 3. შექმენით ცვლადი სახელად user_name, სადაც მომხარებელს შემოატანინებთ სახელს,
#  შემდეგ შექმენით ცვლადი სახელად last_name, სადაც მომხმარებელს შემოატანინებთ გვარს,
#  ბოლოს დაუპრინტეთ მსგავსი მესიჯი: 'hello ' + (სახელი) + (გვარი).

user_name = input()
last_name = input()

print(f'Hello {user_name} {last_name} you can take your seat')