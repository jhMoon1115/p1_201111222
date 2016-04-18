import turtle
import random
import time

def drawSquare(turtle, point, size) :
	turtle.penup()
	turtle.setpos(point)
	turtle.setheading(90)
	turtle.pendown()
	for i in range(4) :
		turtle.fd(size)
		turtle.right(90)

def setGoal(turtle) :
	turtle.pencolor("Black")
	turtle.color("Black")
	turtle.clear()
	rangeX=turtle.window_width()/2-110
	rangeY=turtle.window_height()/2-110
	pos=(random.uniform(-rangeX, rangeX), random.uniform(-rangeY, rangeY))
	drawSquare(turtle, pos, 100)
	turtle.pencolor("WHITE")
	turtle.color("WHITE")
	return pos

def reset(goal, turtle, info) : 
	turtle.reset()
	turtle.clear()
	goal.reset()
	goal.clear()
	while True :
		goalPos=setGoal(goal)
		pos=turtle.pos()
		if(goalPos[0]<=pos[0]<=goalPos[0]+100 and goalPos[1]<=pos[1]<=goalPos[1]+100) :
			continue
		else :
			info["goalPos"]=goalPos
			info["tracks"]=[turtle.pos()]
			break
	
def onKey(screen, goal, turtle, info) :
	def up() :
		if(len(info["tracks"])==1) :
			turtle.clear()
		turtle.fd(100)
		pos=turtle.pos()
		info["tracks"].append(pos)
		if(info["goalPos"][0]<=pos[0]<=info["goalPos"][0]+100 and info["goalPos"][1]<=pos[1]<=info["goalPos"][1]+100) :
			info["point"]+=1
			turtle.write("Done. Your point is "+str(info["point"]))
			time.sleep(2)
			reset(goal, turtle, info)
		
	def down() :
		if len(info["tracks"])<=1 :
			turtle.write("no more")
		else :
			info["tracks"].pop()
			pos=info["tracks"][len(info["tracks"])-1]
			turtle.pencolor("WHITE")
			turtle.setpos(pos)
			turtle.pencolor("BLACK")

	def right() :
		turtle.right(90)
	
	def left() :
		turtle.left(90)

	screen.onkey(up, "Up")
	screen.onkey(down, "Down")
	screen.onkey(right, "Right")
	screen.onkey(left, "Left")
	screen.listen()

def lab() :
	wn=turtle.Screen()
	goal=turtle.Turtle()
	t=turtle.Turtle()
	info=({"point" : 0, "tracks" : [], "goalPos" : (0,0)})
	goal.speed(10)
	reset(goal, t, info)
	onKey(wn, goal, t, info)
	wn.exitonclick()

def main() :
	lab()

if(__name__=="__main__") :
	main()
