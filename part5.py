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
    @abstractmethod   #декоратор означ, что при создании дочерних классов обяз дб заполнена ф-я get_story()
    def get_story(self):  # ф-я б. пустая, мы ее заполним в следующих наших классах
        pass

class Book(StorySource):  #первый источник историй - книга
    def get_story(self):  #нам надо обяз. заполнить ф-ю get_story(), тк в род. классе у нее стоитpass
        print("Чтение интересной книги")  # декоратор, иначе при создании экз. класса Пайтон выдаст ошибку

class AudioBook(StorySource):  #второй источник историй - аудиокнига
    def get_story(self):
        print("Чтение интересной истории вслух")

class StoryReader(): #ниоткуда не б. брать инф-ю, поэтому ни от чего не наследуется
    def __init__(self, story_source: StorySource):  #сюда мы б. передавать источник инф-ии. Он б. сохр-ся в переменную. Через : указ. тип перем, она б иметь тип StorySource, те она б являться классом
        self.story_source = story_source #привяжем эту х-ку к классу
    def tell_story(self):  # созд ф-ю, к-я б. наши истории читать
        self.story_source.get_story()  #story_source - абстракт класс, наш источник, в нем -
               #конкретный источник - Book или AudioBook, анутри каждого источника есть
               #соответствующая ф-я get_story(), она и б вызываться

book = Book()
audioBook = AudioBook()

readerBook = StoryReader(book)  #созд объект кл StoryReader и передаем в него объект класса Book
readerAudioBook = StoryReader(audioBook)

readerBook.tell_story()
readerAudioBook.tell_story()  # воспроизводим истории из этих соответствующих  источников


