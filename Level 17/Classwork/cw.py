# 1. while loop-ის მეშვეობით გამოიტანეთ ციფრები 0-დან 10-მდე.

num = 0
while num<10:
    print(num)
    num = num + 1

# 2. while loop-ის მეშვეობით გამოიტანეთ ციფრები 20-დან 10-მდე.

num = 20
while num != 10:
    print(num)
    num = num - 1

# 3. while loop-ის მეშვეობით გამოიტანეთ 'goa' 5-ჯერ.

a=("goa")
b=1
while b<=6:
    print(a) 
    b=b+1

# 4. მომხმარებელს შემოატანინეთ საიდუმლო სიტყვა და თუ ის დაემთხვა თქვენს საიდუმლო სიტყვას, დაუპრინტეთ 'match'.

secretword = ("Goa")
user_guess = (input("Enter Secret Word: "))
while user_guess != secretword:
    user_guess = (input("Enter Secret Word: "))

print("Match")