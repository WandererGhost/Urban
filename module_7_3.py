with open('test_file.txt', 'w', encoding='utf-8') as test:
    test.write("It's a text for task Найти везде,\n")
    test.write('Используйте его для самопроверки.\n')
    test.write('Успехов в рещении задачи!\n')
    test.write('text text text\n')

with open('test_file_2.txt', 'w', encoding='utf-8') as test2:
    test2.write('Сработает или нет?!\n')
    test2.write('There is a text. Maybe...\n')
    test2.write('Должен создаться: второй элемент словаря! Надеюсь\n')


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        import string
        all_words = {}
        translator = str.maketrans('', '', string.punctuation)
        for file_word in self.file_names:
            with open(file_word, 'r', encoding='utf-8') as file:
                now_read = file.read().lower()
            now_read = now_read.translate(translator)
            all_words[file_word] = now_read.split()
        return all_words

    def find(self, find_word):
        finder = {}
        index = -1
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if words[i] == find_word.lower():
                    index = i + 1
                    finder[name] = index
                    break
        return finder

    def count(self, count_word):
        counter = {}
        count = 0
        for name, words in self.get_all_words().items():
            for word in words:
                if word == count_word.lower():
                    count += 1
            counter[name] = count
            count = 0
        return counter


finder2 = WordsFinder('test_file.txt', 'test_file_2.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# Для проверки корректной работы добавлен второй текстовый файл.
# Правильные значения: find = 7, count = 1
