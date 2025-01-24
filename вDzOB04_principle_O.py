#ДЗ OB04_SOLID
from abc import ABC, abstractmethod #модуль для работы с абстрактными классами:
class Weapon(ABC):  #абстрактный класс оружия
    @abstractmethod
    def attack(self):  # абстракт (пустой) метод, од дб реализован уже в дочерних классах
        pass
class Sword(Weapon):  # создали класс Меч
    def attack(self):
        print("Воин рубит мечом")
class Bow(Weapon):  # создали класс Лук
    def attack(self):
        print("Воин стрелт из лука")

class Fighter:  # создали класс бойца. Если класс ни от чего не насл-ся, скобки м. не писать
    def __init__(self, weapon: Weapon):  # указываем, какой тип д.храниться в переменной
                                         # weapon - там дб объект класса Weapon
                                         # метод init срабатывает, когда мы создаем объект класса
        self.weapon = weapon   # привязываем перем. weapon к классу
    def changeWeapon(self, weapon: Weapon): # еще дб ф-я смены оружия. Будем выбирать тип оружия класса Weapon
        self.weapon = weapon

