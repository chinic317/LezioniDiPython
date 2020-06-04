# -*- coding: utf-8 -*-
"""
Created on Thu May 21 09:39:29 2020

@author: Nicola Chiaradia
"""


def check_even_odd(num):
    
    
     if num % 2 ==0:
        print(num," è un numero pari")
     else:
        print(num," è un numero dispari")
        
     if num % 3 ==0:
          print(num," è numero multiplo di 3")
     else:
        print(num," non è un numero muliplo di 3")
        
        
        
        
def square(num):
    return num**2


def events(num):
    if num % 2 ==0 :
        l_evens= [num]
    else:
        l_evens =[]
    
    while num > 0:
        num -=1
        if not num % 2 == 0:
            continue
        
        l_evens += [num]    
        
    return l_evens

def calcola_occ(stringa_in):
    dict_tmn={}
    for char in stringa_in.lower():
        occ=dict_tmn.get(char,0)
        if occ== 0:
            dict_tmn.update({char:1})
        else:
            dict_tmn[char] +=1            
    return dict_tmn



def divisione(val1,val2):
    try:
        result = val1/val2
    except ZeroDivisionError:
        print("Impossibile fare una divisione per 0")
    
    
        '''  
     try:   
        val1=float(input("Inserire il primo valore: "))
        val2=float(input("Inserire il secondo valore: "))
        print(val1/val2)
    except ValueError:
           print("IL valore non inserito non è corretto")'''
    
    
    
    return result