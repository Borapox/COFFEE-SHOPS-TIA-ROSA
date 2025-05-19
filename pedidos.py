# pedidos.py
from dados import pedidos, salvar_dados_pedidos  # Importa o dicionário de pedidos e a função para salvar os dados

# Função para cadastrar um novo pedido
def cadastrar_pedido(id_cliente, id_produto, quantidade):
    novo_id = len(pedidos) + 1  # Atribui um ID único baseado na quantidade atual de pedidos
    pedidos[novo_id] = {
        "id_cliente": id_cliente,  # ID do cliente que fez o pedido
        "id_produto": id_produto,  # ID do produto pedido
        "quantidade": quantidade,  # Quantidade do produto pedido
    }
    salvar_dados_pedidos(pedidos)  # Salva os dados atualizados no arquivo JSON
    print(f"Pedido {novo_id} realizado com sucesso!")  # Exibe uma mensagem de sucesso

# Função para visualizar os pedidos cadastrados
def ver_pedidos():
    print("Lista de pedidos realizados:")
    if not pedidos:  # Verifica se o dicionário de pedidos está vazio
        print("Não há pedidos registrados.")
    else:
        # Itera sobre os pedidos e imprime suas informações
        for id_pedido, dados_pedido in pedidos.items():
            print(f"ID do Pedido: {id_pedido}")
            print(f"ID do Cliente: {dados_pedido['id_cliente']}")
            print(f"ID do Produto: {dados_pedido['id_produto']}")
            print(f"Quantidade: {dados_pedido['quantidade']}")
            print("-" * 20)
