'''
Crea un sistema ripetibile che chieda di creare una classe panino, 
che per essere istanziato, vuole che l'utente inserisca: 
un tipo di pane, un riempimento, una salsa e un nome panino, 
che devono riempire una lista e 
quando creato dovrà stampare la sua composizione, 
se crei più panini alla fine dovrà stampare tutti i contenuti
'''

class Panino:
    pass



panino = []

while True:
    tipo_pane = int(input("Che pane desidera? \n [1] baguette \n [2] \n [3]\n "))
    riempimento = int(input("Che riempimento? \n [1] prosciutto \n [2] formaggio \n [3] insalata"))
    salsa = int(input("Che salsa? \n [1] ketchup \n [2] senape \n [3] maionese"))
    nome = input("Nome panino? \n ")
    panino.append(tipo_pane,riempimento,salsa,nome)
    print("Il panino scelto è del tipo", tipo_pane, " condito con ", riempimento, " con salsa ", salsa, "e ha il nome ", nome)
    