class Task:

    def __init__(self, job, due_date,):
        self.job = job
        self.due = due_date
        self.done = False

    def __str__(self):
        return f"Description: {self.job} -- Due: {self.due}"


dishes = Task("Dishes", "NOW")
print(dishes)

