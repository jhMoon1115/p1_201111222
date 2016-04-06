def sumMultiplesOf3And5() :
	sum=0
	for i in range(1, 1001) :
		if(i%3==0 or i%5==0) :
			sum+=i
	return sum


def isLeapYear(year) :
	if (year%4==0) and (year%100!=0 or year%400==0) :
		return True
	return False



def lab6() :
	sum=sumMultiplesOf3And5()
	print "Main 9, Sum of Multiples of 3 and 5 : {0:d}".format(sum)

def main() :
	lab6()

if __name__=="__main__" :
	main()

	