# მოცემული გაქვთ სია:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# თქვენი დავალებაა ამ სიიდან დაპრინტოთ მხოლოდ გაორმაგებული ლუწი რიცხვები,
# მაგალითად: 4, 8, 12...

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in numbers:
    if i % 2 == 0:
        print(i * 2)


# მოცემული გაქვთ სია:
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# თქვენი დავალებაა ამ სიის ლუწი რიცხვების ჯამს გამოაკლეთ ამ სიის კენტი რიცხვების ჯამი და დაპრინოთ შედეგი.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_sum = 0
odd_sum = 0

for i in numbers:
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

result = even_sum - odd_sum
print(result)
