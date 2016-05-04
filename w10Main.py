#시청역 37.565738    126.976851
#서대문역 37.565761   126.966639
#종로3가역  37.570414  126.992129
#을지로입구역 37.566064 126.982608
#광화문역  37.571610  126.976436
#경복궁역 37.575829   126.973516

import math


def lab10_8() : 
	locations=[(37.565738, 126.976851), (37.565761, 126.966639), (37.570414, 126.992129), (37.566064, 126.982608), (37.571610 ,126.976436)]
	kyungBok=(37.575829, 126.973516)

	dis=list()

	for loc in locations :
		dis.append(math.sqrt((loc[0]-kyungBok[0])**2 + (loc[1]-kyungBok[1])**2))

	print "distance of kyungBok station from nearest station : ",min(dis)

def main() :
	lab10_8()


if __name__=="__main__" :
	main()
