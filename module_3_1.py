calls = 0
string = '0'
list_to_search = ['0']
def count_calls(): # Счётчик
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    a = len(string)
    b = string.upper()
    c = string.lower()
    result = [a, b, c]
    result = tuple(result)
    return result

def is_contains (string, list_to_search):
    count_calls()
    my_str = string.lower()
    my_list = list_to_search
    for item in my_list:
        item.lower
    result = my_str in my_list
    return result
    
print (string_info('газированный сахар'))
print (is_contains('Путь', ['дорога', 'rOAd', 'игРа', 'ПУТЬ ВЕТРА']))
print (is_contains('ПуТЬ', ['дорога', 'rOAd', 'игРа', 'ПУТЬ ВЕТРА', 'путь']))
print (is_contains('Скоро', ['Скоро', 'можно', 'будет', 'пойти']))
print (string_info('Варежка'))
print (string_info('Mura'))

print (calls)