""" БД - База данных """ 
""" СУБД - Система управления БД """ 
""" CRUD - CREATE, RETRIVE, UPDATE, DELETE """ 
 
import sqlite3 
 
connect = sqlite3.connect('geeks.db') 
cursor = connect.cursor() 
 
cursor.execute(""" 
    CREATE TABLE IF NOT EXISTS users( 
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        full_name VARCHAR (30) NOT NULL, 
        age INT DEFAULT NULL, 
        direction TEXT, 
        is_have BOOLEAN NOT NULL DEFAULT FALSE, 
        rating DOUBLE (4,2) DEFAULT (0.0), 
        birth_day DATE 
    ) 
""") 
 
def register(): 
    full_name = input("Введите ФИО: ") 
    age = int(input("Введите возраст: ")) 
    direction = input("Введите направление: ") 
    is_have = bool(input("Наличие ноутбука: ")) 
    rating = float(input("Введите свой рейтинг: ")) 
    birth_date = input("Введите дату рождения: ")

    cursor.execute(f""" ISERT INTO users
                   (full_name, age, direction, is_have, 
                   rating, birth_day)
                   VALUES ('{full_name}', {age}, '{direction}',
                   {is_have}, {rating}, '{birth_date}')""")

    connect.commit()

def all_students():
    cursor.execute("SELECT * FROM users")
    studets = cursor.fetchall()
    print(studets)

# register()    
all_students()