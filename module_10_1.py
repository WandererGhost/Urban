from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'a', encoding='utf-8') as file:
        for count in range(1, word_count+1):
            sleep(0.1)
            file.write(f'Какое-то слово № {count}\n')
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
print(f'Работа потоков {time_end - time_start}')

time_start_ = datetime.now()

thr_write1 = Thread(target=write_words, args=(10, 'example5.txt'))
thr_write2 = Thread(target=write_words, args=(30, 'example6.txt'))
thr_write3 = Thread(target=write_words, args=(200, 'example7.txt'))
thr_write4 = Thread(target=write_words, args=(100, 'example8.txt'))

thr_write1.start()
thr_write2.start()
thr_write3.start()
thr_write4.start()

thr_write1.join()
thr_write2.join()
thr_write3.join()
thr_write4.join()

time_end_ = datetime.now()
print(f'Работа потоков {time_end_ - time_start_}')
