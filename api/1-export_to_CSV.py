import csv
import requests
import sys

def get_employee_todo_progress(employee_id):
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    
    if employee_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return
    
    employee_data = employee_response.json()
    employee_username = employee_data['username']

    # Fetch employee's TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    
    if todos_response.status_code != 200:
        print(f"Unable to fetch TODO list for employee with ID {employee_id}.")
        return
    
    todos_data = todos_response.json()

    # Create CSV file and write data
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL, delimiter=',', quotechar='"')
        
        # Write task data
        for todo in todos_data:
            writer.writerow([
                f'"{employee_id}"',
                f'"{employee_username}"',
                f'"{str(todo["completed"])}"',
                f'"{todo["title"]}"'
            ])

if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)