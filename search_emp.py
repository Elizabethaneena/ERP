from emp_store import employees
def search_menu():
	print("\t1. Search by name")
	print("\t2. Search by age")
	print("\t3. Search by salary")
	print("\t4. Search by gender")
	print("\t5. exit")

def search_employee():
	while True:
		search_menu()
		choice = int(input("Enter your choice : "))
		if choice == 1:
			name = input("Enter name :")
			st = list(filter(lambda a: a.name == name , employees))
			if len(st) == 0:
				print("No employee found")
			else:
				for i in st:
					print(f"{i.name}")
		elif choice == 2:
			age = input("Enter age :")
			st = list(filter(lambda a: a.age == age , employees))
			if len(st) == 0: 
				print("No employee found")
			else:
				for i in st:
					print(f"{i.age}")
					
		elif choice == 3:
			salary = input("Enter salary :")
			st = list(filter(lambda a: a.salary == salary , employees))
			if len(st) == 0:
				print("No employee found")
			else:
				for i in st:
					print(f"{i.salary}")
				
		elif choice == 4:
			gender = input("Enter gender :")
			st = list(filter(lambda a: a.gender == gender , employees))
			if len(st) == 0: 
				print("No employee found")
			else:
				for i in st:
					print(f"{i.gender}")
				
		elif choice == 5:
			break
		else:
			print("Invalid choice")
