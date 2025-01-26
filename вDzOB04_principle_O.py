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
        print("Воин стреляет из лука")

class Fighter:  # создали класс бойца. Если класс ни от чего не насл-ся, скобки м. не писать
    def __init__(self, weapon: Weapon):  # указываем, какой тип д.храниться в переменной
                                         # weapon - там дб объект класса Weapon
                                         # метод init срабатывает, когда мы создаем объект класса
        self.weapon = weapon   # привязываем перем. weapon к классу
    def changeWeapon(self, weapon: Weapon): # еще дб ф-я смены оружия. Будем выбирать тип оружия класса Weapon
        self.weapon = weapon

    def fight(self):  # осталось реализовать возможность воина использовать это оружие
        print(self.weapon.attack()) #у нас уже есть реализация attack в дочерних классах Меч и Лук
                           # в self.weapon хранится конкретное переданное оружие - Меч или Лук

class Monster():
    pass

#Создадим объекты
#Создадим объекты классов
sword1 = Sword()  #об кл Меч
bow1 = Bow()
fighter = Fighter(sword1)  #созд  об кл Бойца и передали ему оружие Меч
fighter.fight()

# Сейчас сменим оружие:
fighter.changeWeapon(bow1)  #заменили на лук
fighter.fight()
