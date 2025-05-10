# 1. ბეჭდავს ნომრებს 1-დან 10-მდე, ერთ ხაზზე, გამოყოფილი მძიმეებით.
print("Numbers from 1 to 10 in one line:")
numbers = ""
for i in range(1, 11):
    numbers += str(i) + ", " if i < 10 else str(i)
print(numbers)

# 2. ბეჭდავს ნომრებს 2, 4, 6, 8, 10 (მხოლოდ ლუწები 1-დან 10-მდე).
print("only odd numbers from 1 to ten:")
for i in range(2, 11, 2):
    print(i)

# 3. გამოთვლის და ბეჭდავს 1-დან 100-მდე რიცხვების ჯამს.
print("sum of numbers from 1 to 10:")
total = 0
for i in range(1, 101):
    total += i
print("ჯამი:", total)

# 4. იღებს რიცხვთა სიას და ბეჭდავს მხოლოდ ლუწ რიცხვებს.
print("Only odd numbers:")
nums = [3, 8, 11, 14, 17, 20, 23]
for num in nums:
    if num % 2 == 0:
        print(num)

# 5. იღებს რიცხვთა სიას და ბეჭდავს თითოეული რიცხვის კუბს.
print("square of every number:")
nums = [1, 2, 3, 4, 5]
for num in nums:
    print(num ** 3)
