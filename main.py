from dados import clientes, produtos, pedidos  # Importa os dicionários de dados
from dados import salvar_dados_clientes, salvar_dados_produtos, salvar_dados_pedidos  # Importa funções de salvar

from clientes import cadastrar_cliente  # Importa a função de cadastrar cliente
from produtos import cadastrar_produto, ver_produtos  # Importa as funções de produtos

def menu():
    # Mostra o menu principal e espera o usuário escolher uma opção.
    while True:
        print("Bem-vindo ao sistema de pedidos da cafeteria!")
        print("1. Fazer um pedido")
        print("2. Ver pedidos")
        print("3. Cadastrar cliente")
        print("4. Ver clientes")
        print("5. Cadastrar produto")
        print("6. Ver produtos")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Abre a tela para fazer um novo pedido.
            fazer_pedido()
        elif opcao == "2":
            # Mostra todos os pedidos feitos até agora.
            ver_pedidos()
        elif opcao == "3":
            # Cadastra um novo cliente.
            cadastrar_novo_cliente()
        elif opcao == "4":
            # Lista os clientes já cadastrados.
            ver_clientes()
        elif opcao == "5":
            # Adiciona um novo produto ao cardápio.
            cadastrar_novo_produto()
        elif opcao == "6":
            # Mostra os produtos disponíveis.
            ver_produtos()
        elif opcao == "7":
            # Encerra o sistema.
            print("Saindo do sistema...")
            break
        else:
            # Se a opção não existir, avisa o usuário.
            print("Opção inválida. Tente novamente.")

def cadastrar_novo_produto():
    # Coleta as informações necessárias para o produto
    nome = input("Nome do produto: ").strip()
    preco = float(input("Preço do produto: R$").strip())
    
    # Chama a função para cadastrar o produto
    cadastrar_produto(nome, preco)
    
    print(f"Produto {nome} cadastrado com sucesso!")
    input("Pressione Enter para voltar ao menu principal...")
    print()

def fazer_pedido():
    print("Fazendo um pedido...")
    # Pede os dados do cliente para fazer o pedido
    id_cliente = int(input("Informe o ID do cliente: "))
    if id_cliente not in clientes:
        print("Cliente não encontrado.")
        return
    
    print("Selecione os produtos para o pedido:")
    ver_produtos()
    id_produto = int(input("Informe o ID do produto: "))
    if id_produto not in produtos:
        print("Produto não encontrado.")
        return

    quantidade = int(input("Informe a quantidade: "))

    # Cria o pedido
    pedido = {
        "id_cliente": id_cliente,
        "id_produto": id_produto,
        "quantidade": quantidade,
        "total": produtos[id_produto]["preco"] * quantidade
    }

    # Gera um ID único para o pedido
    novo_id_pedido = len(pedidos) + 1
    pedidos[novo_id_pedido] = pedido

    # Salva os dados de pedidos
    salvar_dados_pedidos(pedidos)

    print(f"Pedido realizado com sucesso! ID do pedido: {novo_id_pedido}")
    input("Pressione Enter para voltar ao menu principal...")

def ver_pedidos():
    print("Lista de pedidos realizados:")
    if not pedidos:  # Verifica se o dicionário de pedidos está vazio
        print("Não há pedidos realizados.")
    else:
        for id_pedido, pedido in pedidos.items():
            cliente = clientes[pedido["id_cliente"]]
            produto = produtos[pedido["id_produto"]]
            print(f"ID: {id_pedido}")
            print(f"Cliente: {cliente['nome']}")
            print(f"Produto: {produto['nome']}")
            print(f"Quantidade: {pedido['quantidade']}")
            print(f"Total: R${pedido['total']:.2f}")
            print("-" * 20)

def cadastrar_novo_cliente():
    # Pede os dados do cliente para cadastro
    nome = input("Nome do cliente: ").strip()
    cpf = input("CPF: ").strip()
    telefone = input("Telefone: ").strip()
    endereco = input("Endereço: ").strip()

    # Chama a função de cadastro no arquivo clientes.py
    cadastrar_cliente(nome, cpf, telefone, endereco)

    # Confirmação do cadastro e retorno ao menu
    print(f"Cliente {nome} cadastrado com sucesso!")
    input("Pressione Enter para voltar ao menu principal...")
    print()

def ver_clientes():
    print("Lista de clientes cadastrados:")
    if not clientes:
        print("Não há clientes cadastrados.")
    else:
        for id_cliente, dados_cliente in clientes.items():
            print(f"ID: {id_cliente}")
            print(f"Nome: {dados_cliente['nome']}")
            print(f"CPF: {dados_cliente['cpf']}")
            print(f"Telefone: {dados_cliente['telefone']}")
            print(f"Endereço: {dados_cliente['endereco']}")
            print("-" * 20)

if __name__ == "__main__":
    menu()
