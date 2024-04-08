## esercizio 2

#definisco classe chiamata libro
class Libro:

    def __init__(self, titolo, autore, pagine):
        self.titolo = titolo
        self.autore = autore
        self.pagine = pagine
    #definisco il metodo descrizione che mi printa titolo autore e pagine
    def descrizione(self):
        return print("Il libro" , self.titolo + " è stato scritto da" , self.autore + " e ha " , self.pagine, " pagine")



while True:
    scrivi_libro = input("Vuoi cercare un libro? ")
    if scrivi_libro=="si":
        titolo = input("titolo: ")
        autore = input("autore: ")
        pagine = int(input("pagine: "))
        x = Libro(titolo, autore, pagine)
        print(x.descrizione())
    else:
        break

