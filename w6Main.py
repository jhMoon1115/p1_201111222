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

def upAndDownGame(answer) :
	"""
	check answer is bigger than proposal function
	
	parameters
	----------
	arg1 : int
		answer

	returns
	-------
	int
		cnt

	Examples
	--------
	upAndDownGame(56)
	"""
	cnt=0
	while True :
		cnt+=1
		input=int(raw_input("input positive integer : "))
		if answer>input :
			print "Up"
		elif answer<input :
			print "Down"
		else :
			print "Correct Answer"
			break
	return cnt

def lab6() :
	sum=sumMultiplesOf3And5(1, 1000)
	print "Main 9, Sum of Multiples of 3 and 5 : {0:d}".format(sum)


def lab6_1() :
	print "\nMain11"
	year=int(raw_input("input year : "))
	re=isLeapYear(year)
	if re :
		print "{0:d} is Leap Year".format(year)
	else :
		print "{0:d} is not Leap Year".format(year)

def lab6_2() :
	print "\nUp and Down Game"
	answer=int(raw_input("input one number "))
	print "You get the right answer at {0:d} times.".format(upAndDownGame(answer))

"""
@author mjh
@since 0411
"""

def sumList(list) :
	"""
	sum of Elements of list function
	
	parameters
	----------
	arg1 : list
		list

	returns
	-------
	int 
		sum

	Examples
	--------
	sumList([1,2,3,4,5])
	"""
	sum=0
	for i in list :
		sum+=i
	return sum

def lab6_3() :
	print "\nSum of List : ",
	x=list()
	for i in range(1, 1001) :
		if(i%4==0 and i%5!=0) :
			x.append(i)
	sum=sumList(x)
	print sum

def main() :
	lab6()
	lab6_1()
	lab6_2()
	lab6_3()

if __name__=="__main__" :
	main()

