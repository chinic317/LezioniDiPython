# -*- coding: utf-8 -*-
"""
Created on Wed May 20 09:15:07 2020

@author: Nicola Chiaradia
"""

''' INDEXING
S="Hello"
print (S[0])
print (S[1])
print (S[2])
print (S[3])
print (S[-1])



L="AERONAUTICA MILITARE" SLICING
print (L[0:4])
print (L[-10:-6])
print (L[:])
print (L[:10])
print (L[5:])




F="NOME" CONCATENATION
#D=3 + "\nCOGNOME" Type error
N=str(3) +" "+ F+" COGNOME"
print(N)
print( N* 4)
print (L.lower().rstrip())

lista =[12, "Aeronautica", 2.56 , "Amazon"]
print(type(lista))
print(lista)
print (lista[2])
print (lista[-1])
print (lista[-2:-1])
print (lista[-2:])
print (lista[0:3])
lista[2]="Sostituzione di 2.56 con 26.5"
print (lista)
lista =lista + [0.27]
lista.append(1984)
print (lista)
print (len(lista))

lista2=lista[0:2] * 3
print(lista2)

print(lista.index("Aeronautica"))


listaday=["lun","mer","gio","ven","sab"]
print(listaday)
listaday.append("dom")
print(listaday)

listaday.insert(1,"mar")
print(listaday)





listaday.remove("lun")
print(listaday)


listanum=[10,19,1.4,6.7,0.4,-3]
print(listanum)
listanum.sort()
print(listanum)
listanum.sort(reverse=True)
print(listanum)




stringa='Prova di Comunicazione'
print(stringa)
print("lunghezza stringa " +str(len(stringa)) + " caratteri")
cond1= 'm' in stringa
print(str(cond1) + ": presente nella stringa "+ (stringa))
cond2= 'f' in stringa
print(cond2)
listanum=[10,19,1.4,6.7,0.4,-3]
print(listanum)
cond3=11 in listanum
print(cond3)
cond4=-3 in listanum
print(cond4)
lista_stringa=list(stringa)
print(lista_stringa)

stringa_base= "".join(lista_stringa)
print(stringa_base)
stringa_base1= "+".join(lista_stringa)
print(stringa_base1)

societa="RoccoSiffredi Srl"
print(societa.split()[0]+" "+".".join(societa.split()[1].upper()))
'''

myset={8.22,15,False,"Nicola",8.22}
print(myset)

stringa_vuota=""
lista_vuota=[]
tupla_vuota=()
set_vuota=set()
dizionario={}
dict1={"Nome":"Zinedine","Cognome":"Zidane","Ruolo":"Centrocampista","NAzionalità":"Francia"}

print(type(stringa_vuota))
print(type(lista_vuota))
print(type(tupla_vuota))
print(type(set_vuota))
print(type(dizionario))
print(dict1)
print(dict1["Cognome"])
del dict1["NAzionalità"]
print (dict1)
print(list(dict1.keys()))
print(list(dict1.values()))
print(dict1.get('Nome'))
print(dict1['Nome'])
























