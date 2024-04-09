### ESERCIZIO LIBRERIA
''' 
1- crea la classe Libreria: PADRE
    a. attributo catalogo (contiene gli oggetti della classe Libro)
    b. metodi:
        · aggiungi_libro(libro): prende in input un oggetto della classe Libro e lo aggiunge al catalogo
        · rimuovi_libro(id): rimuove un libro dal catalogo in base al suo ID
        · cerca_titolo(titolo): restituisce una lista di libri che corrispondono al titolo dato
        · mostra catalogo(): stampa una descrizione di tutti i libri presenti nel catalogo
2- crea la classe Libro: FIGLIO
    a. attributi (autore, titolo e id)
    b. metodo descrizione()--> restituisce una stringa che descrive il libro usando gli attributi al punto a

'''

## creo la classe Libreria
class Libreria:
    catalogo = {}
    ## metodo costruttore
    def __init__(self, catalogo):
        self.catalogo = catalogo

    ## metodo aggiungi_libro
    def aggiungi_libro(self, libro):
        if libro.isbn in self.catalogo:
            print("Il libro è nel catalogo")
        else: 
            self.catalogo[libro.isbn] = [libro.titolo, libro.autore]
        

    ## metodo rimuovi_libro
    def rimuovi_libro(self, isbn):
        if isbn in self.catalogo:
            del self.catalogo[isbn]
        else:
            print("Il libro non è nel catalogo")


    #metodo cerca_titolo
    def cerca_titolo(self, titolo):
        libri_tot = {}
        for chiave,valore in self.catalogo.items():
            if titolo == self.catalogo[chiave][0]:
                libri_tot[chiave] = titolo
        return libri_tot
       

    #metodo mostra_catalogo
    def mostra_catalogo(self, catalogo):
        print("Catalogo")
        for isbn, info in self.catalogo.items():
            print("titolo: " , info[0], "autore: " , info[1] , "ISBN: " , isbn)


## creo la classe Libro
class Libro(Libreria):
    ## metodo costruttore
    def __init__(self, catalogo, autore, titolo, isbn):
        super().__init__(self, catalogo)
        self.autore = autore
        self.titolo = titolo
        self.isbn = isbn
    ## metodo descrizione
    def descrizione(self):
        print("Il libro scelto si chiama ", self.titolo, " è di ", self.autore, "e ha codice identificativo", self.isbn)


## ADESSO OTTIMIZZO
