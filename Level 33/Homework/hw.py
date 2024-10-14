# 1. შექმენით ფუნქცია, სადაც არგუმენტად გადასცემთ ორ string-ს, შემდეგ შეაერთეთ ისინი და დაპრინტეთ.

def together(str1, str2):
    print(str1 + str2)
together("Me", "ssi")

# 2. შექმენით ფუნქცია, სადაც არგუმენტად გადასცემთ 5 ელემენტიან რიცხვების სიას, შემდეგ დაპრინტეთ სიის მე-3 ელემენტისა და მე-4 ელემენტის ჯამი.

def sum_of_nums(list):
    result = list[2] + list[3]
    print("sum of 3rd and 4th numbers in the list:", result)

list = [11, 22, 33, 44, 55]

sum_of_nums(list)

# 3. შექმენით ფუნქცია, სადაც არგუმენტად გადასცემთ მანძილს კილომეტრში, შემდეგ გადააქციეთ ის მეტრში და დაპრინტეთ.

def km_to_meters(km):
    meters = km * 1000
    return meters

km_value = 20
result = km_to_meters(km_value)
print(result)

# 4. შექმენით ფუნქცია, სადაც არგუმენტად გადასცემთ ორ რიცხვს, შემდეგ დაპრინეთ ამ ორი რიცხვიდან უფრო დიდი.

def higher_num(num1, num2):
    higher = max(num1, num2)
    print(higher)
higher_num(4, 8)

# 5. შექმენით ფუნქცია, სადაც არგუმენტად გადასცემთ სტრინგს, შემდეგ შეაბრუნეთ ეს სტრინგი და დაპრინტეთ. 

def reverse_str(str):
    reverse_str = str[::-1]
    print(reverse_str)
reverse_str("sigma")

