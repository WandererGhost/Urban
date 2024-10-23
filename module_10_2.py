from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy = 100
        count = 0
        while enemy != 0:
            sleep(1)
            enemy -= self.power
            count += 1
            if (count == 1 or count%10 == 1) and count!=11:
                print(f'{self.name} сражается {count} день..., осталось {enemy} врагов\n')
            else:
                print(f'{self.name} сражется {count} дней..., осталось {enemy} врагов\n')
        print(f'{self.name} одержал победу спустя {count} дней\n')


knights = []
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)
knights.append(first_knight)
knights.append(second_knight)

for knight in knights:
    knight.start()

for knight in knights:
    knight.join()

print('Все битвы закончились')

