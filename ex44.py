#implicit inheritance
class Parent(object):

	def implicit(self):
		print "PARENT implicit()"

class Child(Parent):
	pass

dad = Parent()
son = Child()
dad.implicit()
son.implicit()

#PARENT implicit()
#PARENT implicit()


#explicit override
class Parent(object):
	
	def override(self):
		print "PARENT override()"

class Child(Parent):

	def override(self):
		print "CHILD override()"

dad = Parent()
son = Child()
dad.override()
son.override()

#PARENT override()
#CHILD override()


#alter before or after
class Parent(object):

	def altered(self):
		print "PARENT altered()"

class Child(Parent):

	def altered(self):
		print "CHILD, BEFORE PARENT altered()"
		super(Child, self).altered()
		print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()
dad.altered()
son.altered()

#PARENT altered()
#CHILD, BEFORE PARENT altered()
#PARENT altered()
#CHILD, AFTER PARENT altered()



#multiple inheritance => method resolution order
class SuperFun(Child, BadStuff):
	pass


#super() with __init__
class Child(Parent):
	def __init__(self, stuff):
		self.stuff = stuff
		super(Child, self).__init__()


#composition using other classes and modules
class Other(object):

	def override(self):
		print "OTHER override()"

	def implicit(self):
		print "OTHER implicit()"

	def altered(self):
		print "OTHER altered()"

class Child(object):

	def __init__(self):
		self.other = Other()

	def implicit(self):
		self.other.implicit()

	def override(self):
		print "CHILD override()"

	def altered(self):
		print "CHILD, BEFORE OTHER altered()"
		self.other.altered()
		print "CHILD, AFTER OTHER altered()"

son = Child()

son.implicit()
son.override()
son.altered()

#OTHER implicit()
#CHILD override()
#CHILD, BEFORE OTHER altered()
#OTHER altered()
#CHILD, AFTER OTHER altered()





















