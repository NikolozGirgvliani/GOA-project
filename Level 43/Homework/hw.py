# 1. შექმენით სია, 5 რიცხვით, შემდეგ დაპრინტეთ ამ სიაში შემავალი რიცხვების ჯამი.

numbers = [3, 7, 2, 10, 5]
print("Sum:", sum(numbers))

# 2. შექმენით სია, 5 რიცხვით, შემდეგ დაპრინტეთ ამ სიაში შემავალი რიცხვებიდან უდიდესი.

numbers = [3, 7, 2, 10, 5]
print("Biggest Number:", max(numbers))

# 3. შექმენით სია, 5 რიცხვით, შემდეგ დაპრინტეთ ამ სიაში შემავალი რიცხვებიდან უმცირესი.

numbers = [3, 7, 2, 10, 5]
print("Smallest Number:", min(numbers))

# 4. შექმენით სია, 5 რიცხვით, შემდეგ დაპრინტეთ ამ სიის სიგრძე.

numbers = [3, 7, 2, 10, 5]
print("List Lenght:", len(numbers))

# 5. შექმენით სია, 5 სტრინგით, შემდეგ .append()-ის მეშვეობით სიის ბოლოში დაამატეთ სასურველი სიტყვა.

words = ["apple", "banana", "cherry", "date", "fig"]
words.append("grape")
print("New List:", words)

# 6. შექმენით სია, 5 სტრინგით, შემდეგ .insert()-ის მეშვეობით სიაში სასურველ ინდექსზე დაამატეთ სასურველი სიტყვა.

words = ["apple", "banana", "cherry", "date", "fig"]
words.insert(2, "kiwi") 
print("New List:", words)

# 7. შექმენით სია, 5 სტრინგით, შემდეგ .pop()-ის მეშვეობით სიიან ამოაგდეთ ინდექსის მეშვეობით რომელიმე სიტყვა.

words = ["apple", "banana", "cherry", "date", "fig"]
removed_word = words.pop(1)
print("Removed Word:", removed_word)
print("New List:", words)


