# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:30:35 2020

@author: Nicola Chiaradia
"""

'''
#Area del cerchio avendo come input raggio


pg=3.14
raggio=int(input("Inserisci la lunghezza del raggio in cm: "))

circ=(raggio*raggio)*pg

print("La circonferenza del cerchio è di :",circ)

'''
#Area Trapezio



while True:
        try:
            bMag=int(input("Inserisci la lunghezza della BASE MAGGIORE in cm: "))
            
        except (ValueError):
            print("Inserire un val0re corretto")
            continue
        else:
            break
        
while True:
        try:
            bMin=int(input("Inserisci la lunghezza della BASE MINORE in cm: "))       
        except (ValueError):
            print("Inserire un val0re corretto")
            continue
        else:
            break
        
while True:
        try:
            alt=int(input("Inserisci l'altezza in cm: "))
        except (ValueError):
            print("Inserire un val0re corretto")
            continue
        else:
            break

def AreaTR(bMag,bMin,alt):
    
        
    AreaTrapezio=float((bMag*bMin)*alt/2)
    
    print("L'Area del Trapezio è di  ",AreaTrapezio," cm quadrati")
    
    
    
    
tr1=AreaTR(bMag, bMin, alt)