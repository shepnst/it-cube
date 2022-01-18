# -*- coding: utf-8 -*-
class Hero:
    def __init__(self, hp=100):
        self.health = randint(0, hp)

class Warrior(Hero):
    def __init__(self, name, hp=100, ap = 10, ag = 50):
       seper() __init__(name, hp)
       self.attack = ap
       self.agility = ag
        
        
class Knight(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.health = hp+20
        
class Ranger(Warrior):
    def __init__(self):
        Warrior.__init__(self)
        self.agility = hp-20
        self.attack = ap+5
        
class Wizard(Hero):
    def __init__(self, manna):
        self.manna = manna
        
class Heeler(Wizard):
    def __init__(self, )