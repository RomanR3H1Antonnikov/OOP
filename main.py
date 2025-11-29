class ToDoList:
    def __init__(self):
        self.task_list = {"Запустить программу" : "(СДЕЛАНО)"}

    def add_task(self, task):
        self.task_list[task] = "(НЕ СДЕЛАНО)"
        print(f"Задача {task} успешно добавлена!")

    def complete_task(self, task):
        if task in self.task_list:
            self.task_list[task] = "(СДЕЛАНО)"
            print(f"Задача {task} успешно отмечена как выполненная!")
        else:
            print("Такой задачи нет в списке!")

    def remove_task(self, task):
        if task in self.task_list:
            del self.task_list[task]
            print(f"Задача {task} успешно удалена из списка")
        else:
            print("Такой задачи нет в списке!")

    def list_tasks(self):
        print("Задачи:")
        for key, value in self.task_list.items():
            print(f"{key}: {value}")
        print("\n")


def get_valid_input(inpt):
    while True:
        value = input(inpt).strip()
        if value:
            return value
        print("Название задачи не может быть пустым!")


def print_menu(menu_data):
    print("Доступные функции:")
    for key in sorted(menu_data.keys()):
        text, _ = menu_data[key]
        print(f"{key}. {text}")
    print("Введите номер функции: (1 - 5)")


def main():
    todo = ToDoList()
    text_to_write = "Введите название задачи:"
    menu_data = {
        1:("Показать все задачи", lambda: todo.list_tasks()),
        2:("Добавить задачу в список", lambda: todo.add_task(get_valid_input(text_to_write))),
        3:("Отметить задачу выполненной", lambda: todo.complete_task(get_valid_input(text_to_write))),
        4:("Удалить задачу из списка", lambda: todo.remove_task(get_valid_input(text_to_write))),
        5:("Выход", None)
    }
    while True:
        try:
            print("ПОЛЬЗОВАТЕЛЬСКОЕ МЕНЮ")
            print_menu(menu_data)
            command = int(input())

            if command == 5:
                print("До свидания!")
                break
            elif command in menu_data:
                _, action = menu_data[command]
                if action:
                    action()
            else:
                print("Неверная команда!")
        except ValueError:
            print("Команда не введена!")


if __name__ == "__main__":
    main()