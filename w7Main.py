import turtle
wn=turtle.Screen()
t=turtle.Turtle()
def drawSquareAtSave(pos, size) :
	"""
	draw square at pos and save square's tracks function

	parameter
	--------
	arg1 tuple
		pos
	arg2 int
		size
	
	return
	------
	tracks list
	"""
	tracks=list()
	t.penup()
	t.setpos(pos)
	t.setheading(90)
	t.pendown()
	for i in range(0, 4) :
		tracks.append(t.pos())
		t.fd(size)
		t.right(90)
	return tracks


def lab7() :
	"""
	0418
	"""
	tracks=drawSquareAtSave((100, 100), 100)
	print "Tracks of Square : ",
	print tracks
	wn.exitonclick()

def main() :
	lab7()

if(__name__=="__main__") :
	main()
