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

'''se usa o elif quando queremos verificar varias condições em sequencia, sem precisar aninhar ifs dentro de else.
A estrutura if/elif/else é uma forma de tomar decisões com base em varias condições, onde o programa verifica cada condição em ordem e executa o bloco de código correspondente à primeira condição verdadeira.
A sintaxe é a seguinte:'''
#if condição1:
    # bloco de código para condição1
    # ...
#elif condição2:        
#   # bloco de código para condição2
#  ...
#else:
    # bloco de código para quando nenhuma das condições anteriores for verdadeira
    # ... else se usa so no final se precisar
    
    
    # O programa verifica a condição1, se for verdadeira, executa o bloco de código para condição1 e ignora as outras condições. Se a condição1 for falsa, ele verifica a condição2, se for verdadeira, executa o bloco de código para condição2 e ignora as outras condições. Se a condição2 for falsa, ele executa o bloco de código do else.
    # A estrutura if/elif/else é útil para lidar com situações onde existem varias possibilidades e queremos executar um bloco de código diferente para cada possibilidade.
    # Por exemplo, podemos usar if/elif/else para classificar um número como positivo, negativo ou zero, como fizemos no exemplo acima.
    # Também podemos usar if/elif/else para verificar a faixa de um número, como por exemplo, se um número é menor que 10, entre 10 e 20, ou maior que 20.
    # Em resumo, o elif é uma forma de verificar varias condições em sequencia, sem precisar aninhar ifs dentro de else, e é uma parte importante da estrutura condicional em Python.
    # O código acima é um exemplo de como usar a estrutura if/elif/else para classificar um número como positivo, negativo ou zero, e é uma forma mais clara e eficiente de lidar com varias condições em sequencia.
    # A estrutura if/elif/else é uma ferramenta poderosa para tomar decisões em Python, e é fundamental para escrever código que seja legível e fácil de entender. 