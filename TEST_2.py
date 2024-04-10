'''
Creare un sistema ripetibile che  permetta di registrarsi ( NOME, INT1, INT2, INT3 ) 
e di superare il login solo se fornisco La somma delle tre variabili intere e nome 

'''
import random
nome = "Erica"

while True:
    login = print(input("Vuoi fare il login? \n si \n no \n"))
    int1=random.randint(1, 11)
    int2=random.randint(1, 11)
    int3=random.randint(1, 11)
    if login.lower() == "si":
        test = int(print(input("Devi fare la somma di questi 3 numeri", int1, int2, int3)))
        if test == (int1 + int2 + int3 ):
            nome = print("Risultato esatto, ora scrivi il tuo nome: \n")
            if nome=="Erica":
                print("Nome e somma corretti, ora puoi accedere")
        else: 
            print("Mi dispiace non puoi accedere")
            break 
                        
