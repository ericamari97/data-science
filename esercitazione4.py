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
    num_casuale=random.randint(1, 101) # numero casuale 
    print("Indovina un numero da 1 a 100")
    bool = False
    tentativi = 0
    while bool!=True:
        num = int(input("Indovina il numero: ")) 
        if num == num_casuale:
            print("Hai indovinato!")
            break
        elif num > num_casuale:
            print("Il numero è minore.")
            tentativi+=1
        else :
            print("Il numero è maggiore")
            tentativi += 1
indovina()


### Esercizio 2: sequenza di Fibonacci fino a N
'''
1- chiedi all'utente di inserire un numero N 
2- il programma deve stampare la sequenza di Fibonacci fino a N
ES: se l'utente inserisce 100, il programma deve stampare tutti i numeri della sequenza di Fibonacci minori o uguali a 100
'''
#definisco la funzione di Fibonacci
def fibo():
    n = int(input("Scegli un numero: "))
    a = 1
    b = 1
    if n == 1:
        print("0")
    elif n == 2:
        print("0", "1")
    else:
        print("0")
        print(a)
        print(b)
        for i in range 
        ### continua
fibo()

## c'è qualcosa che non mi torna forse non ho capito come funziona la sequenza di Fibonacci :)
