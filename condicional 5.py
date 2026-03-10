Data_de_nascimento = int(input("Digite sua data de nascimento"))
Ano = int(input("Digite o ano atual"))
if(Ano-Data_de_nascimento>18):
    print("Voce já pode tirar a CNH")
else:
    print("Você ainda é menor de idade")