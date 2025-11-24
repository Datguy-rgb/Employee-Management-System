from datas import users

def login():
    print("\n" + "-"*60)
    print("                 >> LOGIN PAGE <<")
    print("-"*60)
    username = input("Enter Username: ")
    passw = input("Enter Password: ")
    if username in users and users[username] == passw:
        print("Login Successful!\n")
        return True
    else:
        print("Invalid Username or Password.")
        return False
