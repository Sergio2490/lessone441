#  L -  Принцип подстановки Барбары Лисков
# class Bird():  #сначала создадим класс, к-й не использует данный метод
#     def __init__(self, name):
#         self.name = name
#
#     def fly(self):  #любая птица класса будет летать
#         print('птица летает')
#
# class Ping(Bird):  #класс Пингвин
#     pass
#
# p = Ping('Сара')
# p.fly()  #вывод: птица летает - но это неправильно!

class Bird():
    def fly(self):
        print("эта птица летает")

class Duck(Bird):
    def fly(self):  #мы могли бы просто написать в ф-ции pass, тогда бы использовалась ф-ция fly() класса Bird
        print("эта утка летает быстро")  #Но мы переопределим ф-цию
        