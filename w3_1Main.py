import turtle
wn=turtle.Screen()
t=turtle.Turtle()


def drawSquareOrTriangle(size, sides, angle) :
	t.setheading(0)
	for i in range(sides) :
		t.left(angle)
		t.fd(size)


sel=raw_input("Triangle or Square : ")


if(sel=='S'):
	sides=4
	angle=90
else :
	sides=3
	angle=120

drawSquareOrTriangle(100, sides, angle)

wn.exitonclick()