name = "nika"
#name არის ცვლადი
# = არის ცვლადისთვის მნიშვნელობის მიმნიჭებელი სიმბოლო
# "nika" არის ცვლადისთვის მნიშვნელობა

surname = "girgvliani"

# print(name)
# პრინტ ფუნქციას გადაეცემა ეკრანზე გამოსატანი ობიექტი

name = "nika" #ეს არის str (string) ტიპის ცვლადი
age = 14 #ეს არის int (integer) მთელი რიცხვი
height = 170.5 #ეს არის float ტიპის ცვლადი (ათწილადი)
#boolean (booL) ტიპის ცვლადი

knows_programming = True #True ან False
is_ugly = False #snakecase  (უბრალოდ წერის სტილი სტანდარტულად)

IsUgly = False #ჯავასკრიპტული camelcase

# print(name + " " + surname)

# print(name + age) int + str არ ხდება

print(type(age))
print(type(name))
print(type(surname))
print(type(height))
print(type(knows_programming))



print(name + " " + str(age))

print("მე ვარ " + name + " " + str(surname) + " ვარ " + str(age) + " და ვარ " + str(height) + " სანტიმეტრი")