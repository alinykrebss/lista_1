custo_fabrica = float(input("Digite o custo de fábrica do carro em reais: "))
porcentagem_distribuidor = 0.12
porcentagem_impostos = 0.45
custo_consumidor = custo_fabrica * (1 + porcentagem_distribuidor + porcentagem_impostos)
print("O custo ao consumidor do carro é:", custo_consumidor, "reais")
