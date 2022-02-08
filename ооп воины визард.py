# -*- coding: utf-8 -*-
from random import*
from tkinter import*
'''
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
        print(self.name, 'ударил', enemy.name, 'на', self.attack)
        
class Knight(Warrior):
    def __init__(self, name, hp=100, ap = 10, ag = 50):
        super().__init__(name, hp, ap, ag)
        self.health = hp+20
        
class Ranger(Warrior):
    def __init__(self, name, hp=100, ap = 10, ag = 50):
       super().__init__(name, hp, ap, ag)
       self.agility = hp-20
       self.attack = ap+5
        
def fighting(ch):
    while len(ch)>1:
        a = choice(ch)
        b = choice(ch)
        if a==b:
            print(a.name, 'наступил себе на ногу')
            continue
        a.fight(b)
        if b.health<=0:
            ch.remove(b)
            print(b.name, 'убит!')
    print(ch[0].__dict__)
    
    
players = [Knight('Маша'), Ranger ('Дима'), ]
for i in players:
    print(i.__dict__)
'''

root = Tk()
canva = Canvas(root, width =650, height =600 , bg='#73C87F')
canva.pack()

btn = Button(root,text = 'let`s start!', background = '#555', 
             foreground = '#ccc', width = 8, height = 3)
btn.pack()

root.mainloop()










#fighting(players)


             
