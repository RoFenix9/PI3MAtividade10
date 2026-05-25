total = 0

for i in range(1, 8):
    consumo = float(input("Digite o consumo do produto: "))

    if i == 1:
        maior_consumo = consumo
        produto_maior = i

    if consumo > maior_consumo:
        maior_consumo = consumo
        produto_maior = i

    total += consumo

print("Consumo total:", total)
print("Produto que mais consome matéria-prima:", produto_maior)
