# 1)გააკეთეთ 5 მაგალითი while ციკლზე

a=input("Enter your name:")
b=1
while b<=5:
    print(a) 
    b=b+1

password = "nikolozi"
user_guess = input("Type Password:")
while user_guess != password:
    user_guess = input("Type Password:")
print("Password Correct")

Secret_Word = "GoaBest"
user_guess = input("Guess Secret Word:")
while user_guess != Secret_Word:
    user_guess = input("Guess Secret Word:")
print("Secret Word Correct")

user_pass = input("Create Password:")
user_pass1 = input("Retype Password:")
while user_pass1 != user_pass:
    user_pass1 = input("Retype Password:")
print("Password Succesfully Created!")

num = int(input("Guess The Number Between 1-10:"))
while num != 6:
    num = int(input("Guess The Number Between 1-10:"))
print("Number Is Correct!")