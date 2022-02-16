# -*- coding: utf-8 -*-
#поле  с кнопкой старт(очистить)
from tkinter import*

x=0
y=0

root = Tk()
canva = Canvas(root, width = 360, height=360, bg='white')
canva.pack()

canva.create_line(120,0, 120, 360)
canva.create_line(240,0, 240, 360)
canva.create_line(0, 120, 360, 120)
canva.create_line(0, 240, 360, 240)

btn = Button(root, text='start!')
btn.pack()

def getorigin(eventorigin):
    global x, y
    x = eventorigin.x
    y=eventorigin.y
    if 0<=x<=120 and 0<=y<=120:
        canva.create_oval(30, 90, 90, 30, fill='#73C8B7')
    if 120<=x<=240 and 0<=y<=120:
        canva.create_oval(150, 90, 210, 30, fill='#73C8B7')
    if 240<=x<=360 and 0<=y<=120:
        canva.create_oval(270, 90, 330, 30, fill='#73C8B7')
    if 0<=x<=120 and 120<=y<=240:
        canva.create_oval(30, 150, 90, 210, fill='#73C8B7')
    if 120<=x<=240 and 120<=y<=240:
        canva.create_oval(150, 150, 210, 210, fill='#73C8B7')
    if 240<=x<=360 and 120<=y<=240:
        canva.create_oval(270, 150, 330, 210, fill='#73C8B7')
    if 0<=x<=120 and 240<=y<=360:    #?
        canva.create_oval(30, 270, 90, 330, fill='#73C8B7')
    if 120<=x<=240 and 240<=y<=360:
        canva.create_oval(150, 270, 210, 330, fill='#73C8B7')
    if 240<=x<=360 and 240<=y<=360:
        canva.create_oval(270, 270, 330, 330, fill='#73C8B7')
        
        
        
        
root.bind('<Button 1>', getorigin)    


    
root.mainloop()