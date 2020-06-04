# -*- coding: utf-8 -*-
"""
Created on Thu May 28 11:52:08 2020

@author: Nicola Chiaradia
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl
# *************NUMPY************


 
#np.random.seed(18) #valori ramndom sempre con gli stessi valori
a=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
b=np.zeros((5,5))# array con tutti 0
c=np.arange(0,10,2)#array da 0 a 10 di passo 2
d=np.random.randint(0,100,24)# array random di 10 elementi in un range 0-100

f=np.random.uniform(0,100,10)
f=f.reshape(5,2)

x=np.array([[1,2,3],[4,5,6]])
y=np.array([[3,3,3],[3,3,3]])
print(a.shape) # Visualizza dimensioni array
print(a) # Visualizza contenuto array
print (a[0]) # Visualizza elemento indicizzato
print (type(a)) # Visualizza tipo 
print(type(a[1])) # Visualizza tipo elemto indicizzato
print (len(a)) # Visualizza
print(a.ndim)# Visualizza lunghezza array
print(a.dtype)# Visualizza dimesione in byte
print (a.size) # Visualizza il numero degli elementi
print (b.size)
print(b)
print(b.dtype)
print(c)
print(d)
print(f)
print(a.min(),a.max(),a.sum())# Visulaizza minimo massimo e somma dei valori dell'array
print(a.std())#deviazione standard
print(a.mean())#media 
print(a[1].sum())

for k in range (f.shape[0]):
    print ("Somma riga ", k ,":" ,f[k,:].sum())
for k in range (f.shape[1]):
    print ("Somma colonne ", k ,":" ,f[:,k].sum())
    
    
print(x,"\n\n" ,y,"\n")   
print(x+y)
print(x-y)
print(x*y,"\n")

print(x.dot(np.transpose(y))) #Prodotto matriciale