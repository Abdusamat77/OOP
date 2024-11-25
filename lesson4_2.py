# """Полиморфизм"""

# class Cat:
#     def __init__(self, name, preferences):
#         self.name = name
#         self.preferences = preferences
        

#     def info(self):
#         print(f"я кот. Меня зовут {self.name}. мне {self.preferences} года")

#     def make_sound(self):
#         print("Мяу!")

# class Dog:
#     def __init__(self, name, preferences):
#         self.name = name
#         self.preferences = preferences

#     def info(self):
#         print(f"я cобака. Меня зовут {self.name}. мне {self.preferences} года")

#     def make_sound(self):
#         print("Гаф!")

# cat = Cat("васька", 2)
# dog = Dog("Мухтар", 3)

# for animal in (cat,dog):
#     animal.info()
#     animal.make_sound()


# class PaymentMethod:
#     def pay(self, amount):
#         pass

# class CreditCard(PaymentMethod):
#     def pay(self, amount):
#         return f"Cумма {amount}, оплачивается по кредитной карте"
    
# class PayPal(PaymentMethod):
#     def pay(self, amount):
#         return f"Cумма {amount}, оплачивается по PayPal"
    
# class BankTransfer(PaymentMethod):
#     def pay(self, amount):
#         return f"Cумма {amount}, оплачивается по банковскому переводу"
    
# payments = [CreditCard(), PayPal(), BankTransfer()]

# for payment in payments:
#     print(payment.pay(100))


'''Задание: Система оплаты сотрудников

Описание:
Ваша задача — создать систему для расчета зарплаты сотрудников,
 которая демонстрирует абстракцию, наследование и полиморфизм. Не используйте модуль abc, используйте только базовые механизмы Python.

Требования:  
Базовый класс Employee:

Создайте класс Employee с методом calculate_salary(), который возвращает 
нулевую зарплату по умолчанию. Также добавьте метод display_info(), который выводит информацию о сотруднике.
Конструктор класса должен принимать имя сотрудника и его базовую ставку.
Классы-наследники для разных типов сотрудников:

Создайте классы FullTimeEmployee и PartTimeEmployee, которые наследуются от класса Employee.
Для класса FullTimeEmployee метод calculate_salary должен возвращать зарплату как базовую
ставку умноженную на фиксированный коэффициент (например, 1.2).
Для класса PartTimeEmployee метод calculate_salary должен возвращать зарплату как базовую 
ставку умноженную на коэффициент, зависящий от количества отработанных часов (например, базовая ставка умноженная на 0.5 за каждый час).
Использование полиморфизма:

Создайте функцию process_salary(employee), которая принимает объект типа Employee и вызывает его методы calculate_salary и display_info.
Функция должна корректно работать для всех производных классов, демонстрируя полиморфизм.'''


class Employee:
    def __init__(self, name, amount):
        self.name = name 
        self.amount = amount
        
    def display_info(self):
        return f'Имя - {self.name}'
        
    def calculate_salary(self):
        return f'Имя - {self.name}  Зп - {self.amount}'
    
class FullTimeEmployee(Employee):
    def __init__(self, name, amount):
        super().__init__(name, amount)
        
    def calculate_salary(self):
        return f'Имя - {self.name}  Зп - {self.amount * 1.2}'
    
class PartTimeEmployee(Employee):
    def __init__(self, name, amount, time):
        super().__init__(name, amount)
        self.time = time
        
    def calculate_salary(self):
        return f"имя -{self.name} зп - {self.amount* 0.5 * self.time}"
    
    
def process_salary(employee):
    employee.display_info()
    salary = employee.calculate_salary()
    print(f"зп:{salary}")

full_time = FullTimeEmployee("султан", 20000)
part_time = PartTimeEmployee("acлан", 5000, 20)
process_salary(full_time)
process_salary(part_time)
    