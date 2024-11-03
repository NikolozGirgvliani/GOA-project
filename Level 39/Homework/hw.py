# 1. სამი სხვადასხვა ლისტი, მაქსიმალური რიცხვი
list1 = [1, 3, 7, 10, 5]
list2 = [23, 56, 12, 8, 45]
list3 = [11, 19, 21, 7, 33]

print("Max of list1:", max(list1))
print("Max of list2:", max(list2))
print("Max of list3:", max(list3))

# 2. სამი სხვადასხვა ლისტი, მინიმალური რიცხვი
print("Min of list1:", min(list1))
print("Min of list2:", min(list2))
print("Min of list3:", min(list3))

# 3. სამი სხვადასხვა ლისტი, სიგრძე
list4 = [10, 20, 30, 40, 50]
list5 = [100, 200, 300, 400, 500]
list6 = [5, 15, 25, 35, 45]

print("Length of list4:", len(list4))
print("Length of list5:", len(list5))
print("Length of list6:", len(list6))

# 4. სამი სხვადასხვა ლისტი, რიცხვების ჯამი
print("Sum of list1:", sum(list1))
print("Sum of list2:", sum(list2))
print("Sum of list3:", sum(list3))

# 5. ოთხი სხვადასხვა ლისტი, შესაბამისი დავალების შესრულება
list7 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list8 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list9 = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
list10 = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]

# 1) პირველ list-ის პირველიდან მეოთხე ელემენტამდე ცვლადები
print("list7 elements from 1st to 4th:", list7[0:4])

# 2) მეორე list-ის მეოთხედან მერვე ელემენტამდე ცვლადები for ციკლით
print("list8 elements from 4th to 8th:")
for i in range(3, 8):
    print(list8[i])

# 3) მესამე list-ის მეცხრედან მეექვსე ელემენტამდე უარყოფითი ინდექსებით
print("list9 elements from 9th to 6th (reverse):", list9[8:5:-1])

# 4) მეოთხე list-ში ყველა ცვლადი while ციკლის გამოყენებით
print("All elements of list10:")
i = 0
while i < len(list10):
    print(list10[i])
    i += 1

# 6. ფუნქცია, რომელიც დაპრინტავს list-ის მაქსიმალურ, მინიმალურ რიცხვს, ჯამს და სიგრძეს
def analyze_list(lst):
    print("Max:", max(lst))
    print("Min:", min(lst))
    print("Sum:", sum(lst))
    print("Length:", len(lst))

user_list = [10, 23, 45, 5, 9]
analyze_list(user_list)
