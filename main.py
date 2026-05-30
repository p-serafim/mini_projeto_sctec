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

# SPRINT 2: TRANSFORMAÇÃO DE DADOS (STRINGS, NÚMEROS E DATAS)
# ==============================================================================
print("\n--- SPRINT 2: TRANSFORMANDO E LIMPANDO TIPOS DE DADOS ---\n")

# 1. Transformação de Datas (Datetime)
# Convertendo a coluna de data para o tipo datetime do pandas.
coluna_data = 'DATA' 
if coluna_data in df.columns:
    # errors='coerce' transforma erros ou formatos inválidos num valor nulo especial (NaT).
    df[coluna_data] = pd.to_datetime(df[coluna_data], dayfirst=True, errors='coerce')
    print(f"✓ Coluna '{coluna_data}' convertida para datetime (data real).")

# 2. Transformação de Strings usando métodos padrão
# Limpando espaços em branco e padronizando as letras na coluna Categoria
coluna_categoria = 'PR_CAT' 
if coluna_categoria in df.columns:
    df[coluna_categoria] = df[coluna_categoria].astype(str).str.strip().str.title()
    print(f"✓ Textos da coluna '{coluna_categoria}' padronizados.")

# 3. Expressões Regulares (Regex) para limpar o identificador de compra
# Garantindo que o CO_ID contenha apenas números.
coluna_id = 'CO_ID' 
if coluna_id in df.columns:
    # '\D' significa "tudo que NÃO for número". O regex vai substituir letras e símbolos por vazio.
    df[coluna_id] = df[coluna_id].astype(str).str.replace(r'\D', '', regex=True)
    # Convertendo de volta para numérico
    df[coluna_id] = pd.to_numeric(df[coluna_id], errors='coerce')
    print(f"✓ Regra de negócio aplicada: Apenas números extraídos de '{coluna_id}'.")

# Observação: Como a base não possui uma coluna de 'Valor' (R$), não faremos a conversão de float aqui,
# pois as numéricas (CL_FHL, CO_ID, etc.) já são do tipo int64.

# Mostrando como ficaram os tipos de dados após a faxina:
print("\nTipos de dados após as transformações (Sprint 2):")
print(df.dtypes)
print("\n" + "="*78 + "\n")


# (SPRINT 3..5 e DASHBOARD permanecerão comentados nesta etapa incremental.)
"""
# SPRINT 3: LIMPEZA DE NULOS E DUPLICATAS
# (conteúdo omitido nesta versão; será restaurado no commit seguinte)
"""

print("\n(Versão incremental: SPRINT 2 ativado neste commit.)")
