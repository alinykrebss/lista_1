investimento1 = float(input("Digite o valor investido pelo primeiro apostador: "))
investimento2 = float(input("Digite o valor investido pelo segundo apostador: "))
investimento3 = float(input("Digite o valor investido pelo terceiro apostador: "))
premio = float(input("Digite o valor total do prêmio: "))
total_investido = investimento1 + investimento2 + investimento3
proporcao1 = investimento1 / total_investido
proporcao2 = investimento2 / total_investido
proporcao3 = investimento3 / total_investido
premio_ganho1 = premio * proporcao1
premio_ganho2 = premio * proporcao2
premio_ganho3 = premio * proporcao3
print("O primeiro apostador ganhou:", premio_ganho1)
print("O segundo apostador ganhou:", premio_ganho2)
print("O terceiro apostador ganhou:", premio_ganho3)

