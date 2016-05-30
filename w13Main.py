import os
import time
import turtle
wn=turtle.Screen()
t=turtle.Turtle()

def lab13_2() :
	word='line'
	fin=open('output.txt', 'r')
	fout=open('outputUpper.txt', 'w')
	editor='mjh'
	editedtime=time.strftime('%Y-%m-%d %H:%M:%S')
	stamp='[{0} edited {1}]'.format(editor, editedtime)
	for line in fin :
		if word in line :
			fout.write(stamp+line.replace(word, word.upper()))
		else :
			fout.write(line)
	
	fin.close()
	fout.close()


def lab13_4() :
	data=[1,2,3,4,5,6,7,8,9,10]
	fout=open('outputNumber.txt', 'w')
	for num in data :
		fout.write('{0}\t'.format(num))
		if(num%2==0) :
			fout.write('\n')
	fout.close()

def lab13_5() :
	try :
		fin1=open('python.txt', 'a')
		fin2=open('outputNumber.txt.', 'r')
	except IOError as e:
		print e
	else :
		for line in fin2 :
			fin1.write(line)
		fin1.close()
		fin2.close()

def getCoordsFromFile(aFile) :
	coords=list()
	try :
		f=open(aFile, 'r')
	except IOError as e :
		print e
	else :
		for line in f :
			tmp=line.split(',')
			coords.append([(float(tmp[0]), float(tmp[1])), (float(tmp[2]), float(tmp[3]))])
		f.close()
	
	return coords

def drawSquareWithCoords(coords) :
	t.penup()
	t.setpos(coords[0])
	t.pendown()
	t.setpos(coords[1][0], coords[0][1])
	t.setpos(coords[1])
	t.setpos(coords[0][0], coords[1][1])
	t.setpos(coords[0])
	
def lab13_6() :
	coords=getCoordsFromFile('coords.txt')
	for coord in coords :
		drawSquareWithCoords(coord)

def main() :
	lab13_2()
	lab13_4()
	lab13_5()
	lab13_6()
	wn.exitonclick()

if __name__=='__main__' :
	main()
