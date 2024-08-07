#Все ли равны
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))
if first == second and first != third or first == third and first != second or second == third and second != first:
    print ('2')
elif first == second and first == third:
    print ('3')
else:
    print (0)
