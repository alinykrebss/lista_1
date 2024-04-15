comprimento_terreno = float(input("Digite o comprimento do terreno em metros: "))
largura_terreno = float(input("Digite a largura do terreno em metros: "))
preco_metro_tela = float(input("Digite o preço do metro de tela em reais: "))
custo_cercamento = 2 * (comprimento_terreno + largura_terreno) * preco_metro_tela
print("O custo para cercar o terreno com tela é:", custo_cercamento, "reais")
