from datas import employees, check_emp, check_emp_name
from check import valemail, valphone

def add_emp():
    print("\n" + "-"*60)
    print("               >> Add Employee Record <<")
    print("-"*60)
    id = input("Enter Employee Id: ")
    if check_emp(id):
        print("Employee ID already exists!")
        input("Press Enter to continue...")
        return
    name = input("Enter Employee Name: ")
    if check_emp_name(name):
        print("Employee Name already exists!")
        input("Press Enter to continue...")
        return
    email_id = input("Enter Employee Email ID: ")
    if not valemail(email_id):
        print("Invalid Email!")
        input("Press Enter to continue...")
        return
    phone_no = input("Enter Employee Phone No.: ")
    if not valphone(phone_no):
        print("Invalid Phone Number!")
        input("Press Enter to continue...")
        return
    city = input("Enter Employee City: ")
    post = input("Enter Employee Post: ")
    salary = int(input("Enter Employee Salary: "))
    employees[id] = {
        "Name": name,
        "Email": email_id,
        "Phone": phone_no,
        "City": city,
        "Post": post,
        "Salary": salary
    }
    print("Successfully Added Employee Record.")
    input("Press Enter to continue...")

def display_emp():
    print("\n" + "-"*60)
    print("              >> Display Employee Records <<")
    print("-"*60)
    if not employees:
        print("No employee records found.")
    else:
        for emp_id, emp in employees.items():
            print(f"\nEmployee Id: {emp_id}")
            print("Employee Name:", emp["Name"])
            print("Employee Email:", emp["Email"])
            print("Employee Phone:", emp["Phone"])
            print("Employee City:", emp["City"])
            print("Employee Post:", emp["Post"])
            print("Employee Salary:", emp["Salary"])
            print("-"*40)
    input("Press Enter to continue...")

def update_emp():
    print("\n" + "-"*60)
    print("               >> Update Employee Record <<")
    print("-"*60)
    id = input("Enter Employee Id: ")
    if not check_emp(id):
        print("Employee not found!")
        input("Press Enter to continue...")
        return
    email_id = input("Enter New Email ID: ")
    if not valemail(email_id):
        print("Invalid Email!")
        input("Press Enter to continue...")
        return
    phone_no = input("Enter New Phone No.: ")
    if not valphone(phone_no):
        print("Invalid Phone Number!")
        input("Press Enter to continue...")
        return
    city = input("Enter New City: ")
    employees[id]["Email"] = email_id
    employees[id]["Phone"] = phone_no
    employees[id]["City"] = city
    print("Employee Record Updated Successfully.")
    input("Press Enter to continue...")


def promote_emp():
    print("\n" + "-"*60)
    print("              >> Promote Employee Record <<")
    print("-"*60)
    id = input("Enter Employee Id: ")
    if not check_emp(id):
        print("Employee not found!")
        input("Press Enter to continue...")
        return
    amt = int(input("Enter Salary Increase Amount: "))
    employees[id]["Salary"] += amt
    print("Employee Promoted Successfully.")
    input("Press Enter to continue...")

def remove_emp():
    print("\n" + "-"*60)
    print("               >> Remove Employee Record <<")
    print("-"*60)
    id = input("Enter Employee Id: ")
    if not check_emp(id):
        print("Employee not found!")
        input("Press Enter to continue...")
        return
    del employees[id]
    print("Employee Removed Successfully.")
    input("Press Enter to continue...")

def search_emp():
    print("\n" + "-"*60)
    print("               >> Search Employee Record <<")
    print("-"*60)
    id = input("Enter Employee Id: ")
    if not check_emp(id):
        print("Employee not found!")
        input("Press Enter to continue...")
        return
    emp = employees[id]
    print(f"\nEmployee Id: {id}")
    print("Employee Name:", emp["Name"])
    print("Employee Email:", emp["Email"])
    print("Employee Phone:", emp["Phone"])
    print("Employee City:", emp["City"])
    print("Employee Post:", emp["Post"])
    print("Employee Salary:", emp["Salary"])
    input("Press Enter to continue...")
