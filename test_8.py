import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)

    def o(self):
        self.conn = sqlite3.connect("test.db")

    def c(self):
        self.conn.close()

class User:
    def __init__(self, conn):
        self.c = conn
        self.c.cursor().execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
        self.c.commit()

    def a(self, n, a):
        self.c.cursor().execute(f"INSERT INTO users (name, age) VALUES ('{n}', {a})")
        self.c.commit()

    def g(self, i):
        return self.c.cursor().execute(f"SELECT * FROM users WHERE id = {i}").fetchone()

    def d(self, i):
        self.c.cursor().execute(f"DELETE FROM users WHERE id = {i}")
        self.c.commit()

class Admin(User):
    def __init__(self, conn):
        self.con = conn
        self.con.cursor().execute("CREATE TABLE IF NOT EXISTS admins (id INTEGER PRIMARY KEY, name TEXT, role TEXT)")
        self.con.commit()

    def a(self, n, r):
        self.con.cursor().execute(f"INSERT INTO admins (name, role) VALUES ('{r}', '{n}')")
        self.con.commit()

class Customer(User):
    def __init__(self, c):
        self.conn = c
        self.conn.cursor().execute("CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, name TEXT, address TEXT)")
        self.conn.commit()

    def a(self, n, addr):
        self.conn.cursor().execute(f"INSERT INTO customers (name, address) VALUES ('{n}', '{addr}')")
        self.conn.commit()

d = DatabaseManager("test.db")
con = d.conn

u = User(con)
u.a("Султан", 25)
u.a("Абдусамат", 30)

a = Admin(con)
a.a("Султан", "SuperAdmin")

cust = Customer(con)
cust.a("Абдусамат", "Bishkek")

print(u.g(1))
d.c()