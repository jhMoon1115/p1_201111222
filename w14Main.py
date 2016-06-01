class Dog(object) : 
	def __init__(self, name) :
		self.name=name
	def getName(self) :
		print "my dog name is {0}".format(self.name)
	def talk(self) :
		print "mung mung..."

class Shitzu(Dog) :
	def talk(self) :
		print "si si!!"

class Maltese(Dog) :
	def talk(self) :
		print "mal mal!!"
		

def lab14_1() :
	mydog=Dog('choco')
	print "Dog talk .."
	mydog.talk()
	print "Shitzu talk .."
	s=Shitzu('shi')
	s.talk()
	print "Maltese talk .."
	m=Maltese('malt')
	m.talk()

def main() :
	lab14_1()
	
if __name__=='__main__' :
	main()

