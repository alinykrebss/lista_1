numero = int(input("Digite um número inteiro de 4 dígitos: "))
if 1000 <= numero <= 9999:
    for digito in str(numero):
        print(digito)
else:
    print("Número inválido.")
