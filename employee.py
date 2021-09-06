from emp_store import employees
class Employee:
	def __init__(self, serial_no = 0, name = "", age = 0, gender = "",salary = 0, place = "", previous_company = "", joining_date = ""):
		self.serial_no = serial_no
		self.name = name
		self.age = age
		self.gender = gender
		self.place = place
		self.salary = salary
		self.previous_company = previous_company
		self.joining_date = joining_date
	def set_name(self,name):
		self.name = name
		return "name assigned successfully"
	def set_age(self,age):
		self.age = age
		return "age assigned successfully"
	def set_gender(self,gender):
		self.gender = gender
		return "gender assigned successfully"
	def set_place(self,place):
		self.place = place
		return "place assigned successfully"
	def set_salary(self,salary):
		self.salary = salary
		return "salary assigned Successfully"
	def set_previous_company(self,previous_company):
		self.previous_company = previous_company
		return "Previous company assigned successfully"
	def set_joining_date(self,joining_date):
		self.joining_date = joining_date
		return "Joining date company assigned Successfully"
