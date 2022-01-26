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
       
    def fight(self, enemy):
        attack = self.attack*(1+randint(0, self.agility))
            enemy.health -= attack
            if isinstance()
            print(self.name, 'ударил', s.name, 'на', self.attack)
        
class Knight(Warrior):
    def __init__(self, name, hp=100, ap = 10, ag = 50):
        super().__init__(name, hp, ap, ag)
        self.health = hp+20
        
class Ranger(Warrior):
    def __init__(self, name, hp=100, ap = 10, ag = 50):
       super().__init__(self, name, hp, ap, ag)
        self.agility = hp-20
        self.attack = ap+5
        
def fighting():
    while len(s)>1:
        a = choice(s)
        b = choice(s)
        if a==b:
            print(a.name, 'наступил себе на ногу')
            continue
        a.fight(b)
        if b.health<=0:
            s.remove(b)
            print(b.name, 'убит!')
    print(s[0].__dict__)
    
    
players = [Knight('Маша')]
'''
      
class Wizard(Hero):
    def __init__(self, name, mn = 12, hp = 100):
        super().__init__(name, mn, hp)
        self.manna = mn
    
        
        
      
class Heeler(Wizard):
    def __init__(self, ):
        
class Gandalf(Wizard):
    def __init__(self, ):
'''
Vasya = Knight(name='Вася')
Petya = Warrior(name = 'Петя')
Vasya.fight(Petya)
Petya.fight(Vasya)
