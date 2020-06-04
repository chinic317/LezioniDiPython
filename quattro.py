# -*- coding: utf-8 -*-
"""
Created on Tue May 26 09:22:36 2020

@author: Nicola Chiaradia
"""


'''a=7
b=0


try:
    result = a/b
except ZeroDivisionError:
    print("Impossibile fare una divisione per 0")
    
    
try:   
    primo=float(input("Inserire il primo valore: "))
    secondo=float(input("Inserire il secondo valore: "))
    print(primo/secondo)
except ValueError:
    print("IL valore non inserito non è corretto")
    
finally:
    print("Inserisci il tipo di valore corrretto")
    
    
parametri = []
try: 
    dati = open("./config.txt", "r")
    for line in dati: 
        try: 
            parametri.append(float(line.split(sep = "=")[1]))
            if (line.split(sep = "=")[0].strip() == ""):
                print("Un parametro non può essere vuoto come questo: ", line)
        except ValueError: 
            print("Parametro", line.split(sep = "=")[0].rstrip(), "non valido.")
            continue
        except IndexError: 
            print("Il parametro \"", line.replace('\n',''), "\" non è strutturato nella forma param = valore")
            continue
    try: 
        parametri.append(div(parametri[0], parametri[1]))
    except ZeroDivisionError:
        print("\nNel file esiste un valore pari a 0 che genera errore")
except FileNotFoundError: 
    print("\n\nModifica il nome o percorso del file, quello che hai inserito non è valido!")
finally: 
    dati.close()

 

print("\n\n", parametri)

'''


mylist=["martedi","26","maggio","2020"]
mylist_file=open("mylistfile.txt","w")
for k in mylist:
    n=mylist_file.write(k+"\n")
    print("Lunghezza caratteri stringa :",n-1)
mylist_file.close()
print("Passiamo alla sezione 2")