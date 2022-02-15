# -*- coding: utf-8 -*-
#поле  с кнопкой старт(очистить)
from tkinter import*

root = Tk()
canva = Canvas(root, width = 360, height=360, bg='white')
canva.pack()

canva.create_line(120,0, 120, 360)
canva.create_line(240,0, 240, 360)
canva.create_line(0, 120, 360, 120)
canva.create_line(0, 240, 360, 240)

btn = Button(root, text='start!')
btn.pack()



root.mainloop()