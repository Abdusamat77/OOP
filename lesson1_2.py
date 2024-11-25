# """
# ООП - объектно-ортентированное програмирование
# """
# # def car():
# #     pass


# class Car: #"Шаблон или чертеж"
#     def __init__(self, motor, wheels, body): #__init__ - " конструктор"
#         self.motor = motor # self - ссылка на текущий объект
#         self.wheels = wheels # атрибут класса
#         self.body = body

#         self.bak = 20
#         self.is_start = False #флажок

#     def info(self): #Функция внутри класса превращается в МЕТОД
#         print(f"мотор - {self.motor} колеса - {self.wheels}  кузов - {self.body}")

#     def start(self):
#         if self.bak >0:
#             self.is_start = True
#             print("машина заведена")
#         else:
#             print("у машины нет топлива")
#     def stop(self):
#             self.is_start = False
#             print("машина заглушена")

#     def drive(self,city):
#          if self.is_start == True:
#             print(f"Машина едет в {city}")
#          else:
#             print("Машина не заведена")
# car = Car("v6", "R20", "Khan")# Экземпляр класса


# car.info()
# car.start()
# car.drive("Дубай")

# name = ("asko", "isko", "Sema")
# list_example = list(name)
# list_example.append("aslan")

# print())

class Book:
    def __init__(self, avtor, book_name,year):
        self.avtor=avtor
        self.book_name=book_name
        self.year=year
    def info(self):
        print(f"Автор -{self.avtor}  название -{self.book_name}  год -{self.year} ")

book = Book("Abdusamat", "Backend", "2024")

book.info()