# 1. კომენტარების მეშვეობით ახსენი რა არის .upper().

# .upper() სიტყვა/წინადადებას აქცევს მაღალ ასოებად მაგალითად  goa --> GOA

# 2. კომენტარების მეშვეობით ახსენი რა არის .lower()

# .lower() სიტყვა/წინადადებას აქცევს დაბალ ასოებად მაგალითად  GOA --> goa

# 3. ცვლადში შეინახე სტრინგი დიდი ასოებით, შემდეგ .capitalize() ფუნქციის მეშვეობით 
# გადააქციე პირველი ასო დიდ ასოდ, დააკვირდი რა მოუვათ სხვა ასოებს.

str = 'GIRGONA'
print(str.capitalize())
# სხვა ასოები დაბალ ასოებად იქცევიან

# 4. მომხარებელს შემოატანინე სახელი და გვარი ცალ ცალკე, შემდეგ გადააქციე პატარა 
# ასოებად სახელი დაუმატე გვარი ჩვეულებრივად და დაპრინტე.

name = input('Enter Your Name: ')
surname = input('Enter Your surname: ')

print(name.lower() + ' ' + surname.lower())

# 5. შექმენი ცვლადი name='goalorienteacademy', შემდეგ .find() ფუნქციის მეშვეობით იპოვე ამ სტრინგში:

#   1. 'o'
#   2. 'a'
#   3. 'y'
#   4. 'x'.

sigma ='goalorienteacademy'
index = sigma.find('o')
print(index)
index2 = sigma.find('a')
print(index2)
index3 = sigma.find('y')
print(index3)
index4 = sigma.find('x')
print(index4)