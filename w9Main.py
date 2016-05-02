import matplotlib
import matplotlib.pyplot as plt

def charCount(word) :
	d=dict()
	for i in word :
		#if not d.get(i) :
			#d.update({i : 1})
		if i not in d :
			d[i]=1
		else : 
			d[i]+=1
	return d

def countDigitsLetters(word) :
	d=dict({"digit" :0, "char" :0})
	for c in word :
		if c.isdigit() :
			d["digit"]+=1
		else :
			d["char"]+=1
	return d

def lab9_5() :
	print "===Main 5==="
	word="sangmyung university"
	print charCount(word)

def lab9_6() :
	word="sangmyung university, 20, hongjimun 2gil, jongnogu, seoul, 03016, republic of korea"
	d=countDigitsLetters(word)
	print "\n===Main 6==="
	print d
	plt.bar(range(len(d)), d.values())
	plt.xticks(range(len(d)), list(d.keys()))
	plt.show()

def lab9_7() :
	print "\n===Main 7==="
	mine={"TV", "phone", "camera", "fridger", "mixer", "audio", "cd player", "light", "computer", "notebook", "recoder"}
	friend={"coffee machine", "radio", "camera", "running machine", "ramp", "computer", "notebook", "recoder"}

	all=mine.union(friend) #모든 가전제품
	onlyMine=all.difference(mine) #내 방에만 있는 가전제품
	print "** In only my room : ",
	print onlyMine

	onlyFriend=all.difference(friend) #친구 방에만 있는 가전제품
	print "** In only friend's room : ",
	print onlyFriend

	print "** In all room : ",
	common=set() 
	for i in mine :
		if i in friend :
			common.add(i)# 공통된 가전제품
	print common

	print "** All electronic machine : "
	print all
	
	print "** Count electronic machine"
	for i in all :
		if i in common :
			print i,
			print 2
		else :
			print i,
			print 1


			
def main() :
	lab9_5()
	lab9_6()
	lab9_7()

if __name__=="__main__" :
	main()