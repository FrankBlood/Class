class SchoolMember:
	population=0
	def __init__(self,name,age):
		self.name=name
		self.age=age
		SchoolMember.population+=1
		print('Initialized SchoolMember:%s'%self.name)

	def tell(self):
		print('Name:"%s" Age:"%s" '%(self.name,self.age))

class Teacher(SchoolMember):
	def __init__(self,name,age,salary):
		SchoolMember.__init__(self,name,age)
		self.salary=salary
		print('Initialized Teacher: %s'%self.name)

	def tell(self):
		SchoolMember.tell(self)
		print('Salary: "%d"'%self.salary)

class Student(SchoolMember):
	def __init__(self,name,age,marks):
		SchoolMember.__init__(self,name,age)
		self.marks=marks
		print('Initialized Student: %s'%self.name)

	def tell(self):
		SchoolMember.tell(self)
		print('Marks:"%s"'%self.marks)

t=Teacher('Guoxiu',40,30000)
s=Student('Dong',12,75)

print(t.population)
members=[t,s]
for member in members:
	member.tell()