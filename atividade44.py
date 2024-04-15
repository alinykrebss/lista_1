nome_vendedor = input("Digite o nome do vendedor: ")
carros_vendidos = int(input("Digite o número de carros vendidos: "))
valor_vendas = float(input("Digite o valor total das vendas: "))
salario_fixo = 500.00
comissao_carro = 50.00 + (0.05 * valor_vendas)
salario_mes = salario_fixo + (comissao_carro * carros_vendidos)
print("O salário de", nome_vendedor, "é:", salario_mes, "reais")
