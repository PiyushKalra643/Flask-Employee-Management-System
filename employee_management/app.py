# Import the Flask class and other modules
from flask import Flask, render_template, request, redirect, url_for

# Initialize a list of dictionaries to act as our "database"
# Each dictionary represents an employee
employees = [
    {'id': 1, 'name': 'Alice Smith', 'role': 'Software Engineer', 'department': 'Engineering'},
    {'id': 2, 'name': 'Bob Johnson', 'role': 'Project Manager', 'department': 'Marketing'},
    {'id': 3, 'name': 'Charlie Brown', 'role': 'UX Designer', 'department': 'Design'},
]
next_id = 4  # Keep track of the next available employee ID

# Initialize the Flask application
app = Flask(__name__)


# Route for the home page, which displays all employees
@app.route('/')
def index():
    # Render the index.html template and pass the employees list to it
    return render_template('index.html', employees=employees)


# Route to add a new employee
@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    # If the request is a POST, it means the form was submitted
    if request.method == 'POST':
        # These must be the first lines to reference the global variables
        global next_id
        global employees

        # Get data from the form
        name = request.form['name']
        role = request.form['role']
        department = request.form['department']

        # Create a new employee dictionary and add it to our list
        new_employee = {'id': next_id, 'name': name, 'role': role, 'department': department}
        employees.append(new_employee)
        next_id += 1

        # Redirect the user back to the home page
        return redirect(url_for('index'))

    # If the request is a GET, just show the form
    return render_template('add_employee.html')


# Route to edit an existing employee
@app.route('/edit/<int:employee_id>', methods=['GET', 'POST'])
def edit_employee(employee_id):
    employee = None
    # Find the employee with the matching ID
    for emp in employees:
        if emp['id'] == employee_id:
            employee = emp
            break

    # If the employee is not found, redirect to the home page
    if not employee:
        return redirect(url_for('index'))

    # If the request is a POST, update the employee's data
    if request.method == 'POST':
        employee['name'] = request.form['name']
        employee['role'] = request.form['role']
        employee['department'] = request.form['department']

        # Redirect to the home page after updating
        return redirect(url_for('index'))

    # If the request is a GET, show the edit form with the current employee data
    return render_template('edit_employee.html', employee=employee)


# Route to delete an employee
@app.route('/delete/<int:employee_id>')
def delete_employee(employee_id):
    # This must be the first line to reference the global variable
    global employees
    # Filter out the employee with the matching ID
    employees = [emp for emp in employees if emp['id'] != employee_id]

    # Redirect to the home page after deletion
    return redirect(url_for('index'))


# This part runs the app when the script is executed
if __name__ == '__main__':
    # 'debug=True' reloads the server automatically on code changes
    app.run(debug=True)

