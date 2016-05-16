import turtle
import math

wn=turtle.Screen()
t=turtle.Turtle()
t2=turtle.Turtle()

coord=[(-100, -100), (-200, -200)]
line=[(50, 100), (150, 100)]
scircle=(-80, -10)
radius=100
circleCenter=(scircle[0], scircle[1]+radius) 

wn.bgpic("maze.gif")

def isInRectangle(curpos, coord) :
	xs=coord[0][0]
	xe=coord[1][0]
	ys=coord[0][1]
	ye=coord[1][1]
	tmp=0
	if coord[0][0]>coord[1][0] :
		tmp=xs
		xs=xe
		xe=tmp
	if coord[0][1]>coord[1][1] :
		tmp=ys
		ys=ye
		ye=tmp
	return xs<=curpos[0]<=xe and ys<=curpos[1]<=ye

def isOnLine(curpos, spos, epos) :
	xs=spos[0]
	xe=epos[0]
	ys=spos[1]
	ye=epos[1]
	tmp=0
	if spos[0]>epos[0] :
		tmp=xs
		xs=xe
		xe=tmp
	if spos[1]>epos[1] :
		tmp=ys
		ys=ye
		ye=tmp
	return xs-1<=curpos[0]<=xe+1 and ys-1<=curpos[1]<=ye+1

def isInCircle(curpos, radius, pos) :
	return math.sqrt(math.pow(curpos[0]-pos[0], 2)+math.pow(curpos[1]-pos[1], 2))<=radius
	
		
def keyup() :
	t.forward(50)
	if isInRectangle(t.pos(), coord) :
		t.write("Rec Bingo")
	if isOnLine(t.pos(), line[0], line[1]) :
		t.write("Line Bingo")
	if isInCircle(t.pos(), radius, circleCenter) :
		t.write("Cir Bingo")
def keydown() :
	t.back(50)
	if isInRectangle(t.pos(), coord) :
		t.write("Rec Bingo")
	if isOnLine(t.pos(), line[0], line[1]) :
		t.write("Line Bingo")
	if isInCircle(t.pos(), radius, circleCenter) :
		t.write("Cir Bingo")

def keyright() :
	t.right(90)
def keyleft() :
	t.left(90)

def addkeys() :
	wn.onkey(keyup, "Up")
	wn.onkey(keydown, "Down")
	wn.onkey(keyright, "Right")
	wn.onkey(keyleft, "Left")
	
def mousegoto(x, y) :
	t.setpos(x, y)
	if isInRectangle((x, y), coord) :
		t.write("Rec Bingo")
	if isOnLine(t.pos(), line[0], line[1]) :
		t.write("Line Bingo")
	if isInCircle(t.pos(), radius, circleCenter) :
		t.write("Cir Bingo")

def addmouses() :
	wn.onclick(mousegoto)

def lab11_3() :
	t.speed(1)
	t.shape("turtle")
	t.goto(380, -200)
	t.clear()
	t.setheading(180)
	addkeys()
	addmouses()


def drawSquareWithCoord(coord):
        x1=coord[0][0]
        x2=coord[1][0]
        y1=coord[0][1]
        y2=coord[1][1]
        t2.penup()
        t2.setpos((x1,y1))
        t2.pendown()
        t2.setpos((x2,y1))
        t2.setpos((x2,y2))
        t2.setpos((x1,y2))
        t2.setpos((x1,y1))

def lab11_4() :
	t2.color("Red")
	drawSquareWithCoord(coord)

def drawLine(spos, epos) :
	t2.penup()
	t2.setpos(spos)
	t2.pendown()
	t2.setpos(epos)

def lab11_5() :
	drawLine(line[0], line[1])

def drawCircle(pos, radius) :
	t2.penup()
	t2.setpos(pos)
	t2.pendown()
	t2.setheading(0)
	t2.circle(radius)

def lab11_6() :
	drawCircle(scircle, radius)
	
def main() :
	wn.listen()
	lab11_3()
	lab11_4()
	lab11_5()
	lab11_6()
	turtle.mainloop()
	

if __name__=="__main__" :
	main()