import threading
import random
import time

class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100

    def attack(self, other):
        while True:
            time.sleep(random.randint(2,4))
            if self.health <= 0:
                print(f'{other.name} Победил!\n')
                break
            if other.health <= 0:
                break
            other.health -= (random.randint(10,30))
            if other.health<=0:
                other.health = 0
            print(f'{self.name} атаковал, у {other.name} осталось {other.health} очков здоровья')

warrior1 = Warrior('Дима')
warrior2 = Warrior('Филипп')

# Запуск двух потоков
thread1 = threading.Thread(target=warrior1.attack, args=(warrior2,))
thread2 = threading.Thread(target=warrior2.attack, args=(warrior1,))

thread1.start()
thread2.start()