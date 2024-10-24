import multiprocessing
from datetime import datetime as dt


def read_info(name):
    all_data = []
    with open(f'{name}', 'r', encoding='utf-8') as file:
        for line in file:
            all_data.append(line.strip())


file_name = [f'./file {number}.txt' for number in range(1,5)]


#  Линейный вызов
start_time = dt.now()

for fn in file_name:
    read_info(fn)
    
end_time = dt.now()
print(f'Линейный вызов: {end_time-start_time}')

#  Многопроцессорный
if __name__ == '__main__':
    with multiprocessing.Pool(processes=len(file_name)) as pool:
        start_time = dt.now()
        pool.map(read_info, file_name)
    end_time = dt.now()
    print(f'Многопроцессорный вызов: {end_time-start_time}')
