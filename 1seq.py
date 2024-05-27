# Запрашиваем количество элементов
num_elements = int(input("Введите количество элементов: "))

# Создаем пустой список
numbers = []

# Последовательно вводим элементы и добавляем их в список
for i in range(num_elements):
    num = int(input(f"Введите {i+1} элемент: "))
    numbers.append(num)

# Сортируем список по возрастанию
numbers.sort()

# Выводим отсортированный список
print(numbers)