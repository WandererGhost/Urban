def get_matrix (n,m, value):
    matrix = []
    for stroka in range (n):
        matrix.append ([])
        for stolbes in range (0, m):
            matrix[stroka].append (value)
        
    return matrix

n = int(input('Введите количество строк: '))
m = int(input('Введите количество столбцов: '))
value = int(input('Введите значение, которым всё заполнится: '))
result = get_matrix(n,m,value)
print (result)