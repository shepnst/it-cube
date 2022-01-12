# -*- coding: utf-8 -*-
from random import*
class Warrior:
    def __init__(self, hp=100, ap=10, ag =50, ar = 100):
        self.health = randint(0, hp)
        self.attack = randint(0, ap)
        self.agility =randint(0, ag)
        self.armor = randint(0, ar)
        

class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.attack = randint(0,7)

class Samurai(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.agility = 50
        self.attack(0, ap)

def fight(fighter1, fighter2):
    while True:
        fighter2.health -= fighter1.attack*(fighter1.agility//randint(1,100)+1)
        if fighter2.health <= 0:
            return(True)
        fighter1.health -= fighter2.attack*(fighter2.agility//randint(1,100)+1)
        if fighter1.health <= 0:
            return(False)


Vasya = Warrior()
Petya = Knight()
print(fight(Vasya, Petya))