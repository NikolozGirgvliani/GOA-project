# 1. შექმენი პროგრამა, რომელიც ბეჭდავს ციფრებს 1-დან 10-მდე კონსოლში for ციკლის გამოყენებით.
print("numbers from 1 to 10:")
for i in range(1, 11):
    print(i)

# 2. შექმენი პროგრამა, რომელიც ბეჭდავს ყველა ლუწი რიცხვს 1-დან 20-მდე კონსოლში for ციკლის გამოყენებით.
print("odd numbers from 1 to 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# 3. შექმენი პროგრამა, რომელიც ითვლის და ბეჭდავს ყველა რიცხვის ჯამს 1-დან 50-მდე for ციკლის გამოყენებით.
sum = 0
for i in range(1, 51):
    sum += i
print("Su of numbers from 1 to 50:", sum)

# 4. შექმენი პროგრამა, რომელიც იღებს რიცხვთა მასივს და ბეჭდავს მხოლოდ 10-ზე მეტ რიცხვებს for ციკლის გამოყენებით.
print("Numbers which are > than 10:")
numbers = [5, 12, 9, 20, 3, 15]
for number in numbers:
    if number > 10:
        print(number)

# 5. შექმენი პროგრამა, რომელიც მიიღებს რიცხვების სიას და დაბეჭდავს თითოეული რიცხვის კვადრატს for ციკლის გამოყენებით.
print("Number Square:")
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number ** 2)
