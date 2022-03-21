class Sklenice:
    def __init__(self, objem, tekutina):
        self.objem = objem
        self.tekutina = tekutina
    
    def stavSklenice(self):
        return(f"sklenice obsahuje {self.objem}ml tekutiny {self.tekutina}")

sklenice1 = Sklenice(200, "mléko")
sklenice2 = Sklenice(500, "pivo")

sklenice1.stavSklenice()
sklenice2.stavSklenice()

input()