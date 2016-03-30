def computeGrade(marks) :
	if marks<=100 and marks>=90 :
		return "A"
	elif 80<=marks<90 :
		return "B"
	elif 60<=marks<80 :
		return "C"
	elif 40<=marks<60 :
		return "D"
	elif 0<=marks<40 :
		return "F"
	else :
		return "Marks have to be number between 0 and 100"

def lab1() :
	marks=float(raw_input("enter marks : "))
	grade=computeGrade(marks)
	print grade


def main() :
	lab1()
	raw_input("press 'any key' and 'enter key' if you want to finish...")


main()