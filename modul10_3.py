from threading import Thread, Lock
import random
import time


class Bank:
    balance = 0
    lock = Lock()

    def __init__(self):
        pass

    def deposit(self):
        for i in range(100):
            add = random.randint(50, 500)
            self.balance = self.balance + add
            print(f'Пополнение: {add}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)


    def take(self):
        for i in range(100):
            take_ = random.randint(50, 500)
            print(f'Запрос на {take_}')
            if take_ <= self.balance:
                self.balance = self.balance - take_
                print(f'Снятие {take_}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
