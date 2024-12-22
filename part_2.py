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
        print(report.title)  #черезэтот объект клсса выводим Заголовок
        print(report.content)

class HtmlFormatted(Formatted):  #класс б. преобразовывать текст в html
    def format(self, report):
        print(f"<h1>{report.title}</h1>")  #h1 - тэг заголовка, он двойной
        print(f"<p>{report.content}</p>")  #p - тэг параграфа, это обычный текст

class Report():  #класс, где б. вноситься вся инфоромация
    def __init__(self, title, content, formatted):
        self.title = title  #привязка хар-к к классу
        self.content = content
        self.formatted = formatted   #указываем здесь класс, к-1 нужно использовать, те будем создавать
                               #объект класса , к-й б. передаваться в аргумент formatted класса Report
    def docPrinter(self):
        self.formatted.format(self)  #прописываем вызов ф-ции format() у нашей хар-ки formatted

#Все классы готовы
report = Report("заголовок отчета", "это текст отчета, его тут много", TextFormatted())
        #указываем тут (3-й арг-нт) класс, к-й нужно использовать, те создаем объект класса, к-1 б.
        # сохранятьсяв formatted (3-q fhu a-wbb штше rkfccf Кузщке
# А сейчас используем объект класса report в ф-ции format (print) классов TextFormatted и HtmlFormatted

report.docPrinter()  #мы вызываем ф-ю docPrinterЮ но она берет ф-цию format() того класса,
           #к-й у нас прописан в formatted. Сейчас там прописан TextFormatted


