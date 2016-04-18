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


def lab7_2() :
	"""
	0418
	"""
	tracks=drawSquareAtSave((100, 100), 100)
	print "Tracks of Square : ",
	print tracks

def drawSquareFrom(tracks) :
	"""
	draw square from tracks function
	
	parameter
	---------
	arg1 list
		tracks
	return
	------
	none
	"""
	for i in range(0, len(tracks)) :
		if(i==0) :
			t.penup()
			t.setpos(tracks[i])
			t.pendown()
		else :
			t.setpos(tracks[i])
	t.setpos(tracks[0])

def lab7_3() :
	tracks=[(0, 0), (100, 0), (100, -150), (0, -150)]
	print "\ndraw square from tracks - ",
	print tracks
	drawSquareFrom(tracks)

def main() :
	lab7_2()
	lab7_3()
	wn.exitonclick()

if(__name__=="__main__") :
	main()
