from emp_store import employees
def change_menu():
	print("\t1. Change by name")
	print("\t2. Change by age")
	print("\t3. Change by salary")
	print("\t4. Change by gender")
	print("\t5. exit")
def change_main():
	while True:
		change_menu()
		choice=int(input("Enter your choice : "))
		if choice == 1: #change name
			serial_no = input("Enter the serial no: ")
			st_temp  = list(filter(lambda a: a.e_id == serial_no,employees))
			st_temp[0].set_name(input("Enter new name: "))
			
		elif choice == 2: #change age
			age = input("Enter age : ")
			st_temp  = list(filter(lambda a: a.age == age,employees))
			st_temp[0].set_age(input("Enter new age: "))
			
		elif choice == 3: #change salary
			salary = input("Enter salary : ")
			st_temp  = list(filter(lambda a: a.salary == salary,employees))
			st_temp[0].set_salary(input("Enter new salary: "))
			
		elif choice == 4: #gender
			gender = input("Enter gender : ")
			st_temp  = list(filter(lambda a: a.gender == gender,employees))
			st_temp[0].set_gender(input("Enter new gender: "))
		elif choice == 5: #exit
			break
		else:
			print("Invalid choice")
