unit=raw_input("F or C : ")


tem=float(raw_input("temperature : "))


if(unit=='F'):
	result=(tem-32)/1.8
elif(unit=='C'):
	result=tem*1.8+32
else:
	result="user input error"

print result

raw_input("\npress 'any key' and 'enter key' if you want to finish... ")
