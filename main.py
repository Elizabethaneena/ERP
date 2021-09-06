from employee import Employee
from emp_store import employees
import employee as e
import search_emp as s
import change_emp as c

def main_menu():
	print("\n1. Add employee")
	print("2. Delete employee")
	print("3. Search employee")
	print("4. Display all employee")
	print("5. Change a employee details") 
	print("6. exit")

while True:
	main_menu()
	choice = int(input("Enter your choice : "))
	if choice == 1:

		serial_no = input("\tEnter the serial no : ")
		name = input("\tEnter name : ")
		age = input("\tEnter employee age : ")
		gender = input("\tEnter gender : ")
		place = input("\tEnter place : ")
		salary = input("\tEnter salary : ")
		previous_company = input("\tEnter previous company : ")
		joining_date = input("\tEnter joining_date : ")
		st_temp=Employee(serial_no,name,age,gender,place,salary,previous_company,joining_date)
		e.employees.append(st_temp)


	elif choice == 2: #delete 
		serial_no=input("\nEnter the serial no:")
		for i in employees:
			if i.serial_no == serial_no:
				employees.pop(employees.index(i))

	elif choice == 3:
		s.search_employee()
			
		
	elif choice == 4:
		for i in employees:
			print(f"{i.serial_no} |{i.name} | {i.age} | {i.gender} | {i.place} | {i.salary}| {i.previous_company} | {i.joining_date}")
	elif choice == 5:
		c.change_main()
	elif choice == 6:
		#Exit
		break;
	else:
		print("Invalid Choice")
