import produtos  # Importa as funções de produtos
from dados import clientes  # Importa o dicionário de clientes de dados.py
from clientes import cadastrar_cliente  # Importa a função de cadastrar cliente de clientes.py
from produtos import cadastrar_produto, ver_produtos  # Importa as funções de produtos
from dados import salvar_dados_clientes  # Importa a função de salvar dados de clientes
from dados import salvar_dados_produtos  # Importa a função de salvar dados de produtos
from dados import pedidos  # Importa o dicionário de pedidos de dados.py


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
            # Abre a tela pra fazer um novo pedido.
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
            cadastrar_novo_produto()  # Corrigido para chamar a função correta
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

def ver_pedidos():
    print("Ver pedidos...")

def cadastrar_novo_cliente():
    # Pede os dados do cliente para cadastro
    nome = input("Nome do cliente: ").strip()
    cpf = input("CPF: ").strip()
    telefone = input("Telefone: ").strip()
    endereco = input("Endereço: ").strip()

    # Chama a função de cadastro no arquivo clientes.py
    cadastrar_cliente(nome, cpf, telefone, endereco)  # Passa os dados coletados para o cadastro

    # Confirmação do cadastro e retorno ao menu
    print(f"Cliente {nome} cadastrado com sucesso!")
    input("Pressione Enter para voltar ao menu principal...")  # Aguarda o usuário pressionar Enter para continuar
    print()  # Linha em branco para clareza

def ver_clientes():
    print("Lista de clientes cadastrados:")
    if not clientes:  # Verifica se o dicionário de clientes está vazio
        print("Não há clientes cadastrados.")
    else:
        for id_cliente, dados_cliente in clientes.items():
            print(f"ID: {id_cliente}")
            print(f"Nome: {dados_cliente['nome']}")
            print(f"CPF: {dados_cliente['cpf']}")
            print(f"Telefone: {dados_cliente['telefone']}")
            print(f"Endereço: {dados_cliente['endereco']}")
            print("-" * 20)

def ver_produtos():
    print("Lista de produtos cadastrados:")
    if not produtos:  # Verifica se o dicionário de produtos está vazio
        print("Não há produtos cadastrados.")
    else:
        for id_produto, dados_produto in produtos.items():
            print(f"ID: {id_produto}")
            print(f"Nome: {dados_produto['nome']}")
            print(f"Preço: R${dados_produto['preco']:.2f}")
            print("-" * 20)

if __name__ == "__main__":
    menu()
