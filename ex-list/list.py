# quantidade de números
n = int(input("Quantos números deseja informar? "))

numeros = []

# leitura dos valores
for i in range(n):
    valor = float(input(f"Digite o {i+1}º número: "))
    numeros.append(valor)

# cálculos
menor = min(numeros)
maior = max(numeros)
soma = sum(numeros)

# saída
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Soma dos valores: {soma}")