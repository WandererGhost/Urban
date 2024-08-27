def print_params(a={'key': 'count'}, b='Варежка', c=True):
    print(a, b, c)


print_params()
print_params(a=15)
print_params(b=False)
print_params(c=[('h','i'), 101010, ['i', 's'], True, {'my':'program'}])

values_list = [18, 'Тевирп', ('t', 'u', 'p', 1, 'e')]
values_dict = {'a': 48, 'b':'I', 'c':False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ('Апельсин', 26)
values_list_3 = ['Крот']
print_params(*values_list_2, ['c', 'a', 't3'])
print_params(*values_list_3, 56) #Третий параметр выведен по умолчанию
