

# 1. დაპრინტე სიის გასსამმაგებული კენტი რიცხვები
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("numbers * by 3:")
for num in numbers:
    if num % 2 != 0:
        print(num * 3)

# 2. დაპრინტე ყველა 25-ზე დიდი რიცხვი
numbers = [10, 20, 30, 40, 50, 60]
print("numbers bigger than 25:")
for num in numbers:
    if num > 25:
        print(num)

# 3. დაპრინტე ისეთი რიცხვები, რომლებიც უნაშთოდ იყოფა 10-ზე
numbers = [5, 10, 15, 20, 25, 30]
print("Numbers that can be subtracted by 10")
for num in numbers:
    if num % 10 == 0:
        print(num)

# 4. დაპრინტე სიის კენტი რიცხვების ფესვები
numbers = [1, 4, 9, 16, 25, 36, 49]
print("odd numbers square:")
for num in numbers:
    if num % 2 != 0:
        print(num * num)

# 5. დაპრინტე 4-ზე დიდი რიცხვების კვადრატები
numbers = [2, 3, 4, 5, 6, 7, 8]
print("square of numbers bigger than 4:")
for num in numbers:
    if num > 4:
        print(num ** 2)
