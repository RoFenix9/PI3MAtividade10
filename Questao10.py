vendas = []
total = 0

for i in range(6):
    valor = float(input("Digite o valor das vendas do mês: "))
    vendas.append(valor)
    total += valor

media = total / 6

acima_media = 0

for valor in vendas:
    if valor > media:
        acima_media += 1

print("Total de vendas:", total)
print("Média mensal:", media)
print("Meses acima da média:", acima_media)
