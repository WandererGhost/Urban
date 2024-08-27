#Неизменяемые объекты
immutable_var = (23, 'Cat', 11.3, True, ['Apple', 'Dog', 'Bird'])

print ('immutable_var: ',immutable_var)

#immutable_var[0] = 13
#immutable_var[1] = 4
#immutable_var[2] = 'Snake'
#immutable_var[3] = False

#Данные оставлены, однако попытка запустить хоть одну из строчек, что находится в комментариях
#вызовет ошибку, т.к. кортеж не позволяет менять данные, которые в него входят.

#Одна строчка осталась незакомментрированной. Её тип нельзя изменить, это всё так же будет список.
#Но этот список внутри кортежа можно подправить

immutable_var[4][1] = 15
print ('immutable_var: ',immutable_var)
print ('\n')
#Изменяемые объекты
mutable_list = ['Song', 'Earth', 'Shadow', 8, 15.3, [1,2,3]]
print ('mutable_list: ',mutable_list)
#Тип данных list поддаётся изменениям, поэтому...
mutable_list.remove([1,2,3])
mutable_list[0] = 'Road'
mutable_list.append('89')

print ('New_mutable_list: ', mutable_list)
#Получается, что список (list) остаётся изменяемым даже находясь внутри неизменяемого типа данных :)


