lista = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

soma = 0
for linha in lista:
    soma_linha = 0
    print(linha, end='#')
    for coluna in linha:
     soma_linha = soma_linha + coluna
    print(soma_linha)
    soma = soma + soma_linha
print(' '*9,"---")
print(' '*9,soma)
    # soma = soma + valor 
    # contador = contador + 1+