# -*- coding: utf-8 -*-
class Hero:
    def __init__(self, name, hp=100):
        self.health = hp
        self.name = name 

class Warrior(Hero):
    def __init__(self, name, hp=100, ap = 10, ag = 50):
       super().__init__(name, hp)
       self.attack = ap
       self.agility = ag
       
    def fight(self, s):
        s.health -= self.attack
        print(self.name, 'ударил', s.name, 'на', self.attack)
        
        
class Knight(Warrior):
    def __init__(self, name, hp=100, ap = 10, ag = 50):
        super().__init__(name, hp, ap, ag)
        self.health = hp+20
    
    def fight(self, d):
        d.health -= self.agility
        print(self.name, 'напал на', d.name, 'на', self.agility)
   
        
class Ranger(Warrior):
    def __init__(self, name, hp=100, ap = 10, ag = 50):
       super().__init__(self, name, hp, ap, ag)
        self.agility = hp-20
        self.attack = ap+5
        

      
class Wizard(Hero):
    def __init__(self, name, mn = 12, hp = 100):
        super().__init__(name, mn, hp)
        self.manna = mn
    
        
        
'''        
class Heeler(Wizard):
    def __init__(self, ):
        
class Gandalf(Wizard):
    def __init__(self, ):
'''
Vasya = Knight(name='Вася')
Petya = Warrior(name = 'Петя')
Vasya.fight(Petya)
Petya.fight(Vasya)
