# produtos.py
from dados import produtos, salvar_dados_produtos  # Importa os dados de produtos e a função para salvar os dados

# Função para cadastrar um novo produto
def cadastrar_produto(nome, preco):
    novo_id = len(produtos) + 1  # Atribui um ID único baseado na quantidade atual de produtos
    produtos[novo_id] = {
        "nome": nome,  # Nome do produto
        "preco": preco  # Preço do produto
    }
    salvar_dados_produtos(produtos)  # Salva os dados atualizados no arquivo JSON
    print(f"Produto {nome} cadastrado com sucesso!")  # Exibe uma mensagem de sucesso

# Função para visualizar os produtos cadastrados
def ver_produtos():
    print("Lista de produtos cadastrados:")
    if not produtos:  # Verifica se o dicionário de produtos está vazio
        print("Não há produtos cadastrados.")
    else:
        # Itera sobre os produtos e imprime suas informações
        for id_produto, dados_produto in produtos.items():
            print(f"ID: {id_produto}")
            print(f"Nome: {dados_produto['nome']}")
            print(f"Preço: R${dados_produto['preco']:.2f}")
            print("-" * 20)
