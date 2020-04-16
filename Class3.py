class Class1():
	def __init__(self):
		print("Class 1 Created")
	def method_1(self):
		print("method 1 ")
	def method_2(self):
		print("method 2 ")




class Class2(Class1):
	def __init__(self):
		Class1.__init__(self)
		print("Class 2 Created")
	def method_3(self):
		print("method 3 ")



# my_clas = Class2()
# my_clas.method(1,2,3)
