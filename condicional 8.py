m = float(input("Digite sua nota de matemaitca"))
q = float(input("Digite sua nota de quimica"))
b = float(input("Digite sua nota de biologia"))
if((m+q+b)/3<5):
    print("Sua nota é insuficiente")
elif((m+q+b)/3>=5 and (m+q+b)/3<=8.9):
    print("Sua nota é Boa")
elif((m+q+b)/3>=9):
    print("Sua nota é excelente")