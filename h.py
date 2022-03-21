import math

class Trojuhelník:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def Plocha(self):
        print((self.a*self.b)/2)

    def stranaC(self):
        print(math.sqrt(self.a*self.a + self.b*self.b))

t1 = Trojuhelník(2, 3)
t2 = Trojuhelník(24, 60)
t3 = Trojuhelník(3243, 2313)

t1.Plocha()
t2.Plocha()
t3.Plocha()

t1.stranaC()
t2.stranaC()
t3.stranaC()

