# Employee Management System

## Project Overview

The **Employee Management System** is a console-based Python application designed to manage employee records efficiently using in-memory data structures. The system provides a user-friendly interface for performing CRUD (Create, Read, Update, Delete) operations on employee data with built-in authentication and validation mechanisms.

## Key Features

- **Secure Authentication System**: Login functionality with username/password verification
- **Complete Employee CRUD Operations**:
  - Add new employee records with validation
  - Display all employee records in a formatted view
  - Update existing employee information (email, phone, city)
  - Promote employees with salary increment
  - Remove employee records from the system
  - Search for specific employee by ID
- **Data Validation**: Email and phone number validation using regex patterns
- **Duplicate Prevention**: Checks for duplicate employee IDs and names
- **In-Memory Storage**: Uses Python dictionaries for fast data access and manipulation
- **Modular Architecture**: Clean separation of concerns across multiple modules

## Technologies Used

- **Language**: Python 3.x
- **Data Structures**: Dictionaries, Lists
- **Libraries**: 
  - `re` (Regular Expressions) - for validation
- **Storage**: In-memory (Dictionary-based)

## Project Structure

```
employee-management-system/
│
├── menu.py              # Main menu and application entry point
├── functions.py         # Core CRUD operation functions
├── datas.py            # Data storage and helper functions
├── Verification.py     # Authentication module
├── check.py            # Input validation functions
└── README.md           # Project documentation
```

## Installation Instructions

### Prerequisites
- Python 3.6 or higher installed on your system
- No external dependencies required (uses standard library only)

### Setup Steps

1. **Clone or Download the Project**
   ```bash
   git clone https://github.com/Datguy-rgb/Employee-Management-System.git
   cd employee-management-system
   ```

2. **Verify Python Installation**
   ```bash
   python --version
   # or
   python3 --version
   ```

3. **Run the Application**
   ```bash
   python menu.py
   # or
   python3 menu.py
   ```

## Usage Instructions

### Starting the Application

1. Run the main program:
   ```bash
   python menu.py
   ```

2. **Login Credentials** (Default):
   - Username: `Aman` | Password: `RaNdOm`
   - Username: `Vikas` | Password: `Da345DxD`
   - Username: `Shubh` | Password: `You25HxH`

3. After successful login, you'll see the main menu with 7 options

### Sample Data

The system comes pre-loaded with sample employee data:

| ID  | Name            | Email                      | Phone      | City    | Post      | Salary |
|-----|-----------------|----------------------------|------------|---------|-----------|--------|
| 101 | Aman Singh      | amankumar@gmail.com        | 9876543210 | Delhi   | CEO       | 90000  |
| 102 | Vikas Tiwari    | vikastiv11@gmail.com       | 9123456789 | Mumbai  | Chairman  | 50000  |
| 103 | Shubh Thadani   | shubhmax@hotmail.com       | 8999988888 | Chennai | Cofounder | 70000  |
| 104 | Rudreak Rokde   | rokdu991@outlook.com       | 7785562333 | Nashik  | Manager   | 20000  |

## Validation Rules

### Email Validation
- Must follow standard email format: `username@domain.extension`
- Example: `ankitpal@gmail.com`

### Phone Number Validation
- Indian phone number format
- 10 digits starting with 7, 8, or 9
- Optional country code: 0 or 91
- Examples: `9876543210`, `919876543210`, `09876543210`

## Testing Instructions

### Manual Testing Scenarios

**Test 1: Add Employee**
```
1. Login to the system
2. Choose option 1 (Add Employee)
3. Enter ID: 105
4. Enter Name: Test User
5. Enter Email: test@example.com
6. Enter Phone: 9999999999
7. Enter City: Bangalore
8. Enter Post: Manager
9. Enter Salary: 45000
Expected: Success message displayed
```

**Test 2: Duplicate ID Prevention**
```
1. Try adding employee with ID 101 (already exists)
Expected: Error message "Employee ID already exists!"
```

**Test 3: Invalid Email**
```
1. Add employee with email: "invalid-email"
Expected: Error message "Invalid Email!"
```

**Test 4: Search Employee**
```
1. Choose option 6 (Search Employee)
2. Enter ID: 101
Expected: Complete details of Aman Singh displayed
```

**Test 5: Update Employee**
```
1. Choose option 3 (Update Employee)
2. Enter ID: 102
3. Update email, phone, city
Expected: Success message with updated details
```

**Test 6: Promote Employee**
```
1. Choose option 4 (Promote Employee)
2. Enter ID: 101
3. Enter increase amount: 5000
Expected: Salary increased from 90000 to 95000
```

**Test 7: Remove Employee**
```
1. Choose option 5 (Remove Employee)
2. Enter ID: 104
Expected: Employee removed successfully
```

**Test 8: Invalid Login**
```
1. Enter wrong username or password
Expected: Error message and retry prompt
```

## Future Enhancements

- **Data Persistence**: Save data to CSV/JSON files
- **Advanced Search**: Search by name, post, or salary range
- **Sorting Options**: Sort employees by salary, name, or ID
- **Export Reports**: Generate CSV/PDF reports
- **GUI Interface**: Develop Tkinter or web-based UI
- **Password Encryption**: Hash passwords for better security
- **Role-Based Access**: Admin and employee roles with different permissions



---

**Last Updated**: November 2025
