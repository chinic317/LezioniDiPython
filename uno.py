# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''a=6
b=3
x=4.7    
print ("Hello Word!")

print ()
print ("Il mio nome è Nicola Chiaradia")
print ()

print(3*8)

print (round(x))

if a + b ==10:
        print (True)
        if a + b !=10 :
            print (False)
print (a+b)       
    '''
import utils  


try:
    nome=str(input("Inserisci il tuo nome :"))
    eta=int(input("Inserisci la tua età :"))
except ValueError:
        print("Valori non conformi") 
        
        

print ("\n\nIl tuo nome è : ",nome)
print (nome,"La tua età è di ",eta, "anni")
    
s =" Sono esatte le tue informazioni ? "  
print(s.strip())
risposta=str(input(""))


  
while risposta=="No":
    
   
    
        try:  
            nome=str(input("Inserisci il tuo nome :"))
            eta=int(input("Inserisci la tua età :"))
        except ValueError:
            print("Valori non conformi")  
   
    
        print ("\n\nIl tuo nome è : ",nome)
        print (nome,"La tua età è di ",eta , "anni")
            
        s =" Sono esatte le tue informazioni ? "  
        print(s.strip())
        risposta=str(input(""))


if risposta=="Si":
     
        w=int(input("inserisci primo valore: "))
        z=int(input("inserisci secondo valore: "))
        print ("La somma è di " ,(w+z))
        print ("Il prodotto è di " ,(w*z))
        print ("La divisione è di " ,utils.divisione(w,z))
      
