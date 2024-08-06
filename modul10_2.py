from threading import Thread
from time import sleep


class Knight(Thread):

    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy = 100
        day = 0
        while enemy > 0:
            enemy = enemy - self.power
            day += 1
            print(f'{self.name} сражается {day} дней(дня), осталось {enemy} войнов')
            sleep(1)
        print(f'{self.name}одержал победу спустя {day} дней(дня)')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
knights = [first_knight, second_knight]
for i in knights:
    i.start()

for i in knights:
    i.join()

print('Все битвы закончились!')
