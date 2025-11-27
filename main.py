class ToDoList:
    def __init__(self):
        self.task_list = {"Запустить программу" : "(СДЕЛАНО)"}
    def add_task(self, task):
        self.task_list[task] = "(НЕ СДЕЛАНО)"
    def complete_task(self, task):
        if task in self.task_list:
            self.task_list[task] = "(СДЕЛАНО)"
        else:
            print("Такой задачи нет в списке!")
    def remove_task(self, task):
        if task in self.task_list:
            del self.task_list[task]
        else:
            print("Такой задачи нет в списке!")
    def list_tasks(self):
        print("Задачи:")
        for key, value in self.task_list.items():
            print(f"{key}: {value}")


task_list = ToDoList()
task_list.add_task("Сделать уроки")
task_list.complete_task("Сделать уроки")
task_list.remove_task("Запустить программу")
task_list.list_tasks()