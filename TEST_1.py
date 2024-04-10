'''
Creare un sistema che faccia inserire un numero e continui a ripetere il sistema finchè il numero è pari, 
dopo aver inserito invece 3 numeri dispari che vengono salvati li stampa e chiude tutto
'''
lista = []
num = input("Inserisci un numero: \n")
while True:
    if num % 2 == 0:
        num = int(print(input("Inserisci un altro numero: ")))
    elif num % 2 != 0:
        lista.append(num)
        num_disp = int(print(input("Inserisci un altro numero, quello che hai inserito è dispari ")))
        if num_disp % 2 != 0:
            lista.append(num,num_disp)
            num_disp2 = int(print(input("Inserisci un altro numero, quello che hai inserito è dispari ")))
            if num_disp2 % 2 != 0:
                lista.append(num,num_disp,num_disp2)
                print(lista)
                sorry = input("Mi dispiace hai inserito 3 numeri è finita")




