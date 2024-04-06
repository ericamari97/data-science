### ESERCIZIO : SISTEMA DI GESTIONE DI UN NEGOZIO (torte, login, dizionari)
'''
sistema di gestione che interagisce con i clienti, gestisce l'inventario, e fa supervisionare dagli amministratori le operazioni
1- clienti:
    visualizzano gli articoli disponibili 
    selezionano e acquistano articoli 
    il sistema tiene traccia degli articoli

2- inventario: 
    articoli hanno: nome, prezzo e quantità 
    posso aggiungere nuovi articoli
    articoli possono essere rimossi o modificati (di prezzo, quantità, etc)

3- amministratori: 
    possono visualizzare un rapporto delle vendite
    possono vedere lo stato dell'inventario
    il sistema tiene traccia dei guadagni totali

Il programma dovrebbe permettere un'interazione base tra cliente e negozio dopo un login e una registrazione 
e consentire manutenzione e analisi del negozio da parte degli amministratori
'''




#### INVENTARIO
articolo = ("jeans", "maglione", "giacca di pelle")
prezzo = (39.90, 50.00, 79.90)
quantità = (50, 30, 80)

inventario = {
    "jeans" : {"prezzo" : 39.90, "quantità" : 50},
    "maglione" : {"prezzo" : 50.00, "quantità" : 30},
    "giacca di pelle" : {"prezzo" : 79.90, "quantità" : 80}
}

#### SISTEMA LOGIN
# inserire nome utente e password
registrazione = input("Sei registrato? \n si \n no")
if registrazione=="si":
    amministratore = input("Sei amministratore? \n si \n no")
    if amministratore=="si":
        while True: 
            utente_amm = input("Inserire utente amministratore \n")
            passw_amm = input("Inserire password amministratore \n ")
            amm_cosafa = print(input("Benvenuto ", utente_amm, "Cosa vuoi fare?\n [1] visualizza l'inventario [2] modifica inventario [3] rimuovi articolo"))
            if amm_cosafa=="1":
                print(inventario)
            elif amm_cosafa=="2":
                modifica = input("[1] aggiungi articolo\n [2] rimuovi articolo \n [3] modifica articolo")
                if modifica=="1":
                    articolo = input("che articolo vuoi aggiungere?\n")
                    prezzo = int(input("che prezzo ha?\n"))
                    quantità = input("quantità articoli disponibili:\n")
                    inventario.append(articolo,prezzo,quantità)
                elif modifica=="3":
                    # modifica prezzo e quantità
                #else:
                    # rimuovi articolo
            #break 

    #else (amministratore=="no"):
        #while True:
            #nome_utente = input("Inserire nome utente \n")
            #passw_utente = input("Inserire password \n ")
            #ut_cosafa = print(input("Benvenuto", nome_utente, "Cosa vuoi fare?\n [1] visualizza articoli disponibili \n [2] acquista articoli"))
            #if ut_cosafa=="1":
                #print(inventario)
            #elif ut_cosafa=="2": 
                #acquisto=print(input("cosa vuoi comprare? \n [1] jeans [2] maglione [3] giacca di pelle"))
                #if acquisto==articolo[0]:
                    #quanti=print(input("quanti jeans vuoi? "))


                




### CLIENTI

#visualizzo articoli

#acquisto articoli


### AMMINISTRATORI

#visualizza rapporto vendite

#vede lo stato dell'inventario 


### SISTEMA

# tiene traccia dei guadagni totali
# tiene traccia degli articoli



