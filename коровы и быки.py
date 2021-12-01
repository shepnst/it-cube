# -*- coding: utf-8 -*-
from random import *
b=0
c=0

s = '0123456789'
com = choice(s)
for i in range(3):
    com+=choice(s)
    
user = input()
print('вы ввели число', com, 'мое число -',user)

for i in range(4):
    if com[i]==user[i]:
        b+=1
    if user[i] in com:
        c+=1
        
print(b, 'быков',  c, 'коров' )

    

