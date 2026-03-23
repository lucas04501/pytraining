a = 1
b = 1

for i in range(10):
    print(a, end=", ")
    aux = a
    a = b
    b = aux + b

'''
explicando: vai printar o A que vale um e colocar uma virgula e vai pra conta, onde o aux = a (aux passa a ser 1 pq o A vale 1), depois o A = b 
(onde o b é = A onde o A é igual a 1), onde b = aux + 1 (aux = A que é 1, + b que é 1) no final fica b = 1 + 1 ou seja 2.
agora o B = 2 so ir fazendo esse sistema trocando as letras pelos numeros, ate chegar no 55
'''
