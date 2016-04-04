"""
@author mjh
@since 160404
"""

def drawTriangle(char, len) :
	"""
	draw Triangle function
	
	parameters
	----------
	arg1 : str
		char
	arg2 : int
		len

	Returns
	-------
	none
		
	Examples
	--------
	drawTriangle("*", 10)
	"""
	for i in range(1, len+1) :
		print ' '*(len-i)+'*'*(2*i-1)

def computeBMI(weight, height) :
	"""
	compute BMI function
	
	parameters
	----------
	arg1 : float
		weight(kg)
	arg2 : float
		height(cm)

	Returns
	-------
	none
		
	Examples
	--------
	computeBMI(70, 170)
	"""
	mHei=height/100.
	bmi=weight/(mHei*mHei)
	if bmi<18.5 :
		print "low weight"
	elif bmi>=18.5 and bmi<23 :
		print "normal weight"
	elif bmi>23 :
		print "over weight"
	else :
		print "error"


def lab5() :
	char='*'
	len=10
	drawTriangle(char, len)
	print
	weight=70
	height=170
	computeBMI(weight, height)

def main() :
	lab5()

if __name__=="__main__":
	main()

