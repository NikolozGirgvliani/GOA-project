import random
secret = random.randint(1, 40)
guess = 0

while guess != secret:
    guess = int(input("Guess Number (From 1 to 140): "))
    
    if guess < secret:
        print("Higher!")
    elif guess > secret:
        print("Lower!")
    else:
        print("Congrats, You Got Number Right!")
