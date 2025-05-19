from dados import clientes  # Importa o dicionário de clientes de dados.py
from clientes import cadastrar_cliente  # Importa a função de cadastrar cliente de clientes.py


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
            cadastrar_produto()
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


def cadastrar_produto():
    print("Cadastrando produto...")

def ver_produtos():
    print("Ver produtos...")

if __name__ == "__main__":
    menu()
