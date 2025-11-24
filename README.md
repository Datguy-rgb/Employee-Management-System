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

- **Language**: Python 
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

### Menu Options

**1. Add Employee**

**2. Display Employee Records**

**3. Update Employee Record**

**4. Promote Employee Record**

**5. Remove Employee Record**

**6. Search Employee Record**

**7. Exit**

### Sample Data

The system comes pre-loaded with sample employee data:

| ID  | Name            | Email                      | Phone      | City    | Post      | Salary |
|-----|-----------------|----------------------------|------------|---------|-----------|--------|
| 101 | Aman Singh      | amankumar@gmail.com        | 9876543210 | Delhi   | CEO       | 80000  |
| 102 | Vikas Tiwari    | vikastiv11@gmail.com       | 9123456789 | Mumbai  | Chairman  | 50000  |
| 103 | Shubh Thadani   | shubhmax@hotmail.com       | 8999988888 | Chennai | Cofounder | 60000  |
| 104 | Rudreak Rokde   | rokdu991@outlook.com       | 7339655422 | Nashik  | Manager   | 20000  |

## Validation Rules

### Email Validation
- Must follow standard email format: `username@domain.extension`
- Example: `ankit.das@hotmail.com`

### Phone Number Validation
- Indian phone number format
- 10 digits starting with 7, 8, or 9
- Optional country code: 0 or 91
- Examples: `9876543210`, `919876543210`, `09876543210`

## System Architecture

### Module Descriptions

**menu.py**
- Application entry point
- Handles user authentication flow
- Displays main menu and routes user choices

**functions.py**
- Contains all CRUD operation implementations
- Imports data and validation modules
- Handles user input for each operation

**datas.py**
- Stores employee data in dictionary format
- Contains user credentials for authentication
- 
**Verification.py**
- Implements login functionality
- Validates credentials against stored users

**check.py**
- Input validation functions
- Email validation using regex
- Phone number validation using regex

### Data Flow

```
User Input → menu.py → Verification.py (Authentication)
                    ↓
              Main Menu Loop
                    ↓
    User Choice → functions.py (CRUD Operations)
                    ↓
              check.py (Validation)
                    ↓
              datas.py (Data Access)
                    ↓
              Result Display
```

##  Future Enhancements

- **Data Persistence**: Save data to CSV/JSON files
- **Advanced Search**: Search by name, post, or salary range
- **Sorting Options**: Sort employees by salary, name, or ID
- **Department Management**: Add department categorization
- **Export Reports**: Generate CSV/PDF reports
- **GUI Interface**: Develop Tkinter or web-based UI
- **Password Encryption**: Hash passwords for better security
- **Role-Based Access**: Admin and employee roles with different permissions


##  Known Issues

- Data is not persistent (lost on program exit)
- No password encryption
- Limited to console interface
- No backup/recovery mechanism


**Last Updated**: November 2025
