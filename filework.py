with open("data.txt", "r") as test_file:
    print(f"Полное содержимое файла:\n{test_file.read()}")


with open("data.txt", "a") as test_file:
    test_file.write("\nExtra_line 11223344")


with open("data.txt", "r") as test_file:
    print("\nПострочный вывод файла:")
    for line_number, line in enumerate(test_file):
        print(f"Строка номер {line_number + 1}: {line.strip()}")


with open('data.txt', 'rb') as test_file:
    with open("data_copy.txt", "wb") as temp_file:
        temp_file.write(test_file.read())