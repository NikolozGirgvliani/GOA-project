# 1. ფუნქცია, რომელიც იღებს რიცხვების ჩამონათვალს და აბრუნებს ახალ სიას, სადაც თითოეული რიცხვი მრავლდება 2-ზე, for loop და .append()-ის გამოყენებით.
def multiply_by_two(numbers):
    result = []
    for number in numbers:
        result.append(number * 2)
    return result

print(multiply_by_two([1, 2, 3, 4]))


# 2. პროგრამა, სადაც მომხმარებელს შეატანინებთ რიცხვს 5-ჯერ, დაამატებთ მათ სიაში და დაბეჭდავთ შებრუნებულ სიას.
numbers = []
print("Input 5 Numbers:")
for i in range(5):
    num = int(input(f"{i + 1}: "))
    numbers.append(num)

print("Reversed List:", list(reversed(numbers)))


# 3. ფუნქცია, რომელიც მიიღებს სიტყვების ჩამონათვალს და დააბრუნებს მათი სიგრძის სიას.
def word_lengths(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths

print(word_lengths(["apple", "banana", "kiwi"]))

# 4. ფუნქცია, რომელიც მიიღებს სტრინგების სიას და დააბრუნებს ახალ სიას, რომელიც შეიცავს მხოლოდ 3 სიმბოლოზე მეტ სტრინგებს.
def filter_long_strings(strings):
    result = []
    for string in strings:
        if len(string) > 3:
            result.append(string)
    return result

print(filter_long_strings(["cat", "tree", "hi", "world", "go"]))
