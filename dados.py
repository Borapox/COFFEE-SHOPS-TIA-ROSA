# dados.py
import json

# Função para carregar os dados do arquivo
def carregar_dados():
    try:
        with open('dados.json', 'r') as f:
            dados = json.load(f)
            # Certifique-se de que as chaves são convertidas para inteiros
            return {int(k): v for k, v in dados.items()}
    except FileNotFoundError:
        # Caso o arquivo não exista, retorna um dicionário vazio
        return {}

# Função para salvar os dados no arquivo
def salvar_dados(dados):
    # Converte as chaves para string antes de salvar
    dados_str = {str(k): v for k, v in dados.items()}
    with open('dados.json', 'w') as f:
        json.dump(dados_str, f, indent=4)

# Inicializa o dicionário de clientes
clientes = carregar_dados()  # Carrega os dados do arquivo JSON
