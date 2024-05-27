# Ввод элементов первого списка
input_str1 = input("Введите элементы 1-го списка: ")

# Определение разделителя
if "," in input_str1:
    separator1 = ","
elif ";" in input_str1:
    separator1 = ";"
elif "/" in input_str1:
    separator1 = "/"
else:
    print("Неверный формат ввода. Используйте запятую, точку с запятой или слэш в качестве разделителя.")
    exit()

# Создание списка из элементов первого списка
list1 = [int(x) for x in input_str1.split(separator1)]

# Ввод элементов второго списка
input_str2 = input("Введите элементы 2-го списка: ")

# Определение разделителя
if "," in input_str2:
    separator2 = ","
elif ";" in input_str2:
    separator2 = ";"
elif "/" in input_str2:
    separator2 = "/"
else:
    print("Неверный формат ввода. Используйте запятую, точку с запятой или слэш в качестве разделителя.")
    exit()

# Создание списка из элементов второго списка
list2 = [int(x) for x in input_str2.split(separator2)]

# Удаление элементов второго списка из первого
list1 = [x for x in list1 if x not in list2]

# Вывод результата
print("Результат:", ", ".join(map(str, list1)))
