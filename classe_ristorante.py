## Esercizio creare una classe Ristorante

# CREO CLASSE RISTORANTE
class Ristorante:
    # dizionario con piatti e prezzi del ristorante 
    menu = { 
        "piatti" : {"carbonara", "amatriciana", "gricia"},
        "prezzo" : {"12.00€", "13.00€", "11.00€"}
    }
    
    # attributo aperto (mi dice se il ristorante è aperto. default False che vuol dire che è chiuso)
    aperto = False
    
    # metodo costruttore: 
    def __init__ (self, nome, tipo_cucina):
        self.nome = nome
        self.tipo_cucina = tipo_cucina
    

    #### METODI
    # 1- descrivi ristorante (printa "il ristorante + nome + tipo_cucina")
    def descrivi_ristorante(self):
        return print("Il ristorante", self.nome, "fa la cucina ", self.tipo_cucina)

    # 2- stato apertura (printa se il ristorante è aperto o chiuso)
    def stato_apertura(self):
        if Ristorante.aperto == False:
            print("Il ristorante è chiuso")
        else:
            print("Il ristorante è aperto")


    # 3- apri ristorante (imposta aperto==True e printa "il ristorante è aperto")
    def apri_ristorante(self):
        if Ristorante.aperto == False:
            Ristorante.aperto = True
            print("Il ristorante è ora aperto")
        else:
            print("Il ristorante è aperto")



    # 4- chiudi ristorante (imposta aperto==False e printa "il ristorante è chiuso")
    def chiudi_ristorante(self):
        if Ristorante.aperto == True:
            Ristorante.aperto = False
            print("Il ristorante è ora chiuso")
        else:
            print("Il ristorante è chiuso")



    # 5- aggiungi al menu (aggiunge piatti al menu)
    def aggiungi_menu(self):
           aggiungi = input("Vuoi aggiungere un piatto al menù? \n si \n no")
           if aggiungi=="si":                                             
                    piatto=input("inserisci il nome del piatto: ")     
                    prezzo=input("inserisci il prezzo del piatto: ")
                    Ristorante.menu.append([piatto,prezzo])
             


    # 6- togli dal menu (toglie piatti dal menù)
    # 7- stampa menu (printa il menù)

