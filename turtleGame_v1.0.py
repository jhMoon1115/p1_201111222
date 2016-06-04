import turtle
import random
import time

class Rank(object) :
	def __init__(self, name, time) :
		self.name=name
		self.time=time
	def getName(self) :
		return self.name
	def getTime(self) :
		return self.time
	def setName(self, name) :
		self.name=name
	def setTime(self, time) :
		self.time=time

class Ranking(object) :
	def __init__(self, toNum) :
		self.ranking=list()
		self.toNum=toNum
	def addRankAndSort(self, rank) :
		length=len(self.ranking)
		i=0
		isChange=False
		end=self.toNum
		if length==0 :
			self.ranking.append(rank)
			return
		if length<self.toNum : 
			end=length
		for index in range(0, end) :
			if self.ranking[index].getTime()>rank.getTime() :
				while True :
					if i==0 and length<self.toNum :
						self.ranking.append(self.ranking[length-1])
						i+=1
					else :
						if i==0 :
							i+=1
							continue
						else :
							self.ranking[length-i]=self.ranking[length-i-1]
							i+=1
					if i+index==length :
						break
				self.ranking[index]=rank
				isChange=True
				break
		if not isChange :
			if length<self.toNum :
				self.ranking.append(rank)
	def addRank(self, rank) :
		self.ranking.append(rank)	
	def getRanking(self) :
		return self.ranking

def readFile(fileName, toNum) :
	ranking=Ranking(toNum)
	try :
		f=open(fileName, 'r')
	except IOError as e :
		print e
	else :
		for line in f.readlines() :
			tmp=line.split()
			tmpRank=Rank(tmp[0], int(tmp[1]))
			ranking.addRank(tmpRank)
		f.close()
	return ranking

def writeFile(fileName, ranking) :
	try : 
		f=open(fileName, 'w')
	except IOError as e :
		print e
	else :
		for rank in ranking.getRanking() :
			f.write("{0} {1}\n".format(rank.getName(), rank.getTime()))
		f.close()

def printRank(ranking) :
	lrank=ranking.getRanking()
	before=1
	for i in range(0, len(lrank)): 
		if i==0 :
			print "{0}\t{1}\t{2}".format(i+1, lrank[i].getName(), lrank[i].getTime())
		else : 
			if lrank[i].getTime()==lrank[i-1].getTime() :
				print "{0}\t{1}\t{2}".format(before, lrank[i].getName(), lrank[i].getTime())
			else :
				print "{0}\t{1}\t{2}".format(i+1, lrank[i].getName(), lrank[i].getTime())
				before=i+1

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
	
def onKey(screen, goal, turtle, info, ranking) :
	def up() :
		if(len(info["tracks"])==1) :
			turtle.clear()
		turtle.fd(100)
		pos=turtle.pos()
		info["tracks"].append(pos)
		if(info["goalPos"][0]<=pos[0]<=info["goalPos"][0]+100 and info["goalPos"][1]<=pos[1]<=info["goalPos"][1]+100) :
			info["point"]+=1
			turtle.write("Done. Your point is "+str(info["point"]))
			if info["point"]==10 :
				info["eTime"]=time.mktime(time.localtime())
				ptime=int(info["eTime"]-info["sTime"])
				ranking.addRankAndSort(Rank(info["name"], ptime))
				writeFile('ranking.txt', ranking)
				turtle.clear()
				turtle.write("Game Clear.Your play time is {0}.\nCheck your rank in cmd".format(ptime))
				printRank(ranking)
			else : 
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
	name=raw_input("enter your name : ")
	info=({"name" : name, "point" : 0, "tracks" : [], "goalPos" : (0,0), "sTime" : time.mktime(time.localtime()), "eTime" : 0})
	goal.speed(10)
	ranking=readFile('ranking.txt', 5)
	reset(goal, t, info)
	onKey(wn, goal, t, info, ranking)
	turtle.mainloop()

def main() :
	lab()

if(__name__=="__main__") :
	main()
