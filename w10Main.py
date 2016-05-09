
#시청역 37.565738    126.976851
#서대문역 37.565761   126.966639
#종로3가역  37.570414  126.992129
#을지로입구역 37.566064 126.982608
#광화문역  37.571610  126.976436
#경복궁역 37.575829   126.973516

import math
import matplotlib
import matplotlib.pyplot as plt

def lab10_8() : 
	print "==main 8=="
	locations=[(37.565738, 126.976851), (37.565761, 126.966639), (37.570414, 126.992129), (37.566064, 126.982608), (37.571610 ,126.976436)]
	kyungBok=(37.575829, 126.973516)

	dis=list()

	for loc in locations :
		dis.append(math.sqrt((loc[0]-kyungBok[0])**2 + (loc[1]-kyungBok[1])**2))

	print "distance of kyungBok station from nearest station : ",min(dis)

def sumTotalPopulationByLocation(populations) :
	gu=list()
	for i in populations :
		gu.append(i[0]+i[1])
	return gu

def sumTotalPopulationByGender(populations) :
	men=0
	women=0
	total=len(populations)
	for item in populations :
		men+=item[0]
		women+=item[1]
	return [[men, women], [men/total, women/total]]

	
def lab10_9() :
	print "\n==main 9=="
	populations=[[74452, 76326], [61164, 61636], [109688, 115744], [144796, 146776], [17996, 181676], [177841, 177434], [204630, 205980], [223373, 232245],[161055, 166130], [171576, 176735],[279169, 293772], [239450, 251066], [148690, 156510], [182977, 196992],[237792, 242641],[283869, 296762], [209344, 210282], [118965, 114441],[186503, 186856], [195734, 203014], [254381, 249472], [212401, 229111], [271654, 295354], [319197, 335045], [229829, 231671]]
	gu = sumTotalPopulationByLocation(populations)
	gender=sumTotalPopulationByGender(populations)
	print "* Total population by Gu : {0}".format(gu)
	print "* Total pupulation by Gender : men - {0}, women - {1}".format(gender[0][0], gender[0][1])
	print "* Average pupulation by Gender : men - {0}, women - {1}".format(gender[1][0], gender[1][1])
	plt.xlabel("-gu")
	plt.ylabel("total sum of population by gu")
	plt.bar(range(len(gu)), gu)
	plt.show()

def lab10_10() :
	allData=[['Coffee', 'Water', 'Milk', 'Icecream'],['Espresso', 'No', 'No', 'No'],["Long Black", "Yes", "No", "No"],["Flat White", "No", "Yes", "No"],["Cappuccino", "No", "Yes - Frothy", "No"],["Affogato", "No", "No", "Yes"]]
	pList=allData[1:]
	print "==Main 10=="
	cntMilk=0.
	for item in pList :
		if "YES" in item[2].upper() :
			cntMilk+=1
	print "* Rate of Milk : {0}".format(cntMilk/len(pList))

def main() :
	lab10_8()
	lab10_9()
	lab10_10()

if __name__=="__main__" :
	main()
