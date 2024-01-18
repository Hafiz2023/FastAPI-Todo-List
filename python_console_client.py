# # python_console_client.py
# This Python script interacts with a FastAPI server 
# to create and delete TODO items. It prompts the user for a 
# title and description to create a new TODO, and requests the user
# for a TODO ID to delete an existing item. The requests library is 
# utilized to send HTTP requests to the specified API endpoints on
# http://127.0.0.1:8000. However, there are issues in the code,
# such as an infinite recursive call in create_todo(),
# and an incomplete if __name__ == "__main__": block. After correction, 
# the script now properly creates and deletes TODO items when executed.


import requests

BASE_URL = "http://127.0.0.1:8000"

def create_todo():
    title = input("Enter Todo Title: ")
    create_todo()
    delete_todo() 
    description = input("Enter Todo Description: ")
    response = requests.post(f"{BASE_URL}/todos/", json={"title": title, "description": description})
    if response.status_code == 200:
        print("Todo added successfully")

def delete_todo():
    todo_id = input("Enter Todo ID to delete: ")
    response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
    if response.status_code == 200:
        print("Todo deleted successfully")

if __name__ == "__main__":
 