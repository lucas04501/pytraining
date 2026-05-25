def disponibilidade(produto, produtos):
    for p in ["uva", "maçã", "pera"]:
        if produto == p:
            return "disponivel"
    return "indisponivel"

produtos = ["uva", "maçã", "pera"]
flag = True
while flag:
    produto = input("entre com um produto: ")
    if produto == "fim":
        flag = False
    else:
        print(disponibilidade(produto, produtos))
