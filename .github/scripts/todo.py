class Task:
    def __init__(self, title, status="ToDo"):
        self.title = title
        self.status = status
        self.completed = False

    def mark_completed(self):
        self.completed = True
        self.status = "Done"

    def __repr__(self):
        return f"{self.title} - {self.status}"

    def __str__(self):
        return f"Task: {self.title}, Status: {self.status}"


class TaskPool:
    def __init__(self):
        self.tasks = []

    def populate(self):
        t1 = Task("Task 1")
        t2 = Task("Task 2")
        t3 = Task("Task 3")
        t4 = Task("Task 4")
        t5 = Task("Task 5")
        t6 = Task("Task 6")
        t1.mark_completed()
        t2.mark_completed()
        t3.mark_completed()
        self.tasks = [t1, t2, t3, t4, t5, t6]

    def add_task(self, task):
        self.tasks.append(task)

    def get_open_tasks(self):
        return [t for t in self.tasks if t.status == "ToDo"]

    def get_done_tasks(self):
        return [t for t in self.tasks if t.status == "Done"]


def main():
    pool = TaskPool()
    pool.populate()
    todo = [t.title for t in pool.get_open_tasks()]
    print("ToDo Tasks:")
    for t in todo:
        print(t)
    done = [t.title for t in pool.get_done_tasks()]
    print("Done Tasks:")
    for t in done:
        print(t)

if __name__ == "__main__":
    main()
    