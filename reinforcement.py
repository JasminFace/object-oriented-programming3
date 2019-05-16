#EXERCISE 1

class Task:

    def __init__(self, description, due_date):
        self.description = description
        self.due = due_date

    def __str__(self):
        return f"Description: {self.description} -- Due: {self.due}"

groceries = Task("Buy Food", "Tuesday")
laundry = Task("Do laundry", "Next week")
gym = Task("Go to the gym", "EVERYDAY")

#EXERCISE 2

class ToDoList:

    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append(task)

    def show_list(self):
        print("----------------  STUFF TO DO  ----------------")
        print("-----------------------------------------------")
        for task in self.tasks:
            print(f"- {task}")



getitdone = ToDoList()

getitdone.add_task(gym)
getitdone.add_task(laundry)
getitdone.add_task(groceries)

getitdone.show_list()