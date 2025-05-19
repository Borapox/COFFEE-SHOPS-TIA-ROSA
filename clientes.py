#Lista de clientes cadastrados na cafeteria
# Cada cliente é representado por um dicionário com informações como nome, CPF, telefone e endereço

from dados import clientes


def cadastrar_cliente(nome, cpf, telefone, endereco):

    novo_id = len(clientes) + 1
    clientes[novo_id]= {
        "nome": nome,
        "cpf": cpf,
        "telefone": telefone,
        "endereco": endereco,
    }
    print(f"Cliente {nome} cadastrado com sucesso!")

def ver_clientes():
    print("Lista de clientes cadastrados:")
    for id_cliente, dados_cliente in clientes.items():
        print(f"ID: {id_cliente}")
        print(f"Nome: {dados_cliente['nome']}")
        print(f"CPF: {dados_cliente['cpf']}")
        print(f"Telefone: {dados_cliente['telefone']}")
        print(f"Endereço: {dados_cliente['endereco']}")
        print("-" * 20)

