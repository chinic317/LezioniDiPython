# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:28:44 2020

@author: Nicola Chiaradia
"""


materie=('Informatica', 'Matematica', 'Italiano', 'Inglese', 'Storia', 'Arte')
voti=[]

n=len(materie) #ottengo la lunghezza della tupla

for i in range(n):
    v=int(input('Voto in ' + materie[i] + ': '))
    
    while v<1 or v>10:
        v=int(input('Voto in ' + materie[i] + ': '))
        
    voti.append(v)

s=0
massimo=voti[0]
minimo=voti[0]

for i in range(n):
    print('Il voto in', materie[i], 'è', voti[i])
    s+=voti[i]
    if voti[i]>massimo:
        massimo=voti[i]
    elif voti[i]<minimo:
        minimo=voti[i]

print('La media è', s/len(voti))

j = voti.index(minimo) 
print('Voto più basso:', minimo, 'in', materie[j])

j = voti.index(massimo)        
print('Voto più alto:', massimo, 'in', materie[j])