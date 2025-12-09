from task_manager import TaskManager


def test_add_and_complete_task():
    my_list = TaskManager()
    my_list.add_task("Завершить модуль Python на курсе")

    assert len(my_list.task_list) == 1
    assert my_list.task_list[0]["description"] == "Завершить модуль Python на курсе"
    assert my_list.task_list[0]["completed"] == False

    my_list.complete_task(0)

    assert my_list.task_list[0]["completed"] == True


def test_remove_task():
    my_test_list = TaskManager()
    my_test_list.add_task("Тестовая задача 1")
    my_test_list.add_task("Тестовая задача 2")
    my_test_list.complete_task(0)
    my_test_list.remove_task(0)

    assert len(my_test_list.task_list) == 1
    assert my_test_list.task_list[0]["description"] == "Тестовая задача 2"


def test_save_and_load_via_json():
    list_1 = TaskManager()
    list_1.add_task("Простая тестовая задача")
    list_1.complete_task(0)
    list_1.save_to_json("json_task_list_temp.json")

    list_2 = TaskManager()
    list_2.load_from_json("json_task_list_temp.json")

    assert len(list_2.task_list) == 1
    assert list_2.task_list[0]["description"] == "Простая тестовая задача"
    assert list_2.task_list[0]["completed"] == True


if __name__ == "__main__":
    try:
        test_add_and_complete_task()
        print("Тест 1 - прошёл проверку!")
    except AssertionError as e:
        print(f"Тест 1 не пройден: {e}")
    try:
        test_remove_task()
        print("Тест 2 - прошёл проверку!")
    except AssertionError as e:
        print(f"Тест 2 не пройден: {e}")
    try:
        test_save_and_load_via_json()
        print("Тест 3 - прошёл проверку!")
    except AssertionError as e:
        print(f"Тест 3 не пройден: {e}")