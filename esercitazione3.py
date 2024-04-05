'''conteggio = 0
while conteggio < 5: 
    print(conteggio)
    conteggio += 1
'''

'''esercizio: ristorante automatico
1- fare inserire un nome all'utente
2- ad ogni nome assegna un numero di tavolo che aumenta di uno ogni volta
3- l'utente sceglie 3 ingredienti da 3 liste (base, farcitura, topping)(3 basi 3 farciture)
4- in base alla scelta crea una torta finale e il prezzo
5- alla fine dell'ordine di ogni torta devo stampare base farcitura topping e totale del prezzo 
6- scrivere alla fine quante torte e quanto guadagno totale
'''

nrtav = 0 ##conteggio tavoli
base = ["pan di spagna", "pasta frolla", "pan brioche"] 
farcitura = ["cioccolato", "crema chantilly", "panna"]
topping = ["fragole", "gocce di cioccolato", "granella di pistacchio"]
prezzo_base = [2, 3, 4]
prezzo_farcitura = [5, 6, 7]
prezzo_topping = [8, 9, 10]
guadagno_tot = 0 #guadagno finale
tot_torte = 0 # torte totali


while True:
    #chiedo il nome al cliente
    nome = input("Buonasera quale è il suo nome? \n")
    tavolo = nrtav + 1
    #chiedo che base per la torta vuole
    print("Queste sono le basi torta disponibili: \n", base)
    base_torta = input("Che base desidera per la sua torta? \n")
    if base_torta==0:
        prezzo_cliente = prezzo_base[0]
    elif base_torta==1:
        prezzo_cliente = prezzo_base[1]
    else:
        prezzo_cliente = prezzo_base[2]
    scelta_base = base_torta # scelta finale base
    tot_base = prezzo_cliente # prezzo per la base scelta
    #chiedo la farcitura
    print("Queste sono le farciture disponibili: \n", farcitura)
    farcitura_torta = input("Che farcitura desidera per la sua torta? \n")
    if farcitura_torta==0:
        prezzo_cliente = prezzo_farcitura[0]
    elif farcitura_torta==1:
        prezzo_cliente = prezzo_farcitura[1]
    else:
        prezzo_cliente = prezzo_farcitura[2]
    scelta_farc = farcitura_torta # scelta finale farcitura
    tot_farc = prezzo_cliente # prezzo per la farcitura scelta 
    #chiedo i topping
    print("Questi sono i topping disponibili: \n", topping)
    topping_torta = input("Che topping desidera per la sua torta? \n")
    if topping_torta==0:
        prezzo_cliente = prezzo_topping[0]
    elif topping_torta==1:
        prezzo_cliente = prezzo_topping[1]
    else:
        prezzo_cliente = prezzo_topping[2]
    scelta_top = topping_torta # scelta finale topping
    tot_top = prezzo_cliente # prezzo per il topping scelto
    
    prezzotot_torta = tot_base + tot_farc + tot_top # prezzo finale della torta in base alle scelte fatte
    print("Hai scelto una torta composta da: ", scelta_base , scelta_farc , scelta_top , " e il prezzo finale è di " , prezzotot_torta , "euro")


    if nrtav==5: 
        nrtav = False
    break 


        


