# ==============================================================================
# SPRINT 1: IMPORTAÇÃO DOS DADOS E EXPLORAÇÃO INICIAL
# ==============================================================================

# Importando as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt # Adicionado para gerar o Dashboard

# Definindo o nome do arquivo da nossa base de dados.
# Certifique-se de que o script e este arquivo .csv estão na mesma pasta.
caminho_arquivo = 'base_varejo.csv'

# Usando a função read_csv do pandas para ler o arquivo e guardar em uma variável chamada 'df'.
# Adicionado o parâmetro sep=';' pois é o padrão de separação da sua base.
df = pd.read_csv(caminho_arquivo, sep=';')

# Exibindo informações básicas solicitadas nas instruções do desafio:
print("--- SPRINT 1: INFORMAÇÕES INICIAIS DA BASE DE DADOS ---\n")

# 1. Número de registros (linhas) e colunas
# O atributo .shape retorna uma tupla (linhas, colunas)
linhas, colunas = df.shape
print(f"Número de registros (linhas): {linhas}")
print(f"Número de colunas: {colunas}\n")

# 2. Mostrando os nomes das colunas e os tipos de dados de cada uma
# O atributo .dtypes lista o tipo de dado de cada coluna (int64, float64, object(string), etc.)
print("Tipos de dados por coluna:")
print(df.dtypes)
print("\n")

# Mostrando as 5 primeiras linhas 
print("Visualização das 5 primeiras linhas da tabela:")
print(df.head())


# ==============================================================================
# SPRINT 2: TRANSFORMAÇÃO DE DADOS (STRINGS, NÚMEROS E DATAS)
# ==============================================================================

# (Os blocos SPRINT 2..5 e DASHBOARD estão temporariamente comentados nesta versão)
# Para simular desenvolvimento incremental, este commit mantém apenas SPRINT 2 como comentário
# e exibe uma mensagem de placeholder. Os blocos reais serão restaurados nos commits seguintes.

print("\n(SPRINT 2..5 e DASHBOARD comentados nesta versão incremental.)")

# (restante do código foi movido para commits posteriores)
