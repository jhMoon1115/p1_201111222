#return : -1(error), 0(draw), 1(rsp1 win), 2(rsp1 lose) 
def doRSP(rsp1, rsp2) :
	if((rsp1!='rock' and rsp1!='scissor' and rsp1!='paper') or (rsp2!='rock' and rsp2!='scissor' and rsp2!='paper')) :
		return -1
	elif(rsp1==rsp2) :
		return 0
	elif(rsp1=='scissor') :
		if(rsp2=='paper') :
			return 1
		else:
			return 2
	elif(rsp1=='rock') :
		if(rsp2=='scissor') :
			return 1
		else :
			return 2
	elif(rsp1=='paper') :
		if(rsp2=='rock') :
			return 1
		else :
			return 2
			
def lab2() :
	user1=raw_input("user1 : rock, scissor, paper !! ")

	user2=raw_input("user2 : rock, scissor, paper !! ")

	result=doRSP(user1, user2)
	if(result==0) :
		print "draw"
	elif(result==1) :
		print "user1 wins"
	elif(result==2) :
		print "user2 wins"
	else :
		print "please check spelling of your inputs"

def main() :
	lab2()
	raw_input("\npress 'any key' and 'enter key' if you want to finish...")

main()

