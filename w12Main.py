import os
import sys

def lab12_1() :
	mydir=os.getcwd()
	filename='python.txt'
	myfilename=os.path.join(mydir, filename)

	try :
		myfile=open(myfilename, 'r')
	except IOError as e:
		print e
		sys.exit()
	contents=myfile.readlines()
	myfile.close()
	print "==Main 1=="
	for content in contents :
		if content.lower().find('python')>-1 :
			print content

def lab12_2() :
	filename='output.txt'
	myfile=open(filename, 'w')
	line1='first line\n'
	myfile.write(line1)
	line2='\tsecond line\n'
	myfile.write(line2)
	line3='third\n'
	myfile.write(line3)
	myfile.close()

	try :
		myfile=open(filename, 'r')
	except IOError as e :
		print e
		sys.exit()
	
	contents=myfile.readlines()
	myfile.close()

	word='line'
	for i in range(0, len(contents)) :
		if word in contents[i] :
			contents[i]=contents[i].replace(word, word.upper())

	myfile=open(filename, 'w')
	for line in contents :
		myfile.write(line)
	myfile.close()

def main() :
	lab12_1()
	lab12_2()

if __name__=='__main__' :
	main()

