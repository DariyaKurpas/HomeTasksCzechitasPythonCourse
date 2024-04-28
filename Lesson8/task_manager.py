from datetime import datetime


class Task:
    def __init__(self, description, timestamp=datetime.now()):
        self.description = description
        self.timestamp = timestamp

    def add_task(self):
        new_task = input("What is your new task?: ")
        task_id = len(tasks+1)
        if task_id not in tasks:
            tasks[task_id] = f"{new_task}, timestamp: {self.timestamp}"
            return f"Adding the new task was successful."
        else:
            return "There was an error. Please try again."

    def remove_task(self):
        remove_task_id = input("Which task ID would you like to remove?: ")
        if remove_task_id in tasks:
            tasks.pop(remove_task_id)
            return f"Your task with the number {remove_task_id} has been successfully removed."
        else:
            return "There was an error. Please try again."

    def show_tasks(self):
        return tasks


tasks = {}


while True:
    new_record = input("Do you want to manage your task manager? ")
    if new_record == "yes":
        action = input(
            "Would you like to create a task, remove a task or view the whole manager?: ")
        if action == "create":
