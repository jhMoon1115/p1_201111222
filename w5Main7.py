def drawTriangle(char, len) :
	for i in range(1, len+1) :
		print ' '*(len-i)+'*'*(2*i-1)

def lab7() :
	char='*'
	len=10
	drawTriangle(char, len)

def main() :
	lab7()
	raw_input("\npress 'any key' and 'enter key' if you want to finish...")

main()
