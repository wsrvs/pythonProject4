# Запрашиваем элементы списка через запятую, точку с запятой или слэш
input_str = input("Введите элементы списка через запятую, точку с запятой или слэш: ")

# Определяем разделитель
if "," in input_str:
    separator = ","
elif ";" in input_str:
    separator = ";"
elif "/" in input_str:
    separator = "/"
else:
    print("Неверный формат ввода. Используйте запятую, точку с запятой или слэш в качестве разделителя.")
    exit()

# Проверяем, что в строке ввода использован только один разделитель
if input_str.count(separator) != len(input_str.split(separator)) - 1:
    print("Неверный формат ввода. Используйте только один разделитель.")
    exit()

# Создаем список из введенных элементов
numbers = [int(x) for x in input_str.split(separator)]

# Создаем новый список с уникальными элементами
unique_numbers = [x for x in numbers if numbers.count(x) == 1]

# Выводим новый список
print(unique_numbers)
