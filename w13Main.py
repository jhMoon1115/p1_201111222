import os
import time

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

def main() :
	lab13_2()
	lab13_4()

if __name__=='__main__' :
	main()
#num=[[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]