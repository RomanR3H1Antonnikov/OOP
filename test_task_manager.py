from task_manager import TaskManager

my_list = TaskManager()
my_list.add_task("Завершить модуль Python на курсе")
my_list.complete_task(0)
my_list.save_to_json("json_task_list_temp_1")
my_list.remove_task(0)
my_list.save_to_json("json_task_list_temp_2")
my_list.load_from_json("json_task_list_temp_1")
my_list.save_to_json("json_final_result")