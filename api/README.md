# ALX Intro to Software Engineering Python API Project

This directory contains Python script solutions for the ALX Intro to Software Engineering Python API project. The project consists of four tasks, each with specific requirements. Below, you will find descriptions of each task and the associated scripts.

### Description
Write a Python script that, using the REST API, retrieves information about a given employee's TODO list progress.

### Requirements
- Use `urllib` or `requests` module
- Accept an integer as a parameter (employee ID)
- Display employee TODO list progress in the following format:
  - First line: `Employee EMPLOYEE_NAME is done with tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):`
    - `EMPLOYEE_NAME`: name of the employee
    - `NUMBER_OF_DONE_TASKS`: number of completed tasks
    - `TOTAL_NUMBER_OF_TASKS`: total number of tasks (completed and non-completed)
  - Subsequent lines: Display the title of completed tasks with one tabulation and one space before each `TASK_TITLE`

### Script
- `task0.py`

## Task 1: Export to CSV

### Description
Extend the script from Task 0 to export data in CSV format.

### Requirements
- Record all tasks owned by the employee
- Format: `"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"`
- File name: `USER_ID.csv`

### Script
- `1-export_to_CSV.py`

## Task 2: Export to JSON

### Description
Extend the script from Task 0 to export data in JSON format.

### Requirements
- Record all tasks owned by the employee
- Format: `{ "USER_ID": [{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}`
- File name: `USER_ID.json`

### Script
- `2-export_to_JSON.py`

## Task 3: Export All Employees' Data to JSON

### Description
Extend the script from Task 0 to export data for all employees in JSON format.

### Requirements
- Record all tasks from all employees
- Format: `{ "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ]}`
- File name: `todo_all_employees.json`

### Script
- `2-export_to_JSON.py`

**Note**: Ensure that you have the required modules (e.g., `requests` or `urllib`) installed to run the scripts successfully.