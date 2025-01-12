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
    @abstractmethod   #декоратор означ, что при создании дочерних классов обяз дб заполнена ф-яgrt_store()
    def get_store(self):  # ф-я б. пустая, мы ее заполним в следующих наших классах
        pass

class Book(StorySource):  #первый источник историй - книга
    def get_store(self):  #нам надо обяз. заполнить ф-ю get_store(), тк в род. классе у нее стоит
        print("Чтение интересной книги")  # декоратор, иначе при создании экз. класса Пайтон выдаст ошибку

class AudioBook(StorySource):  #второй источник историй - аудиокнига
    def get_store(self):
        print("Чтение интересной истории вслух")

class StoryReader(): #ниоткуда не б. брать инф-ю, поэтому ни от чего не наследуется
    def __init__(self, story_source: StorySource):  #сюда мы б. передавать источник инф-ии. Он б. сохр-ся в переменную. Через : указ. тип перем, она б иметь тип StorySource, те она б являться классом
        self.story_source = story_source #привяжем эту х-ку к классу
    def tell_story(self):  # созд ф-ю, к-я б. наши истории читать
        



