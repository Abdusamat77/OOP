""" 
ООП - объектно-ортентированное програмирование
"наследование"
"""

# class Game: # Родительский класс
#     def __init__(self,game_name, game_year, company,graphics):
#         self.game_name = game_name
#         self.game_year = game_year
#         self.company = company
#         self.graphics = graphics   

#     def info(self):
#         print(f"game - {self.game_name} - {self.game_year} - {self.company} - {self.graphics}")

# # game = Game("CsGo2", "2009", "Valve", "4k")
# # game.info()

# class Roblox(Game):
#     def  __init__(self, game_name, game_year, company, graphics, multiplayer):
#         # super().__init__(game_name, game_year, company, graphics)
#         Game.__init__(self, game_name,game_year, company, graphics)
#         self.multiplayer = multiplayer
#         self.name = "Player"
#         self.gender = "none"
#         self.skin = "none"
#         self.hp = 100

#     def info(self):
#         print(f"game - {self.game_name} - {self.game_year} - {self.company} - {self.graphics} - {self.multiplayer}")
    
#     def info_player(self):
#         print(f"Игрок - {self.name}  - {self.gender} - {self.skin} - {self.hp}HP")

#     def edit_player(self):
#         name = input('Введите имя игрока: ')
#         gender = input("Введите пол для игрока: ")
#         skin = input("Введите облик игрока: ")
#         self.name = name
#         self.gender = gender
#         self.skin = skin

# roblox = Roblox("Roblox", 2006, "Roblox Corp.", "ultra", 'yes' )
# roblox.info()
# roblox.edit_player()
# roblox.info_player()


# class Strike(Roblox):
#     def __init__(self, game_name, game_year, company, graphics, multiplayer):
#         super().__init__(game_name, game_year, company, graphics, multiplayer)

# class Animal:
#     def __init__(self,name):
#         self.name = name
    
#     def eat(self):
#         print(f"{self.name} ест")

#     def sleep(self):
#         print(f"{self.name} спит")

# walk = Animal("гориллф")
# swim = Animal('рыба')



# class Walker():
#     def __init__(self,goril):
#         self.goril = goril
#     def walk(self):
#         print(f" {self.goril} ходит")
# walke = Walker("гориллa")
# walke.walk()

# class Swimmer():
#     def swim(self):
#         print(f"{self.name} плавает")

# class Flyer():
#     def fly(self):
#         print(f"{self.name}плавает")

# class Penguin(Animal, Walker, Swimmer):
#     def describe(self):
#         print(f"{self.name} может плавать и ходить")
        
class A:
    def show(self):
        print("A")
class B(A):
    def show(self):
        print("B")
class C(A):
    def show(self):
        print("c")
class D(B, C):
    pass
d = D()
d. show()