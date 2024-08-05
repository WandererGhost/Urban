#Задание "Средний балл"

grades = [[5,3,3,5,4], [2,2,2,3], [4,5,5,2], [4,4,3], [5,5,5,4,5]] #Оценки учащихся, размещённые в алфавитном порядке
students = {'Johnny', 'Bilbo', 'Steve', 'Khendric', 'Aaron'} #Неупорядоченное множество учащихся


Average_score = {} #Сюда мы будем закидывать учеников и их средний балл

#Приводи множество (set) students к списку (list)
students = list(students)
#Теперь, если мы выведем тип, к которому относится переменная students, то получим list.
#print (type(students)) #для проверки
print (students)
#У нас есть тип данных, который мы можем отсортировать в алфавитном порядке
students = sorted(students, reverse = False) #Естесственно не вручную
print (students)

# Итак, имена упорядоченны по алфавиту и соответсвуют списку с оценками
# Следующий шаг, найти средний балл каждого ученика и занести всё в словарь

#Итак, первый вариант (на мой взгляд) решения. Практически вручную:
Average_score[students[0]] = sum(grades[0])/len(grades[0])
Average_score[students[1]] = sum(grades[1])/len(grades[1])
Average_score[students[2]] = sum(grades[2])/len(grades[2])
Average_score[students[3]] = sum(grades[3])/len(grades[3])
Average_score[students[4]] = sum(grades[4])/len(grades[4])
print (Average_score)

#Второй вариант, мне он нравится больше и делает всё сам
for i in students:
    Average_score[students[0]] = sum(grades[0])/len(grades[0])
    i = +1
print (Average_score)