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
        print("Задачи:\n")
        for key, value in self.task_list.items():
            print(f"{key}: {value}")


def show_menu():
    print("ПОЛЬЗОВАТЕЛЬСКОЕ МЕНЮ\n")
    print("1. Показать все задачи")
    print("2. Добавить задачу в список")
    print("3. Отметить задачу выполненной")
    print("4. Удалить задачу из списка")
    print("5. Выход")


def main():
    todo = ToDoList()

    while True:
        show_menu()
        command = input("\nВыберите действие (1-5): \n").strip()

        if command == "1":
            todo.list_tasks()
        elif command == "2":
            task = input("Введите новую задачу:\n").strip()
            if task:
                todo.add_task(task)
            else:
                print("Нельзя добавить пустую задачу!")
        elif command == "3":
            todo.list_tasks()
            if todo.task_list:
                task = input("Введите задачу, которую хотите отметить выполненной:\n").strip()
                todo.complete_task(task)
        elif command == "4":
            todo.list_tasks()
            if todo.task_list:
                task = input("Введите задачу, которую хотите удалить из списка:\n").strip()
                todo.remove_task(task)
        elif command == "5":
            print("До свидания!")
            break
        else:
            print("Неправильный выбор! Введите число от 1 до 5.")


if __name__ == "__main__":
    main()