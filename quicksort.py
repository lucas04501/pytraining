def quicksort(lista):
    if len(lista) < 2:
        return lista

    pivo = lista[0]

    menores = [x for x in lista[1:] if x <= pivo]
    maiores = [x for x in lista[1:] if x > pivo]

    return quicksort(menores) + [pivo] + quicksort(maiores)


numeros = [10, 5, 2, 3, 8, 1]

resultado = quicksort(numeros)

print("Lista original:", numeros)
print("Lista ordenada:", resultado)