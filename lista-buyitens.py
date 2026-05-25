# Código resumido: conta produtos informados pelo usuário até digitar "fim".
def main():
	# cria um dicionário vazio para armazenar a contagem de cada produto
	counts = {}

	# loop principal: continua pedindo produtos até o usuário encerrar
	while True:
		try:
			# lê uma linha do usuário e remove espaços extras nas extremidades
			item = input("Produto (ou 'fim' para encerrar): ").strip()
		except EOFError:
			# se o input acabar (e.g. EOF), interrompe o loop
			break

		# se o usuário digitou 'fim' (independente de maiúsculas/minúsculas), encerra
		if item.lower() == 'fim':
			break

		# se a entrada estiver vazia (apenas enter), ignora e continua
		if not item:
			continue

		# incrementa a contagem do produto no dicionário
		counts[item] = counts.get(item, 0) + 1

	# após sair do loop, verifica se há produtos registrados
	if counts:
		# imprime cabeçalho simples
		print('\nContagem de produtos:')
		# ordena por quantidade decrescente e, em caso de empate, por nome
		for product, cnt in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
			# mostra o produto e sua contagem
			print(f"{product}: {cnt}")
	else:
		# caso nenhum produto tenha sido informado
		print('Nenhum produto informado.')


# ponto de entrada: executa main() apenas quando o arquivo for executado diretamente
if __name__ == '__main__':
	main()

