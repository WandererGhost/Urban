data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(data):
    sum_data = 0
    for i in data:
        if isinstance(i, list):
            sum_data += calculate_structure_sum(i)
        if isinstance(i, tuple):
            sum_data += calculate_structure_sum(i)
        if isinstance(i, dict):
            sum_data += calculate_structure_sum(i.items())
        if isinstance(i, set):
            sum_data += calculate_structure_sum(i)
        if isinstance(i, str):
            sum_data += len(i)
        if isinstance(i, int):
            sum_data += i
#    for element in data:
#        if isinstance(element, list):
#            sum_data += calculate_structure_sum(element)
#        else:
#            sum_data += element

    return sum_data

result = calculate_structure_sum (data_structure)
print(result)