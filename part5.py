#D - принцип инверсии зависимости
# сначала созд класс, к-й не использ д-й принцип
# class Book():
#     def read(self):
#         print("Чтение интересной истории")
#
# class StoryReader():
#     def __init__(self):
#         self.book = Book()  # мы создали объект класса Book.
#
#     def tell_story(self):
#         self.book.read()  #мы используем ф-ю read() из класса Book. Те, сейчас класс StoryReader
#                         # сильно зависит от класса Book/ А так быть не должно!

from abc import ABC, abstractmethod  # подключаем возм-ть работы с абстрактными методами
class StorySource(ABC): # абстракт класс, наследуется от ABC
    @abstractmethod
    def get_store(self):  # ф-я б. пустая, мы ее заполним в следующих наших классах
        pass

