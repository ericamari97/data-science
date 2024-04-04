num = int(input("Inserisci un numero: "))
num2 = 3
while True:
    for numero in range(num, -1, -1):
        print(numero)
    while num2 != 0 and num2!=1:
        num2=int(input("Vuoi ripetere un altro numero? \n si [1] \n no [0]"))
    if num2==0:
        break
    else: 
        num = int(input("Inserisci un numero: "))
        break