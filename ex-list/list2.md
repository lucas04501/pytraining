O que é um “array”

Aqui precisa de precisão:

👉 Em Python, o que você usa normalmente NÃO é array — é lista
✔ Lista (o “array” do Python na prática)
numeros = [10, 20, 30]

👉 Isso é uma lista, que funciona como um array, mas é mais poderosa.

🔎 Definição simples

Um array/lista é:

Uma estrutura que guarda vários valores dentro de uma única variável.

🧠 Exemplo prático

Sem lista:

n1 = 10
n2 = 20
n3 = 30

Com lista:

numeros = [10, 20, 30]

✔ Muito mais organizado e escalável

⚙️ Acesso aos valores
print(numeros[0])  # 10
print(numeros[1])  # 20
⚠️ Diferença técnica (importante)
Lista (Python):
Pode ter tipos diferentes (int, float, string)
Tamanho dinâmico
Array “real” (outras linguagens / módulo específico):
Tipo fixo
Mais restrito
🔗 Ligando os dois conceitos
numeros = []

numeros.append(5)
numeros.append(10)
numeros.append(15)

📌 Resultado:

[5, 10, 15]

👉 Ou seja:

Você usa append() para colocar valores dentro do array (lista)
💡 Resumo direto
append() → adiciona item na lista
array/lista → guarda vários valores em uma variável
