# * შექმენი ფუნქცია სახელად max_of_two, რომელიც არგუმენტად იღებს ორ რიცხვს. 
# * ფუნქციამ უნდა დააბრუნოს და დაპრინტოს ამ ორი რიცხვიდან უფრო დიდი. 

def max_of_two(num1, num2):
    larger = max(num1, num2)
    print(larger)
    return larger

max_of_two(5, 7)
