numero = int(input("Digite um número inteiro positivo de três dígitos: "))
if 100 <= numero <= 999:
    numero_invertido = int(str(numero)[::-1])
    print("O número formado pelos dígitos invertidos é:", numero_invertido)
else:
    print("Número inválido.")
