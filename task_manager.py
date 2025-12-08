import json


class TaskManager:
    def __init__(self):
        self.task_list = []


    def add_task(self, description: str):
        new_task = {
            "description": description,
            "completed": False
        }
        self.task_list.append(new_task)
        print(f"Задача '{description}' успешно добавлена!")


    def complete_task(self, index: int):
        if 0 <= index < len(self.task_list):
            self.task_list[index]["completed"] = True
            print(f"Задача '{self.task_list[index]["description"]}' успешно отмечена как выполненная")
        else:
            print("Такой задачи нет в списке или индекс указан неверно")


    def remove_task(self, index: int):
        if 0 <= index < len(self.task_list):
            removed_task = self.task_list.pop(index)["description"]
            print(f"Задача '{removed_task}' успешно удалена!")
        else:
            print("Такой задачи нет в списке или индекс указан неверно")


    def save_to_json(self, filename: str):
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(self.task_list, file, indent=4, ensure_ascii=False)


    def load_from_json(self, filename: str):
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.task_list = json.load(file)
        except json.JSONDecodeError as e:
            print(f"Ошибка при разборе JSON: {e}")
        except FileNotFoundError:
            print(f"Файл с названием {filename} не найден!")