# Flask-Employee-Management-System

## Overview

This is a simple web-based Employee Management System built with the Flask framework in Python. The application allows users to view, add, edit, and delete employee records through a clean and responsive web interface. It uses an in-memory list for data storage, making it perfect for a lightweight, beginner-friendly project.

## Features

- **View Employees:** Displays a list of all employees in a table.
- **Add Employee:** A form to add a new employee with a name, role, and department.
- **Edit Employee:** Functionality to update an existing employee's details.
- **Delete Employee:** Option to remove an employee from the system.
- **Responsive Design:** The user interface is designed to work well on both desktop and mobile devices.

## Technologies Used

- **Python:** The core programming language for the backend logic.
- **Flask:** The web framework used to build the application.
- **HTML:** For the structure and content of the web pages.
- **CSS:** Styled with Tailwind CSS for a modern, clean look.

## Installation

Follow these steps to get the project up and running on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/employee_management.git](https://github.com/your-username/employee_management.git)
    cd employee_management
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install Flask
    ```

## Usage

1.  **Run the Flask application:**
    ```bash
    python app.py
    ```
2.  **Open the application in your browser:**
    Navigate to `http://127.0.0.1:5000` to access the application.

## File Structure

The project is organized as follows:

employee_management/
├── venv/
├── app.py
├── templates/
│   ├── index.html
│   ├── add_employee.html
│   └── edit_employee.html
└── static/
└── css/
└── style.css


