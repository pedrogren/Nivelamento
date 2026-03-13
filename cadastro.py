nome = input("Digite seu nome")
idade = int(input("Digite sua idade"))
email = input("Digite seu email")
usuario = [nome, idade, email]
def nomeEhValido(nome):
    if len(nome)<=2:
        return False
    return True
def validaNome():
    while nomeEhValido(nome):
        print("Seu nome deve ter pelo menos 3 letras")
        usuario[0] = input("Digite seu nome")

def idadeEhValida(idade):
    if idade<=17:
        return False
    return True
def validaIdade():
    while idadeEhValida(idade):
        print("Você deve ter pelo menos 18 anos pra se cadastrar")
    usuario[1] = input("Digite sua idade")

def emailEhValido(email):
    if idade <=17:
        return False
    return True
def validaEmail():
    while emailEhValido(email):
        print("Insira um email valido")
    usuario[2] = input("Digite seu email")