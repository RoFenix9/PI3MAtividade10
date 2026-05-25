n = input("Digite um número inteiro: ")
d = input("Digite um dígito de 0 a 9: ")

contador = 0

for numero in n:
    if numero == d:
        contador += 1

print("Quantidade de vezes que o dígito aparece:", contador)
