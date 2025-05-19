# Sistema de Pedidos da Cafeteria
# A ideia é ter um jeito simples de registrar quem pediu o quê, quanto, e o total da conta.

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
        print("Escolha uma opção:")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # Abre a tela pra fazer um novo pedido.
            fazer_pedido()
        elif opcao == "2":
            # Mostra todos os pedidos feitos até agora.
            ver_pedidos()
        elif opcao == "3":
            # Cadastra um novo cliente.
            cadastrar_cliente()
        elif opcao == "4":
            # Lista os clientes já cadastrados.
            ver_clientes()
        elif opcao == "5":
            # Adiciona um novo produto ao cardápio.
            cadastrar_produto()
        elif opcao == "6":
            # Mostra os produtos disponíveis.
            ver_produtos()
        elif opcao == "0":
            # Encerra o sistema.
            print("Saindo do sistema...")
            break
        else:
            # Se a opção não existir, avisa o usuário.
            print("Opção inválida. Tente novamente.")

def fazer_pedido():
    print("Fazendo um pedido...")
    # Coleta os itens do pedido, calcula o total e salva.
    pass

def ver_pedidos():
    print("Ver pedidos...")
    # Mostra todos os pedidos já feitos.
    pass

def cadastrar_cliente():
    print("Cadastrando cliente...")
    # Pega os dados do cliente e salva no sistema.
    pass

def ver_clientes():
    print("Ver clientes...")
    # Lista todos os clientes cadastrados.
    pass

def cadastrar_produto():
    print("Cadastrando produto...")
    # Adiciona um novo item ao cardápio com nome e preço.
    pass

def ver_produtos():
    print("Ver produtos...")
    # Mostra todos os produtos disponíveis pra venda.
    pass

if __name__ == "__main__":
    # Ponto de partida do sistema. Inicia o menu.
    menu()
