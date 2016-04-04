"""
@author mjh
@since 160404
"""

def drawTriangle(char, len) :
	for i in range(1, len+1) :
		print ' '*(len-i)+'*'*(2*i-1)


def lab5() :
	char='*'
	len=10
	drawTriangle(char, len)

def main() :
	lab5()

if __name__=="__main__"
	main()