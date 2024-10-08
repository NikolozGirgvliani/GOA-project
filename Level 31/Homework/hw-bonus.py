# 6. შექმენი ფუნქცია, რომელსაც არგუმენტად გადასცემ რიცხვს (სტრინგად), შემდეგ ფუნქციაში გადაქციე ეს სტრინგი ინტეჯერად,
#  და დაპრინტე მასზე 5-ჯერ მეტი რიცხვი.

def multiply_by_five(numstr):
    number = int(numstr)
    result = number * 5
    print(f"რიცხვი {number}-ზე 5-ჯერ მეტი არის: {result}")

# ფუნქციის გამოძახება
numstr = "7"
multiply_by_five(numstr)


# 7. შექმენი ფუნქცია, რომელსაც არგუმენტად გადასცემ სამ რიცხვს, შემდეგ დაპრინტე ამ სამი რიცხვის ნამრავლი, განაყოფი, სხვაობა, ჯამი.

def calculate_operations(a, b, c):
    product = a * b * c
    division = a / b / c
    difference = a - b - c
    summation = a + b + c

    print(f"ნამრავლი: {product}")
    print(f"განაყოფი: {division}")
    print(f"სხვაობა: {difference}")
    print(f"ჯამი: {summation}")

# ფუნქციის გამოძახება
a = float(input("enter 1st number: "))
b = float(input("enter 2nd number: "))
c = float(input("enter 3rd number: "))
calculate_operations(a, b, c)


# 8. შექმენი ფუნქცია, რომელსაც არგუმენტად გადასცემ 5 ელემენტიან სიას, შემდეგ დაპრინტე ამ სიის მე-3 ინდექსზე მყოფი ელემენტი.

def print_third_element(my_list):
    print(f"სიის მე-3 ინდექსზე მყოფი ელემენტი არის: {my_list[3]}")

# ფუნქციის გამოძახება
my_list = [1, 2, 3, 4, 5]  # 5 ელემენტიანი სია
print_third_element(my_list)


# 9. შექმენი ფუნცია, რომელსაც პირველ არგუმენტად გადასცემ 5 ელემენტიან სიას, ხოლო მეორე არგუმენტად გადასცემ რაიმე რიცხვს
# , შემდეგ დაპრინტე ამ სიიდან ის ინდექსი, რომელი რიცხვიც მეორე არგუმენტად გადაეცი.

def find_index_of_number(my_list, number):
    if number in my_list:
        index = my_list.index(number)
        print(f"რიცხვი {number} სიის {index}-ე ინდექსზეა.")
    else:
        print(f"რიცხვი {number} სიაში არ არის.")

# ფუნქციის გამოძახება
my_list = [10, 20, 30, 40, 50]  # 5 ელემენტიანი სია
number = int(input("შეიყვანეთ რიცხვი: "))
find_index_of_number(my_list, number)


# 10. შექმენი ფუნქცია, რომელსაც არგუმენტად გადასცემ რიცხვს, შემდეგ დაპრინტე 0-იდან ამ რიცხვამდე ყველა რიცხვი, გამოიყენე for loop().

def print_numbers_up_to(n):
    for i in range(n + 1):
        print(i)

# ფუნქციის გამოძახება
n = int(input("შეიყვანეთ რიცხვი: "))
print_numbers_up_to(n)

