#sampl data
employees = {
    "101": {"Name": "Aman Singh","Email": "amankumar@gmail.com","Phone": "9876543210","City": "Delhi","Post": "CEO","Salary": 80000},
    "102": {"Name": "Vikas Tiwari","Email": "vikastiv11@gmail.com","Phone": "9123456789","City": "Mumbai","Post": "Chairman","Salary": 40000},
    "103": {"Name": "Shubh Thadani","Email": "shubhmax@hotmail.com","Phone": "8999988888","City": "Chennai","Post": "Cofounder","Salary": 50000},
    "104": {"Name": "Rudreak Rokde","Email": "rokdu991@outlook.com","Phone": "8999988888","City": "Nashik","Post": "Manager","Salary": 20000}
}   

# Creds
users = {
    "Aman": "RaNdOm",
    "Vikas": "Da345DxD",
    "Shubh": "You25HxH",
}

def check_emp(emp_id):
    """Check if employee ID exists"""
    return emp_id in employees

def check_emp_name(name):
    """Check if employee name already exists"""
    for emp in employees.values():
        if emp["Name"] == name:
            return True
    return False
