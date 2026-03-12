imagem = '''============================
           | ======================== |
           | |                      | |
           | | 0                    | |
           | ======================== |
           |                          |
           |1 - soma                  |
           |2 - subtração             |
           |3 - multiplicar           |
           |4 - dividir               |
           |5 - elevar x a y          |
           |6 - função afim           |
           |7 - tirar a raiz          |
           |8 - fatorial              |
           |9 - historico             |
           |0 - fechar calculadora    |
           |                          |
           |                          |
           ============================'''
print(imagem)
parar = "não"
while parar != "sim":
    qo = int(input("qual operação voce quer fazer?"))
    if qo == 1:
        print('''============================
            | ======================== |
            | |                      | |
            | |quantos numeros?      | |
            | ======================== |''')
        qn = int(input("?"))
        if qn <=1:
            print("Não é possivel somar 1 numero")
        elif qn == 2:
            numero = int(input("digite um numero"))
            numero2 = int(input("digite o segundo numero"))
            print(f'''============================
            | ======================== |
            | |                      | |
            | |{numero2+numero}             |           
            | ======================== |''')
            parar = input("deseja parar?")
        elif qn == 3:
            numero = int(input("digite um numero"))
            numero2 = int(input("digite o segundo numero"))
            numero3 = int(input("digite o terceiro numero"))
            print(f'''============================
            | ======================== |
            | |                      | |
            | |{numero2+numero+numero3}            |             
            | ======================== |''')
            parar = input("deseja parar?")
        
    if qo == 2:
        print('''============================
            | ======================== |
            | |                      | |
            | |quantos numeros?      | |
            | ======================== |''')
        qn = int(input("?"))
        if qn <=1:
            print("Não é possivel subtrair 1 numero")
        elif qn == 2:
            numero = int(input("digite um numero"))
            numero2 = int(input("digite o segundo numero"))
            print(f'''============================
            | ======================== |
            | |                      | |
            | |{numero-numero2}             |           
            | ======================== |''')
            parar = input("deseja parar?")
        elif qn == 3:
            numero = int(input("digite um numero"))
            numero2 = int(input("digite o segundo numero"))
            numero3 = int(input("digite o terceiro numero"))
            print(f'''============================
            | ======================== |
            | |                      | |
            | |{numero-numero2-numero3}            |             
            | ======================== |''')
            parar = input("deseja parar?")
    if qo == 3:
        print('''============================
            | ======================== |
            | |                      | |
            | |quantos numeros?      | |
            | ======================== |''')
        qn = int(input("?"))
        if qn <=1:
            print("Não é possivel multiplicar 1 numero")
        elif qn == 2:
            numero = int(input("digite um numero"))
            numero2 = int(input("digite o segundo numero"))
            print(f'''============================
            | ======================== |
            | |                      | |
            | |{numero2*numero}                |           
            | ======================== |''')
            parar = input("deseja parar?")
        elif qn == 3:
            numero = int(input("digite um numero"))
            numero2 = int(input("digite o segundo numero"))
            numero3 = int(input("digite o terceiro numero"))
            print(f'''============================
            | ======================== |
            | |                      | |
            | |{numero2*numero*numero3}            |             
            | ======================== |''')
            parar = input("deseja parar?")
    if qo == 4:
        print('''============================
            | ======================== |
            | |                      | |
            | |quantos numeros?      | |
            | ======================== |''')
        qn = int(input("?"))
        if qn <=1:
            print("Não é possivel dividir 1 numero")
        elif qn == 2:
            numero = int(input("digite um numero"))
            numero2 = int(input("digite o segundo numero"))
            if numero == 0 or numero2 == 0:
                print("Não é possivel dividir por zero")
            print(f'''============================
            | ======================== |
            | |                      | |
            | |{numero/numero2}                    |           
            | ======================== |''')
            parar = input("deseja parar?")
        else:
            print("não é possivel dividir mais numeros")
            parar = input("deseja parar?")

    
    

        
    
        
    
        
    
        
    