# მომხმარებელს შემოატანინეთ 2 რიცხვი და ოპერატორი ანუ მაგ:
# პირველი რიცხვი - 10
# მეორე რიცხვი- 15
# ოპერატორი - +
# და შეასრულეთ მოქმედება კალკულატორის სტილში 
# მომხმარებელს უნდა შეეძლოს +,-,/,* შემოტანა ასევე გაითვალისწინეთ რომ 0ზე გაყოფა არ შეიძლება

num1 = float(input("First Number: "))
num2 = float(input("Second Number: "))
operator = input("Operator (+, -, *, /): ")

if operator == "+":
    print(f"Result: {num1} + {num2} = {num1 + num2}")
elif operator == "-":
    print(f"Result: {num1} - {num2} = {num1 - num2}")
elif operator == "*":
    print(f"Result: {num1} * {num2} = {num1 * num2}")
elif operator == "/":
    if num2 == 0:
        print("You cant use 0.")
    else:
        print(f"Result: {num1} / {num2} = {num1 / num2}")
else:
    print("Incorrect Operator!")

