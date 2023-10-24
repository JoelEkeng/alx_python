"""
This is a python module that takes id from d user
and send a request to the Url. the response is
formatted and save to a json file.

param:
    filename: string
    user_id : string
    data_to_json : function
"""
import json
import requests
import sys


def employee_todo_task():
    """
    Fetches the employee's details and TODO list using the
    provided API endpoints,
    exports the informationto a JSON file.

    Parameters:
    - employee_id (int): The ID of the employee.

    Returns:
    None
    """
    # format url with input from user
    user_url = 'https://jsonplaceholder.typicode.com/users'
    users_data = requests.get(user_url).json()

    all_task_data = {}
    
    for user_data in users_data:
        user_id = user_data.get('id')
        
        username = user_data.get('username')
        
        todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
        .format(user_id)
        todo_data = requests.get(todo_url).json()

        user_task_data = []
        for task in todo_data:
            user_task_data.append({
                "username":username,
                "task": task['title'],
                "completed": task['completed']
            })
        all_task_data[user_id] = user_task_data
    #   
    # request data frm to
    # do and user api
    

    # Write to JSON file name filename
    filename = "todo_all_employees.json"

    # open the file and overwrite it content with w
    with open(filename, 'w') as file:
        json.dump(all_task_data, file, indent=2)

# function call
if __name__=='__main__':
    employee_todo_task()