# dados.py
import json

# Função para carregar os dados dos clientes do arquivo JSON
def carregar_dados_clientes():
    try:
        with open('dados_clientes.json', 'r') as f:
            dados = json.load(f)  # Carrega o conteúdo do arquivo JSON
            # Converte as chaves para inteiros para garantir consistência no tipo de chave
            return {int(k): v for k, v in dados.items()}
    except FileNotFoundError:
        # Se o arquivo não existir, retorna um dicionário vazio
        return {}

# Função para salvar os dados dos clientes no arquivo JSON
def salvar_dados_clientes(dados):
    # Converte as chaves para string antes de salvar no arquivo
    dados_str = {str(k): v for k, v in dados.items()}
    with open('dados_clientes.json', 'w') as f:
        json.dump(dados_str, f, indent=4)  # Salva o dicionário como JSON no arquivo

# Função para carregar os dados dos produtos do arquivo JSON
def carregar_dados_produtos():
    try:
        with open('dados_produtos.json', 'r') as f:
            dados = json.load(f)  # Carrega o conteúdo do arquivo JSON
            # Converte as chaves para inteiros para garantir consistência no tipo de chave
            return {int(k): v for k, v in dados.items()}
    except FileNotFoundError:
        # Se o arquivo não existir, retorna um dicionário vazio
        return {}

# Função para salvar os dados dos produtos no arquivo JSON
def salvar_dados_produtos(dados):
    # Converte as chaves para string antes de salvar no arquivo
    dados_str = {str(k): v for k, v in dados.items()}
    with open('dados_produtos.json', 'w') as f:
        json.dump(dados_str, f, indent=4)  # Salva o dicionário como JSON no arquivo

# Inicializa os dicionários de clientes e produtos carregando os dados dos arquivos JSON
clientes = carregar_dados_clientes()
produtos = carregar_dados_produtos()
