# streamlit_client.py
# This Streamlit script creates a Todo App with a user-friendly interface. 
# It allows users to input TODO titles and descriptions, 
# and provides buttons to add and delete TODO items. 
# The create_todo function captures user input, sends a POST request 
# to a FastAPI server to add a new TODO, and displays a success message 
# upon success. The delete_todo function prompts users for a TODO ID,
# triggers a DELETE request to remove the specified TODO, and shows a success 
# message if the operation is successful. When executed, users can interact 
# with the app to manage their TODO list.

import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("Todo App by Hafiz Adil")

def create_todo():
    name = st.text_input("Enter Todo Title")
    description = st.text_area("Enter Todo Description")
    if st.button("Add Todo"):
        response = requests.post(f"{BASE_URL}/todos/", json={"name": name, "description": description})
        if response.status_code == 200:
            st.success("Todo added successfully")

def post_todo():
    todo_id = st.number_input("Enter Todo ID to delete")
    if st.button("POST Todo"):
        response = requests.post(f"{BASE_URL}/todos/{todo_id}")
        if response.status_code == 200:
            st.success("Todo post successfully")

if __name__ == "__main__":
    create_todo()
    post_todo()