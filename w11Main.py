import turtle

wn=turtle.Screen()
t=turtle.Turtle()
t3=turtle.Turtle()

def keyUp() :
	t.forward(50)	

def keyDown():
	t.backward(50)

def keyRight() :
	t.right(90)

def keyLeft() :
	t.left(90)

def keyQ() :
	wn.bye()

def addKeys() :
	wn.onkey(keyUp, "Up")
	wn.onkey(keyDown, "Down")
	wn.onkey(keyRight, "Right")
	wn.onkey(keyLeft, "Left")

def mouseGoto(x, y) :
	t.setpos((x, y))
	re=isIn((x,y))
	if re :
		t.write("Bingo")

def addMouse() :
	wn.onclick(mouseGoto)
	
def addQ() :
	wn.onkey(keyQ, "q")
	wn.onkey(keyQ, "Q")

def lab11() :
	addKeys()
	addMouse()

	

def isIn(now) :
	if -20<=now[0]<=100 and 100<=now[1]<=100 :
		return True
	else :
		return False

def setposOfT(spoint, epoint) :
	t3.penup()
	t3.setpos(spoint)
	t3.pendown()
	t3.setpos(epoint)

def lab11_2() :
	setposOfT((-20, 100),(100, 100))

def main() :
	lab11()
	lab11_2()
	addQ()
	wn.listen()
	turtle.mainloop()

if __name__=="__main__" :
	main()
