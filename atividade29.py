dias_trabalhados = int(input("Digite o número de dias trabalhados: "))
valor_dia = 30.00
previdencia = dias_trabalhados * valor_dia * 0.11
salario_bruto = dias_trabalhados * valor_dia - previdencia
imposto_renda = salario_bruto * 0.08
salario_liquido = salario_bruto - imposto_renda
print("O salário líquido a ser pago é:", salario_liquido)
