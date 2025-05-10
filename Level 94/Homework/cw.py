# 1. დაბეჭდე 0-დან 20-მდე რიცხვები, ყოველ ჯერზე 2-ით გაზრდით
num = 0
while num <= 20:
    print(num)
    num += 2


# 2. დაბეჭდე რიცხვები 10-დან 1-მდე, ყოველ ჯერზე აკლდება 1
num = 10
while num >= 1:
    print(num)
    num -= 1


# 3. დაითვალე რამდენი რიცხვია 1-იდან 5-მდე
num = 1
count = 0
while num <= 5:
    count += 1
    num += 1
print("numb:", count)



# 4. დაიწყე 1-დან და ყოველი იტერაციისას გაამრავლე 2-ზე, სანამ 100-ზე მეტი გახდება
num = 1
while num <= 100:
    print(num)
    num *= 2


# 5. მომხმარებელს შეაყვანინე რიცხვი და დაბეჭდე 1-იდან იმ რიცხვამდე
end = int(input("input number: "))
i = 1
while i <= end:
    print(i)
    i += 1

# 1. დაბეჭდე 1-დან 10-მდე ყველა რიცხვის კვადრატი
for i in range(1, 11):
    print(i**2)


# 2. დაბეჭდე 1-დან 50-მდე ყველა რიცხვი
for i in range(1, 51):
    print(i)


# 3. მიაწოდე სიას სახელები და დაბეჭდე: "გამარჯობა, [სახელი]!"
names = ['ana', 'ben', 'carl', 'dana', 'eva']
for name in names:
    print(f"hello, {name}!")


# 4. დაბეჭდე 100-დან 0-მდე ყველა რიცხვი, ყოველ ჯერზე 10-ით შემცირებით
for i in range(100, -1, -10):
    print(i)


# 5. მიაწოდე რიცხვების სია და დაბეჭდე მხოლოდ ლუწი რიცხვების ჯამი
numbers = [5, 8, 12, 7, 6, 3, 10]
even_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num
print("Odd numbers sum:", even_sum)
