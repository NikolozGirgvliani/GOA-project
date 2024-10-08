# 1)შექმენით 4 ლისტი და დაპრინტეთ მათში შეყვანილი ცვლადების რაოდენობა

list1 = [1, 2, 3, 4]
list2 = ['apple', 'banana', 'cherry']
list3 = [True, False]
list4 = ['car', 'bike', 'bus', 'train', 'airplane']


print(len(list1)) 
print(len(list2))  
print(len(list3)) 
print(len(list4))  


# 2)შექმენთ 3 ლისტი და თითოეულს append ფუნქციის გამოყენებით დაუმატეთ 2-2 ცვლადი


list1 = []
list2 = []
list3 = []

list1.append(5)
list1.append(10)

list2.append('cat')
list2.append('dog')

list3.append(3.14)
list3.append(2.71)


print(list1) 
print(list2) 
print(list3)


# 3)შექმენით 2 ლისტი. პირველს მე3ე და მე0ე ადგილას დაუმატეთ ცვლადები ხოლო მეორეს მე4ე და მე2ე ადგილას

list1 = [10, 20, 30]
list2 = ['a', 'b', 'c', 'd', 'e']

list1.insert(3, 100)
list1.insert(0, 0)   

list2.insert(4, 'x')
list2.insert(2, 'y') 

print(list1)
print(list2)


# 4)შექმენით 1 ლისტი და ორივედან ამოშალეთ 2 ცვლადი pop ფუნქციის გამოყენებით

list1 = [1, 2, 3, 4, 5]

list1.pop() 
list1.pop(1)  

print(list1)  

# 5)შექმენით 3 ცვლადი და დაითვალეთ რამდენი სიმბოლოა თითოეულ ცვლადში

var1 = "Sololearn"
var2 = "Python"
var3 = "Programming"

print(len(var1))  # Output: 9
print(len(var2))  # Output: 6
print(len(var3))  # Output: 11


# 6)კომენტარების გამოყენებით ახსენით რას აკეთებს თითოეული ფუნქცია

print(len([1, 2, 3]))  # Output: 3

list1 = [1, 2]
list1.append(3)
print(list1)  # Output: [1, 2, 3]

list1 = [1, 2, 4]
list1.insert(2, 3)  # პოზიცია 2-ზე 3-ის დამატება
print(list1)  # Output: [1, 2, 3, 4]

list1 = [1, 2, 3, 4]
list1.pop()    # ბოლოს ელემენტის ამოშლა
list1.pop(1)   # მეორე (პოზიცია 1) ელემენტის ამოშლა
print(list1)  # Output: [1, 3]

