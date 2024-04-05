'''def saluta(nome):
    print("Ciao",nome)
saluta("Erica")

def somma(a,b):
    risultato = a + b
    print(risultato)
somma(200,35)

def quadrato(numero):
    return numero * numero
es = quadrato(4)
print(es)'''

### Esercizio 1 
'''
1- un programma genera un numero casuale tra 1 e 100
2- l'utente deve indovinare il numero 
3- ad ogni tentativo il programma deve dire se il numero è più basso o più alto rispetto al numero inserito
4- il gioco termina quando l'utente indovina il numero o decide di uscire
'''


import random
# definisco la funzione che richiamando mi fa indovinare un numero
def indovina():
    num_casuale=random.randint(1, 101)
    print("Indovina un numero da 1 a 100")
    bool = False
    tentativi = 0
    while bool!=True:
        num = int(input("Indovina: "))
        if num == num_casuale:
            print("Hai indovinato!")
        elif num > num_casuale:
            print("Il numero è minore.")
            tentativi+=1
        else :
            print("Il numero è maggiore")
            tentativi += 1
indovina()


