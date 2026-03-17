#quando for rodar o codigo, e o usuario digitar 0, o resultado sera negativo e zero, pois ta estruturado dessa forma, o codigo vai verificar se o numero é maior que 0, se for, ele imprime positivo, se nao for, ele imprime negativo e depois verifica se o numero é igual a 0, se for, ele imprime zero.
#ou seja, o codigo nao esta estruturado para verificar se o numero é igual a 0 antes de verificar se é maior que 0, entao quando o usuario digitar 0, ele vai entrar no else e imprimir negativo, e depois vai verificar se o numero é igual a 0, e como é, ele vai imprimir zero.
#temos que estruturar o codigo para verificar se o numero é igual a 0 antes de verificar se é maior que 0, para que quando o usuario digitar 0, ele imprima zero e nao negativo.
#para isso, podemos usar a estrutura elif, que é uma abreviação de else if, e permite verificar varias condições em sequencia, sem precisar aninhar ifs dentro de else.

x = int(input("Digite um número: "))   #solicita ao usuário que digite um número e armazena o valor na variável x
if x > 0:
    print("positivo")
elif x == 0:           #x = 0      # atribuição
                     #x == 0     # comparação (retorna True)
    print("zero")
else:
    print("negativo")
#O código acima é um exemplo de estrutura condicional em Python, onde a variável x é comparada com o valor 0 para determinar se é positiva, negativa ou zero. 
# O código solicita ao usuário que digite um número, converte a entrada para um inteiro e, em seguida, verifica se o número é maior que zero para classificar como positivo, igual a zero para classificar como zero, ou menor que zero para classificar como negativo.    
# Se o número for maior que zero, a mensagem "positivo" será exibida; se o número for igual a zero, a mensagem "zero" será exibida; caso contrário, a mensagem "negativo" será exibida.
