#Задача "Нули ничто, отрицание недопустимо!"

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
#my_list = [42, 69, 322, 13, 0, 99, 5, 9, 8, 7, 6, 5] Проверка. Остановится ли цикл по достижении конца списка
length_of_my_list = len(my_list) - 1 #Длина списка считает элементы в списке начиная с 1, а индексация начинается с 0.
#Чтобы программа могла сравнивать длину списка с меняющимся индексом, то нужно привести длину списка к тому же значению, что и последний индекс в списке
tracker = 0
while tracker <= length_of_my_list:
    if my_list[tracker] == 0:
        tracker = tracker + 1
        continue
    elif my_list[tracker] > 0:
        print (my_list[tracker])
        tracker = tracker + 1
        continue
    else:
        break