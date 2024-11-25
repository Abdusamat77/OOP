"""OOП - объектно ориентированное программирование
"Инкапсуляция"
1) публичный
2) защищенный
3) приватный
"""

# class PublicExample: # публичный класс
#     def __init__(self,value):
#         self.value = value #публичный атрибут

#     def info(self):
#         return self.value #публичный метод
    
# public = PublicExample(23)
# print(public.info())#вызов публичного метода
# print(public.value)# доступ к публичному атрибуту

# class ProtectedExample: #защищенный класс
#     def __init__(self,value):
#         self._value = value #защищенный атрибут

    
#     def _info(self):
#         return self._value #защищенный метод
        


# protected = ProtectedExample(43)

# print(protected._info())#Это работает, но противоречит принципам инкапсуляции
# print(protected._value)#Можно получить значение напрямую, но тоже не рекамендуется

# class PrivateExample:#приватный класс
#     def __init__(self, value):
#         self.__value = value #приватный атрибут  

#     def __info(self):#публичный метод, где мы получаем доступ к приватному методу
#         return self.__value
    
#     def access_private(self):
#         return self.__info()

# privat = PrivateExample(12)
# # print(privat.__info()) #Прямой вызов приватного метода вызовет ошибку

# # print(privat.__value) #прямой вызов прямого атрибута тоже вызовет ошибку 

# # print(privat.access_private())#Доступ через публичный метод

# print(privat._PrivateExample__info

import datetime

class Car:
    def __init__(self, marka, model, year, mileage):
        self.marka = marka
        self.model = model
        self._year = year
        self.__mileage = mileage

    def info(self):
        return f"Марка - {self.marka}\nМодель - { self.model}"

    def _calculate_age(self):
        current = datetime.datetime.now().year
        return f'Возраст машины - {current - self._year}'
    
    def __update_mileage(self, mileage_update = 1000):
        self.__mileage = mileage_update
        return self.__mileage
    
    def set_mileage(self):
        return self.__update_mileage
    
car = Car("Mazda", "Demio", 2008, 140000)

print(car.info())
print(car._calculate_age())
print(car.__update_mileage())
print(car.set_mileage())