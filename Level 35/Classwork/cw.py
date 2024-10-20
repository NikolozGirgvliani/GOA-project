# 1. შექმენით ფუნქცია, რომელიც ითვლის სამკუთხედის პერიმეტრს (ყველა გვერდის ჯამს), სადც გექნებათ 3 არგუმენტი, სამიცე გვერდის სიგრძე.

def triangle(side1, side2, side3):
    perimeter = (side1 + side2 + side3)
    return perimeter

result = triangle(7, 6, 8)
print(result)


# Bonus:
# + ფართობის გამოთვლა.


def triangle(side1, height):
    area = (side1 * height) / 2
    return area

result = triangle(7, 4)
print(result)




