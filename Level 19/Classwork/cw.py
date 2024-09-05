# 1. ცვლადში შეინახეთ რიცხვი, თუ ეს რიცხვი ნაკლები იქნება 18-ზე, დაპრინტეთ (underage), თუ იქნება 18-ის ტოლი, დაპრინტეთ (teen), თუ იქნება 18-ზე მეტი (adult).

num = int(input("Age: "))

if num < 18:
    print("Underage")
elif num == 18:
    print("Teen")
else:
    print("Adult")

# 2. მომხარებელს ცვლადში შემოატანინე რიცხვი, თუ ის რიცხვი უარყოფითია დაუპრინტე (negative), თუ დადებითია (positive), თუ ნულია (zero).

user_input = int(input("Enter Random Number: "))

if user_input > 0:
    print("Positive")
elif user_input == 0:
    print("Zero")
else:
    print("Negative")