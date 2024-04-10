'''
Crea un sistema ripetibile che crei un oggetto della classe visitatore ( Nome, ID  )  
e lo aggiunga al registroVisitatori che è una lista della classe 
( padre / figlia a scelta ) Museo, stampa alla fine tutti i visitatori

'''
class Museo:
    registroVisitatori = []
    def __init__(self, registroVisitatori):
        self.registroVisitatori = registroVisitatori

    def stampa_visitatori(self):
        print("Ecco la lista dei visitatori", self.registroVisitatori)

class Visitatore(Museo):
    nome = []
    ID = []
    def __init__(self, registroVisitatori, nome, ID):
        super().__init__(registroVisitatori)
        self.nome = nome
        self.ID = ID
    
    def stampa_visitatori(self):
        super().stampa_visitatori()

ID = 0 
registroVisitatori = []
while True:
    nome = input("Inserisci il tuo nome")
    ID += 1
    registroVisitatori.append(nome,ID)
    
