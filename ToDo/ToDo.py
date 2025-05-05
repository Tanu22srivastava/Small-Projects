class ToDo:
    def __init__(self):
        self.li = []

    def add_task(self, task):
        for t in self.li:
            if t['name'] == task:
                print(f"{task} already exists")
                return
        self.li.append({"name": task, "done": False})

    def remove_task(self, task):
        for t in self.li:
            if t['name'] == task:
                self.li.remove(t)
                print(f"{task} removed.")
                return
        print("No such task available")

    def show_task(self):
        if not self.li:
            print("No tasks available.")
        else:
            print("Current tasks:")
            for task in self.li:
                status = "✔️ Done" if task["done"] else "❌ Pending"
                print(f"- {task['name']} [{status}]")

    def mark_task(self, task):
        for t in self.li:
            if t['name'] == task:
                if t['done']:
                    print(f"{task} is already marked as completed")
                else:
                    t['done'] = True
                    print(f"{task} marked as completed")
                return
        print("No such task found")
    
    def show_completed(self):
        if not self.li:
            print("No tasks available.")
        else:
            print("Completed tasks are")
            for task in self.li:
                if task['done']:
                    print(task['name'])
    
    def show_pending(self):
        if not self.li:
            print("No tasks available.")
        else:
            print("Pending tasks are")
            for task in self.li:
                if not task['done']:
                    print(task['name'])

todo = ToDo()
todo.add_task("complete work")
todo.add_task("go to gym")
todo.add_task("eat good food")
todo.show_task()

todo.mark_task("go to gym")
todo.show_task()

# todo.remove_task("go to gym")
todo.show_completed()
todo.show_pending()
