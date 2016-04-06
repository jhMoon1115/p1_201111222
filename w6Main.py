"""
@author mjh
@since 0406
"""

def sumMultiplesOf3And5(begin, end) :
	"""
	Main 9
	sum Multiples of 3 and 5 function

	parameters
	----------
	arg1 : int
		begin
	arg2 : int
		end

	Returns
	-------
	sum of multiples of 3 and 5

	Examples
	--------
	sumMultiplesOf3And5()
	"""
	sum=0
	for i in range(begin, end+1) :
		if(i%3==0 or i%5==0) :
			sum+=i
	return sum


def isLeapYear(year) :
	"""
	Main 11
	is Leap Year function

	parameters
	----------
	arg1 : int
		year

	Returns
	-------
	int

	Examples
	--------
	isLeapYear(2016)
	"""
	if (year%4==0) and (year%100!=0 or year%400==0) :
		return 1
	return 0

def lab6() :
	sum=sumMultiplesOf3And5(1, 1000)
	print "Main 9, Sum of Multiples of 3 and 5 : {0:d}".format(sum)
	print "\nMain11"
	year=int(raw_input("input year : "))
	re=isLeapYear(year)
	if re :
		print "{0:d} is Leap Year".format(year)
	else :
		print "{0:d} is not Leap Year".format(year)

def main() :
	lab6()

if __name__=="__main__" :
	main()

	