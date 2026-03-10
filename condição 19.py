compra = input("O valor final da sua compra deu 100 reais, digite a forma de pagamento")
if(compra == "credito" or "crédito"):
    print("o valor final da sua compra é", 100-100*5/100)
elif(compra == "pix"):
    print("o valor final da sua compra é", (100-100/10))
elif(compra == "debito" or "debito"):
    print("o valor final da sua compra é 100")