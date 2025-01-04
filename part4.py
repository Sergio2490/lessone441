#I принцип разделения интерфейсов
# class SmartHouse():  #сначала - как обычно, без использ принципа
#     def turn_on(self):  # ф-я вкл света
#         pass
#     def head_food(self):  #ф-ция разогрев еды
#         pass
#     def turn_on_music(self):  #ф-я вкл музыки
#         pass

class Light():
    def turn_on(self):
        print("Свет включен")
class Food():
    def heat_food(self):
        print("Еда начала разогреваться")

class Music():
    def turn_on_music(self):
        print("Включаю подборку Ваших любимых песен")




