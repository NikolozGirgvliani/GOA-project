# 1. Write an if-else statement that prints "Good morning!" if the current hour is before 12, and "Good afternoon!" if it is 12 or later.

current_hour = 7

if current_hour < 12:
    print("Good morning!")
else:
    print("Good afternoon!")

# 2. Create an if-else statement to check if the temperature exceeds 30 degrees. If it does, print "It's hot outside!"; otherwise, print "It's not too hot."

temperature = 37

if current_hour < 30:
    print("It's hot outside!")
else:
    print("It's not too hot.")

# 3. Create an if-else statement to determine if a person is a teenager. If the age is less than 19 print "You are a teenager!"; otherwise, print "You are not a teenager."

user_age = input("Your Age: ")
if user_age > 19:
    print("You are not a teenager.")
else: 
    print("You are a teenager!")
