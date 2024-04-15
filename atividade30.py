valor_hora = float(input("Digite o valor da hora de trabalho em reais: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
salario_bruto = valor_hora * horas_trabalhadas
aumento = salario_bruto * 0.1
salario_total = salario_bruto + aumento
print("O valor a ser pago ao funcionário é:", salario_total)