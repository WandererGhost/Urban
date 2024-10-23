from threading import Thread, Lock
from random import randint
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = Lock()


    def deposit(self):
        for time in range(101):
            dep = randint(50,500)
            self.balance += dep
            print(f'Пополнение: {dep}. Баланс: {self.balance}')
            sleep(0.001)
        return self.balance

    def take(self):
        for _ in range(101):
            req = randint(50, 500)
            print(f'Запрос на {req}')
            with self.lock:
                if req <= self.balance:
                    self.balance -= req
                    print(f'Снято: {req}. Баланс: {self.balance}')
                else:
                    print('Запрос отклонён, недостаточно средств')
            sleep(0.001)


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk, ))
th2 = Thread(target=Bank.take, args=(bk, ))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
