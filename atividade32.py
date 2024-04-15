valor_total = float(input("Digite o valor total da compra: "))
desconto_vista = valor_total * 0.1
valor_vista = valor_total - desconto_vista
parcelas = valor_total / 3
comissao_vista = valor_vista * 0.05
comissao_parcelado = valor_total * 0.05
print("O total a pagar com desconto de 10% é:", valor_vista)
print("O valor de cada parcela, no parcelamento de 3x sem juros, é:", parcelas)
print("A comissão do vendedor, caso de a venda ser a vista, é:", comissao_vista)
print("A comissão do vendedor, caso de a venda ser parcelada, é:", comissao_parcelado)
