
## esercizio 1 

#definisco classe Punto
class Punto:
    #definisco i punti nel piano cartesiano
    x = 0
    y = 0
    def __init__(self, x, y): #metodo costruttore (non necessario)
        self.x = x
        self.y = y
    #definisco il metodo muovi che in input mi da un valore per dx e uno per dy 
    def muovi(self): 
        x = int(input("Inserisci valore di x "))
        y = int(input("Inserisci valore di y  "))
        self.x = x
        self.y = y
        print("le nuove coordinate sono", self.x, self.y)
    #definisco il metodo distanza che mi dà la distanza del punto dall'origine (radice quadrata della somma dei quadrati di x e y)
    def distanza(self):
        distanza = ((self.x**2) + (self.y**2))**(1/2)
        print("La distanza dall'origine è " , self.distanza)

z = Punto(3,5)
print(z.muovi())
