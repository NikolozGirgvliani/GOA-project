# შექმენით 4 ლისტი და დაპრინტეთ მათში შეყვანილი ცვლადების რაოდენობა

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c', 'd']
list3 = [True, False]
list4 = [10.5, 20.3, 30.8, 40.2, 50.1]

print(len(list1))
print(len(list2))  
print(len(list3)) 
print(len(list4))

# შექმენთ 2 ლისტი და თითოეულს append ფუნქციის გამოყენებით დაუმატეთ 3-3 ცვლადი

list1 = []
list2 = []

list1.append(10)
list1.append(20)
list1.append(30)

list2.append('x')
list2.append('y')
list2.append('z')

print(list1)  
print(list2)  

# შექმენით 2 ლისტი. პირველს მე5ე და მე2ე ადგილას დაუმატეთ ცვლადები ხოლო მეორეს მე3ე და მე4ე ადგილას

list1 = [10, 20, 30, 40]
list2 = ['a', 'b', 'c', 'd', 'e']

list1.insert(4, 100) 
list1.insert(1, 50)   

list2.insert(2, 'x')  
list2.insert(3, 'y')  

print(list1)  
print(list2) 

# შექმენით 2 ლისტი და ორივედან ამოშალეთ 2-2 ცვლადი pop ფუნქციის გამოყენებით

list1 = [10, 20, 30, 40]
list2 = ['a', 'b', 'c', 'd']

list1.pop()
list1.pop(1) 

list2.pop()  
list2.pop(2) 

print(list1) 
print(list2) 

list1 = []

# შექმენით 1 ლისტი და გამოიყენეთ ყველა ფუნქცია რაც დღეს გავიარეთ

list1.append(10)
list1.append(20)
list1.append(30)

list1.insert(1, 50)

list1.pop(2)

print(len(list1))  

print(list1)  

var1 = "hello"
var2 = "Python"
var3 = "openai"

# შექმენით 3 ცვლადი და დაითვალეთ რამდენი სიმბოლოა თითოეულ ცვლადში

print(len(var1))  
print(len(var2))  
print(len(var3))  

var1 = "hello"
var2 = "Python"
var3 = "openai"

print(len(var1)) 
print(len(var2)) 
print(len(var3))  









