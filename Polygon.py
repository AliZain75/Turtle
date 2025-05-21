import turtle
turtle.Screen().bgcolor("green")
turtle.Screen().setup(500,700)
polygon=turtle.Turtle()
sides=6
side_lenth=70
angle=360.0 / sides
for i in range(sides) :
 polygon.forward(side_lenth)
 polygon.right(angle)
turtle.done 