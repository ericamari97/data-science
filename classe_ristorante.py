## Esercizio creare una classe Ristorante

# CREO CLASSE RISTORANTE
class Ristorante:
    # dizionario con piatti e prezzi del ristorante 
    piatti = ["carbonara", "amatriciana", "gricia"]
    prezzo = [12.00, 13.00, 11.00]
    
    menu = { 
        "carbonara" : "12.00",
        "amatriciana" : "13.00", 
        "gricia" : "11.00"
    }
    
    
    # metodo costruttore: 
    def __init__ (self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
        self.aperto = False  # mi dice se il ristorante è aperto. default False che vuol dire che è chiuso
    
    #### METODI
    # 1- descrivi ristorante (printa "il ristorante + nome + tipo_cucina")
    def descrivi_ristorante(self):
        return print("Il ristorante", self.nome, "fa la cucina", self.tipo_cucina)

    # 2- stato apertura (printa se il ristorante è aperto o chiuso)
    def stato_apertura(self):
        print("Il ristorante è aperto o chiuso?")
        if self.aperto == False:
            print("Il ristorante è chiuso")
        else:
            print("Il ristorante è aperto")


    # 3- apri ristorante (imposta aperto==True e printa "il ristorante è aperto")
    def apri_ristorante(self):
        if self.aperto == False:
            self.aperto = True
            print("Il ristorante è ora aperto")
        else:
            print("Il ristorante è aperto")


    # 4- chiudi ristorante (imposta aperto==False e printa "il ristorante è chiuso")
    def chiudi_ristorante(self):
        if self.aperto == True:
            self.aperto = False
            print("Il ristorante è ora chiuso")
        else:
            print("Il ristorante è chiuso")



    # 5- aggiungi al menu (aggiunge piatti al menu)
    def aggiungi_menu(self):
        aggiungi = input("Vuoi aggiungere un piatto al menù? \n si \n no")
        if aggiungi=="si":                                             
            piatto=input("inserisci il nome del piatto: ")     
            prezzo=input("inserisci il prezzo del piatto: ")
            Ristorante.piatti.append([piatto])
            Ristorante.prezzo.append([prezzo])
           
            print("Nuovo piatto aggiunto al menù")
            print(Ristorante.piatti)
        else: 
            print("Addio")
        
            

    # 6- togli dal menu (toglie piatti dal menù)
    def togli_dal_menu(self):
        rimuovi = input("Vuoi togliere un piatto dal menù? \n si \n no ")
        if rimuovi=="si":
            quale = input("Quale piatto vuoi rimuovere dal menù? \n carbonara \n amatriciana \n gricia")
            if quale=="carbonara":
                Ristorante.piatti.remove("carbonara")
            if quale== "amatriciana":
                Ristorante.piatti.remove("amatriciana")
            else:
                Ristorante.piatti.remove("gricia")

              

    # 7- stampa menu (printa il menù)
    def stampa_menu(self):
        stampa = input("Vuoi stampare il menù del ristorante? \n si \n no ")
        if stampa=="si":
            print(Ristorante.menu.items)
        else:
            print("Addio")
    ### DA RIGUARDARE



### OTTIMIZZAZIONE
##Aggiungere un ristorante sulla piattaforma
while True:
    new_risto = input("Buongiorno vuole aggiungere un ristorante sulla nostra piattaforma? \n si \n no \n")
    if new_risto=="si":
        nome = input("Come si chiama il ristorante? ")
        tipo_cucina = input("Che tipologia di cucina fa? ")
        x = Ristorante(nome, tipo_cucina)
        print(x.descrivi_ristorante())
        
        # aggiungere al menù
        while True:
            print(x.aggiungi_menu())
            ancora = input("Vuoi aggiungere altro? \n si \n no \n")
            if ancora=="si":
                print(x.aggiungi_menu())
            else:
                print("Addio")
                break
        
        # togliere dal menù
        while True: 
            print(x.togli_dal_menu())
            ancora = input("Vuoi rimuovere altro? \n si \n no \n")
            if ancora=="si":
                print(x.togli_dal_menu())
            else:
                print("Addio")
                break
    print(x.stampa_menu)
    print(x.chiudi_ristorante)
    print(x.stato_apertura)
    
    altro = input("Vuoi fare altro? \n si \n no \n")
    if altro=="no":
        break
    else: 
        continue
    
    
    

