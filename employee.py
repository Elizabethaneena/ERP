employee = {} #Empty dictionary
groups = {} #empty dictionary
def add_employee():
	serial_no = input("Enter serial_no")
	if serial_no not in employee.keys():
		name=input("Enter the employee name\n")
		age=int(input("enter the age"))        
		gender=input("enter the gender")
		place=input("Enter the place")
		salary=int(input("Enter the salary"))
		previous_company=input("Enter the previous company")
		joining_date=int(input("Enter the joining date"))
		temp = {
                        "name" : name,
                        "age" : age,
                        "gender" : gender,
                        "place" : place,
                        "salary" : salary,
                        "previous_company" : previous_company,
                        "joining_date" : joining_date
                        }
		employee[serial_no] = temp
	else:
		print("Serial no already taken")



def delete_employee():
	serial_no = input("\tEnter serial no")
	if serial_no not in employee.keys():
		print("\tWrong serial No")
	else:
		del employee[serial_no]
def search_employee():
	name = input("Enter name")
	found = False
	for i in employee.values():
		if i["name"] == name:
			print(f"{i['name']} | {i['age']} |{i['gender']} |{i['place']} |{i['salary']} | {i['previous_company']} | {i['joining_date']} ")
			found = True
			break
		if found == False :
			print("Not found")
	

def display_employee():
	for serial,employee in employee.items():
		print(f"{serial} | {employee['name']} | {employee['age']} | {employee['gender']} | {employee['place']} | {employee['salary']} | {employee['previous_company']} | {employee['joining_date']}")


def change_employee_name():
	serial_no = input("\tEnter serial no.")
	if serial_no not in employee.keys():
		print("\tWrong serial no")
	else:
		employee[serial_no]['name'] = input("\tEnter new name")
		employee[serial_no]['age'] = int(input("Enter the new age"))
		employee[serial_no]['gender'] = input("Enter the new gender")
		employee[serial_no]['place'] = input("Enter the new place")


def main_menu():
	print("1. Add employee details")
	print("2. Delete employee")
	print("3. Search employee")
	print("4. Display all employee details")
	print("5.Change employee data")
	print("6.Manage all groups")
	print("7.Exit")


def manage_all_group_menu():
	print("\t1.Create Group")
	print("\t2.Display Groups")
	print("\t3.Manage Group(Particular)")
	print("\t4.Delete Group")
	print("\t5.Exit")

def manage_all_groups():
	while True:
		manage_all_group_menu()
		ch = int(input("\tEnter your choice "))
		if ch == 1:
			#Create group
			create_group()
		elif ch == 2:
			#display groups
			display_groups()
		elif ch == 3:
			#Manage group(Particular)
			manage_group()
		elif ch == 4:
			#Delete Group
			delete_group()
		elif ch == 5:
			#exit
			break
		else:
			print("\tInvalid choice")	

def create_group():
	group_name = input("\tEnter group name ")
	groups[group_name] = []

def delete_group():
	group_name = input("\tEnter group name ")
	if group_name in groups.keys():
		del groups[group_name]
		print("\tDeleted the group")
	else:
		print("\tWrong group name")

def display_groups():
	for key,value in groups.items(): #key is group_name,value is list of employee
		name_string = ""
		for i in value:
			name_string = name_string +"|"+employee[i]["name"]
		print(f"{key} => {name_string}")

def manage_group_menu():
	print("\t\t1.Add Member")
	print("\t\t2.Delete Member")
	print("\t\t3.List Members")
#	print("\t\t4.Exit")
	

def manage_group():
	group_name = input("\t\tEnter group name ")
	manage_group_menu()
	ch = int(input("\t\t Enter your Choice "))
	if ch == 1:
		#Add member
		add_member(group_name)
	elif ch == 2:
		#Delete member
		delete_member(group_name)
	elif ch == 3:
		#List member
		list_member(group_name)
	else:
		print("\tInvalid choice")	
	
def add_member(group_name):
	display_student()
	serial_no = input("\t\tEnter the serial no of student ")
	if serial_no in students.keys():
		groups[group_name].append(serial_no)
	else:
		print("\t\tWrong serial No.")

def list_member(group_name):
	name_string=""
	for i in groups[group_name]:
		name_string = name_string +"|"+i+"."+students[i]["name"]
	print(f"{name_string}")

def delete_member(group_name):
	list_member(group_name)
	serial_no = input("\t\tEnter serial no from list")
	if serial_no in groups[group_name]:
		groups[group_name].remove(serial_no)
	else:
		print("\t\tWrong serial No.")

	



while True:
	main_menu()
	ch = int(input("Enter your choice"))
	if ch == 1:
		#Add employee
		add_employee()
	elif ch == 2:
		#Delete employee
		delete_employee()
	elif ch == 3:
		#Search employee
		search_employee()
	elif ch == 4:
		#Display 
		display_employee()
	elif ch== 5:
		#Change a employee name in the list
		change_employee_name()
	elif ch == 6:
		#Manage groups
		manage_all_groups()
	elif ch == 7:
		#Exit
		break;
	else:
		print("Invalid Choice")


