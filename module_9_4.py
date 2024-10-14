#  Первая часть задания: lambda-функции
first = 'Мама мыла раму'
second = 'Рамена мало было'
l_result = list(map(lambda x, y: x == y, first, second))

# Вторая часть задания:
def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a', encoding='utf-8') as f:
            for data in data_set:
                f.write(str(data) + '\n')
    return write_everything


# Третья часть задания:
class MysticBall:
    from random import choice
    
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)