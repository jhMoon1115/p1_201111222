import turtle
wn=turtle.Screen()
t=turtle.Turtle()


def drawSwirlSquare(size, bigger, sides, angle) :
	for i in range(sides) :
		if(i!=0 and i%2==0) :
		#if(i%2) :
			size+=bigger
		t.fd(size)
		t.right(angle)



sides=10
bigger=10
angle=90
size=10

drawSwirlSquare(size, bigger, sides, angle)

wn.exitonclick()