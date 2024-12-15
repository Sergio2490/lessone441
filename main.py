# OB04 Пример принципа S
#class UserManager():
    # def __init__(self, user):   #ф-я init() - чт. м.б. создавать объекты этого класса
    #     self.user = user    # привязываем это хар-ку к классу
    # def change_user_name(self, user_name):   #ф-я позволяет изменять инф. о польз-ле в классе
    #     self.user = user_name  #сразу сохр имя, переданное в атрибуте, в self.user
    #
    # def save_user(self):  #ф-я будет сохранять инф. о польз-ле в файл
    #     file = open("users.txt", "a")  #открываем файл для записи? a - б. доб. в него инф-ю
    #     file.write(self.user)  #записываем инф. о польз-ле
    #    file.close()  #закрываем файл
# Т.о. мы создали класс с неединственной ответственнойстью - 1) создаем нов. польз-ля и
#    2) сохряняем  инф. о польз-ле в файл. Как сделать правильно:
class User():  # класс для создания пользователя
    def __init__(self, user):  # ф-ция для ввода пользователя
        self.user = user  # привязываем хар-ку (пользователя) к классу
class UserNameChanger():   # у каждого класса дб своя единственная ответственность
    def __init__(self, user):
        self.user = user
    def change_name(self,new_name):  #ф-ция для изменения имени пользователя
        self.user = new_name

class SaveUser():  # класс для сохраниения информации о пользователе в файл
    def __init__(self, user):
        self.user = user

    def save(self):
        file = open("users.txt", "a")  #открываем файл для записи? a - б. доб. в него инф-ю
        file.write(self.user)  #записываем инф. о польз-ле
        file.close()  #закрываем файл




