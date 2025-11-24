from functions import (add_emp, display_emp, update_emp,promote_emp, remove_emp, search_emp)
from Verification import login

def menu():
    while True:
        print("\n" + "*" * 60)
        print("          >> EMPLOYEE MANAGEMENT SYSTEM <<")
        print("*" * 60)
        print("""
1. Add Employee
2. Display Employee Records
3. Update Employee Record
4. Promote Employee
5. Remove Employee Record
6. Search Employee Record
7. Exit
""")
        o = int(input("Enter your choice: "))

        if o == 1: 
            add_emp()
        elif o == 2: 
            display_emp()
        elif o == 3: 
            update_emp()
        elif o == 4: 
            promote_emp()
        elif o == 5: 
            remove_emp()
        elif o == 6: 
            search_emp()
        elif o == 7:
            print("Thank you! Have a nice day :)")
            break

if __name__ == "__main__":
    auth = False
    while not auth:
        auth = login()
        if not auth:
            print("Try Again.\n")
    menu()
