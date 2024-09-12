# 1. შექმენით სია, სადაც გექნებათ 4 სტრინგი, შემდეგ კი indexing-ის მეშვეობით გამოიტანეთ მეორე ელემენტი.

my_list = ["vashli", "banani", "dinamiki", "mikautadze"]

second_element = my_list[1]

print(second_element)

# 2. შექმენით სია, სადაც გექნებათ 4 სტრინგი, შემდეგ კი შეცვალეთ მეორე ინდექსი სხვა მნიშვნელობით.

my_list = ["marshutka", "banana", "zuriko", "davitashvili"]

my_list[1] = "Kvara"

print(my_list)

# 3. შექმენით სია, სადაც გექნებათ 5 სტრინგი, შემდეგ კი slicing-ის მეშვეობით გამოიტანეთ პირველი და მეორე ელემენტი (positive indexing).

my_list = ["lochoshvili", "sanioli", "ozerbayal", "ronaldo", "airpods"]

first_and_second = my_list[0:2]

print(first_and_second)

# 4. შექმენით სია, სადაც გექნებათ 5 სტრინგი, შემდეგ კი slicing-ის მეშვეობით გამოიტანეთ პირველი და მეორე ელემენტი (negative indexing).

my_list = ["doner", "kebab", "nacho", "alejandro", "garnacho"]

first_and_second = my_list[-5:-3]

print(first_and_second)

# 5. შექმენით სია, სადაც გექნებათ 6 სტრინგი, შემდეგ კი slicing-ის მეშვეობით გამოიტანეთ პირველი და მეოთხე ელემენტი (negative indexing & positive indexing).

my_list = ["Leg", "hand", "ear", "xeli", "fexi", "yuri"]

first_element = my_list[0]
fourth_element = my_list[-3]

first_and_fourth = [my_list[0], my_list[-3]]

print(first_and_fourth)




