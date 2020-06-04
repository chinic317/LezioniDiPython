# -*- coding: utf-8 -*-
"""
Created on Thu May 21 09:13:14 2020

@author: Nicola Chiaradia
"""

'''
a=10
b=20

if a==b:
    print('numeri uguali')
else:
    print ('numeri diversi')
    
opt=2
if opt==1:
    print("Hai scelto l'opzione 1")
if opt==2:
    print("Hai scelto l'opzione 2")
if opt==3:
    print("Hai scelto l'opzione 3")
if opt==4:
    print("Hai scelto l'opzione 4")
else:
    print("nessuna pzione è stata scelta")
    '''





import numpy
import utils 
import timeit
# from utils import check_even_odd(num)
#from nomecartella.utils import check_even_odd(num)
asknum=False        
    
if asknum==True:
     
    while True:
     try :
         num= int(input("Inserisci un numero: "))
         print("il numero scelto è ",num)
         utils.check_even_odd(num)
         break
     
     except(ValueError):
         print("Devi inseire un numero")
    print("il quadrato di ",num ,"è", utils.square(num))
    print   ("il quadrato di ",num ,"è", numpy.square(num))
    print ("La lista dei sottomultippli di ",num," è " ,utils.events(num))  


'''
stringa="stringa di prova"
stringa2="Mi devo andare a prendere il caffè"

for c in stringa2:
    print (c)
   
    
start1=timeit.default_timer()
lista_quadrati=[]
for c in range(10):
    lista_quadrati.append(numpy.square(c))
#print(lista_quadrati)
print("Tempo di esecuzione primo ciclo (CICOLO FOR)" ,round(1000*(timeit.default_timer()-start1),5) , " ms")
    
start2=timeit.default_timer()   
lista_q=[utils.square(c) for c in range(10)] 
#print(lista_q)   
print("Tempo di esecuzione secondo ciclo (COMPPREHENSION)" , round(1000*(timeit.default_timer()-start2),5) , " ms")


start3=timeit.default_timer()
dict_q={utils.square(c) for c in range(10)}

print("Tempo di esecuzione terzo ciclo (COMPPREHENSION) e dizionario" , round(1000*(timeit.default_timer()-start3),5) , " ms")
print("Terzo ciclo (COMPPREHENSION) e dizionario",dict_q)

'''


stringa_in="Esercizio di calcolo occorrenze nel testo"
print(utils.calcola_occ(stringa_in))