Abates = int(input("Digite seu numero de abates"))
Assistencias = int(input("Digite seu numero de assistencias"))
Mortes = int(input("Digite seu numero de mortes"))
if(Abates+Assistencias-Mortes>0):
    print("Seu saldo é positivo")
elif(Abates+Assistencias-Mortes == 0):
        print("Voce não tem saldo")
else:
    print("Seu saldo é negativo")