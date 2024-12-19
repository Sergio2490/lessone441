# Сначала - как мы не должны делать. То есть, без использования 2-го принципа open/closed

# class Report():   #класс б. обрабат-ть данные и выводить отчеты
#     def __init__(self, title, content):  # ф-я иниц-уии.У нашего отчета(док-та) будет заголовок и контент
#         self.title = title    #все эти хар-ки привязываем к классу
#         self.content = content
#
#     def docPrinter(self):
#         print(f"Сформирован отчет - {self.title} - {self.content}")
# Это - обычный класс. Закомментируем все что написали выше


from abc import ABC, abstractmethod   # Модуль для работы с абстрактными классами:
class Formatted(ABC):   #наследуем класс от абстракции
    @abstractmethod   #это декоратор, ко-й прописываем перед функцией, к которой он будет применен
    def format(self, report):
        pass   #мы создали абстрактный класс, внутри к-го есть абстракт.метод, сейчас он пустой = шаблон

class TextFormatted(Formatted):  #сначала создадим класс, к-й б. раб. с обычным текстом
    def format(self, report):
        print()
        print()

class HtmlFormatted(Formatted):  #класс б. преобразовывать текст в html
    def format(self, report):
        print()
        print()

class Report():  #класс, где б. вноситься вся инфоромация
