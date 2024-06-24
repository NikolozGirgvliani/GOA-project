from turtle import *

#we want to paint a house

#step 1: draw a square
speed(7)
width(7)
color("blue")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of a square

#step 2: draw a door

forward(70)
color("purple")
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
#end of a door

#step 3: draw a roof
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#end of a roof



exitonclick()