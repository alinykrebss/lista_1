hamburguer = int(input("Digite a quantidade de hambúrgueres consumidos: "))
cheeseburger = int(input("Digite a quantidade de cheeseburgers consumidos: "))
fritas = int(input("Digite a quantidade de fritas consumidas: "))
refrigerante = int(input("Digite a quantidade de refrigerantes consumidos: "))
milkshake = int(input("Digite a quantidade de milkshakes consumidos: "))
total_conta = hamburguer * 3.00 + cheeseburger * 2.50 + fritas * 2.50 + refrigerante * 1.00 + milkshake * 3.00
print("O total da conta é:", total_conta, "reais")