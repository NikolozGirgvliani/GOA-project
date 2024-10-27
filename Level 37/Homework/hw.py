# 1. შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვს და აბრუნებს მის კვადრატს.

def square_of_num(num):
    square = num ** 2
    print(square)
    return square

square_of_num(5)


# 2. შექმენით ფუნქცია, რომელიც არგუმენტად იღებს ორ რიცხვს და აბრუნებს მათ ჯამს.

def sum_of_two(num1, num2):
    sum = num1 + num2
    print(sum)
    return sum

sum_of_two(5, 2)

# 3. შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვთა სიას და აბრუნებს ყველაზე პატარას.

def find_smallest(numbers):
    return min(numbers)

numbers = [1,2,3,4,5]
smallest = find_smallest(numbers)

print(smallest)

# 4. შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვს და ამოწმებს, არის თუ არა ის დადებითი.

def positive(num):
    if num > 0:
        print("This Number Is Positive")
    elif num < 0:
        print("This Number Is Negative")
    else:
        print("This Number Is Zero")

positive(7)

# 5. შექმენით ფუნქცია, რომელიც არგუმენტად იღებს რიცხვთა სიას და აბრუნებს მათ ჯამს.

def sum_of_list(list):
    return sum(list)

list = [5, 10, 15, 20, 25]
total_sum = sum_of_list(list)

print(total_sum)
