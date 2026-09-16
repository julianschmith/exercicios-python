preco = float(input("Digite o preço do produto: "))
qntd = int(input("Digite a quantidade comprada: "))

valor_total = preco * qntd

print(f"O valor total da compra é: R${valor_total:.2f}")