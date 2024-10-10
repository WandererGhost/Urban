def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    valid_count = 0  # Счетчик корректных чисел
    for num in numbers:
        try:
            result += num
            valid_count += 1  # Увеличиваем счетчик корректных чисел
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {num}')
    return result, valid_count, incorrect_data  # Возвращаем также количество корректных чисел
    

def calculate_average(numbers):
    if not isinstance(numbers, (list, tuple)):  # Проверяем, является ли входной параметр коллекцией
        print(f'В numbers записан некорректный тип данных')
        return None

    sum_collect, valid_count, incorrect_data = personal_sum(numbers)
    
    if valid_count == 0:  # Проверяем, есть ли корректные числа
        print(f'Нет корректных чисел для вычисления среднего.')
        return None
    
    average = sum_collect / valid_count  # Делим на количество корректных чисел
    return average


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Некорректный тип данных
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать