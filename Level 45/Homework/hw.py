# 1. Print "Hello World"
print("Hello World")

# 2. Two int variables and their sum
a = 5
b = 10
print("Sum:", a + b)

# 3. Two str variables and concatenation
str1 = "Hello"
str2 = "World"
print("Concatenated string:", str1 + " " + str2)  # Concatenation means joining two strings.

# 4. Two int variables and their division
num1 = 10
num2 = 4
print("Division result:", num1 / num2)  # Result is float because division in Python returns float (implicit conversion).

# 5. Comparison operators examples
print("5 > 3:", 5 > 3)
print("5 < 3:", 5 < 3)
print("5 == 5:", 5 == 5)
print("5 != 3:", 5 != 3)
print("5 >= 5:", 5 >= 5)
print("5 <= 3:", 5 <= 3)

# 6. Combine comparison and mathematical operations
print("5 + 5 == 8 + 2:", 5 + 5 == 8 + 2)

# 7. Logical operators examples
print("True and False:", True and False)
print("True or False:", True or False)
print("not True:", not True)

# 8. Combining logical and comparison operators
print("(5 > 3) and (2 < 4):", (5 > 3) and (2 < 4))
print("(5 < 3) or (2 == 2):", (5 < 3) or (2 == 2))
print("not (5 == 5):", not (5 == 5))
print("(10 > 5) and (5 != 4):", (10 > 5) and (5 != 4))
print("(3 + 2 == 5) or (7 - 3 != 4):", (3 + 2 == 5) or (7 - 3 != 4))

# 9. For loop to print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# 10. For loop to print each character in the string "Hello, World!"
for char in "Hello, World!":
    print(char)

# 11. While loop to print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1

# 12. While loop to sum numbers from 1 until the total equals 50
total = 0
num = 1
while total < 50:
    total += num
    num += 1
print("Sum reached 50:", total)

# 13. Function to calculate the average of a list of numbers
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

test_case = [1, 3, 4, 5, 2]
print("Average:", calculate_average(test_case))

# 14. Function to return a new list with squares of each number
def square_numbers(numbers):
    squares = []
    for num in numbers:
        squares.append(num ** 2)
    return squares

test_case = [3, 12, 5, 2, 6]
print("Squares:", square_numbers(test_case))

# 15. Examples of list and string methods
# List methods
my_list = [1, 2, 3, 4]
my_list.append(5)  # Add an item
print("List after append:", my_list)
my_list.remove(3)  # Remove an item
print("List after remove:", my_list)
my_list.reverse()  # Reverse the list
print("Reversed list:", my_list)

# String methods
my_string = "Hello, World!"
print("Uppercase:", my_string.upper())  # Convert to uppercase
print("Lowercase:", my_string.lower())  # Convert to lowercase
print("Find 'World':", my_string.find("World"))  # Find substring
print("Replace 'World' with 'Python':", my_string.replace("World", "Python"))  # Replace substring
