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
# SPRINT 3: LIMPEZA DE NULOS E DUPLICATAS
# ======================================================================
print("\n--- SPRINT 3: LIMPANDO NULOS E DUPLICATAS ---\n")

# 1. Verificando os dados nulos e duplicados ANTES da limpeza
print("Quantidade de valores nulos por coluna (ANTES):")
print(df.isnull().sum())
print(f"\nQuantidade de linhas duplicadas (ANTES): {df.duplicated().sum()}\n")

# 2. Remoção de linhas duplicadas
df = df.drop_duplicates()
print("✓ Linhas duplicadas exatas removidas da base.")

# 3. Tratamento de nulos com condicional (if/else) na coluna de Categoria
if coluna_categoria in df.columns:
    def preencher_categoria(valor):
        if pd.isna(valor) or str(valor).strip() == "" or str(valor).lower() == "nan":
            return "Sem Categoria"
        else:
            return valor
            
    df[coluna_categoria] = df[coluna_categoria].apply(preencher_categoria)
    print(f"✓ Valores nulos em '{coluna_categoria}' substituídos por 'Sem Categoria' (usando if/else).")

# 4. Tratamento de nulos em dimensões físicas com JUSTIFICATIVA
# Como a base não possui colunas de dimensão física, deixamos a lista vazia.
colunas_dimensoes = [] 

for col in colunas_dimensoes:
    if col in df.columns:
        # Optei por preencher as dimensões físicas nulas com o valor 0 (zero).
        # Motivo: Um valor nulo pode indicar que a medida não se aplica ou não foi informada.
        df[col] = df[col].fillna(0)
        print(f"✓ Nulos na dimensão física '{col}' preenchidos com 0.")

# 5. Verificando o resultado final da limpeza
print("\nQuantidade de valores nulos por coluna (DEPOIS):")
print(df.isnull().sum())
print(f"\nQuantidade de linhas duplicadas (DEPOIS): {df.duplicated().sum()}")
print("\n" + "="*78 + "\n")


# SPRINT 4: ESTATÍSTICA DESCRITIVA E AGRUPAMENTOS
# ======================================================================
print("\n--- SPRINT 4: ESTATÍSTICA DESCRITIVA E AGRUPAMENTOS ---\n")

# 1. Estatística Descritiva para a coluna "Número de filhos"
coluna_filhos = 'CL_FHL' # Usando a coluna exata da sua base

if coluna_filhos in df.columns:
    print(f"1. Estatísticas Descritivas para a coluna '{coluna_filhos}':")
    
    # Garantindo que a coluna seja tratada como número
    df[coluna_filhos] = pd.to_numeric(df[coluna_filhos], errors='coerce')
    
    # Calculando os parâmetros exigidos
    contagem = df[coluna_filhos].count()
    media = df[coluna_filhos].mean()
    mediana = df[coluna_filhos].median()
    desvio_padrao = df[coluna_filhos].std()
    moda = df[coluna_filhos].mode()[0]
    minimo = df[coluna_filhos].min()
    maximo = df[coluna_filhos].max()
    quartil_25 = df[coluna_filhos].quantile(0.25)
    quartil_50 = df[coluna_filhos].quantile(0.50) # Equivalente à mediana
    quartil_75 = df[coluna_filhos].quantile(0.75)
    
    # Exibindo os resultados formatados
    print(f"  - Contagem: {contagem}")
    print(f"  - Média: {media:.2f}")
    print(f"  - Mediana: {mediana}")
    print(f"  - Desvio Padrão: {desvio_padrao:.2f}")
    print(f"  - Moda: {moda}")
    print(f"  - Mínimo: {minimo}")
    print(f"  - Máximo: {maximo}")
    print(f"  - 1º Quartil (25%): {quartil_25}")
    print(f"  - 2º Quartil (50%): {quartil_50}")
    print(f"  - 3º Quartil (75%): {quartil_75}\n")
else:
    print(f"AVISO: Coluna '{coluna_filhos}' não encontrada.\n")

# 2. Explorando Padrões de Agrupamento
print("2. Padrões de Agrupamento:\n")

# Agrupamento A: Quantidade de produtos vendidos por Categoria (já que não temos 'Valor')
if coluna_categoria in df.columns:
    # Agrupamos por Categoria e contamos o número de identificadores (CO_ID)
    vendas_por_categoria = df.groupby(coluna_categoria)['CO_ID'].count().reset_index()
    vendas_por_categoria.columns = [coluna_categoria, 'Qtd_Vendida']
    vendas_por_categoria = vendas_por_categoria.sort_values(by='Qtd_Vendida', ascending=False)
    
    print(f"A) Quantidade de Vendas por Categoria ('{coluna_categoria}'):")
    print(vendas_por_categoria.to_string(index=False))
    print("\n")

# Agrupamento B: Contagem de compras e Média de Filhos por Gênero usando pivot_table()
coluna_genero = 'CL_GENERO'

if coluna_genero in df.columns and coluna_filhos in df.columns:
    # Pivot table usando a coluna filhos para calcular a média, e o próprio CL_FHL para contar os registros
    agrupamento_genero = pd.pivot_table(
        df, 
        values=coluna_filhos, 
        index=coluna_genero, 
        aggfunc=['count', 'mean']
    )
    # Renomeando colunas pra ficar mais bonito no terminal
    agrupamento_genero.columns = ['Qtd_Compras_Registradas', 'Media_de_Filhos']
    
    print(f"B) Análise por Gênero ('{coluna_genero}'):")
    print(agrupamento_genero.round(2))
    print("\n" + "="*78 + "\n")


# SPRINT 5: RELATÓRIO FINAL E EXPORTAÇÃO DOS DADOS LIMPOS
# ======================================================================
print("\n--- SPRINT 5: RELATÓRIO FINAL E EXPORTAÇÃO ---\n")

# Construção dos contadores do relatório final
linhas_finais = df.shape[0]
linhas_removidas = linhas - linhas_finais

print("Resumo do Processamento (Contadores Finais):")
print(f"  - Total de registros originais: {linhas}")
print(f"  - Total de registros após limpeza: {linhas_finais}")
print(f"  - Registros removidos (duplicados): {linhas_removidas}")
print(f"  - Total de colunas analisadas: {df.shape[1]}\n")

# Exportando a base de dados limpa (df_limpo) conforme exigido para a entrega
nome_arquivo_limpo = 'base_varejo_limpa.csv'
try:
    df.to_csv(nome_arquivo_limpo, index=False, encoding='utf-8')
    print(f"✓ Base de dados limpa exportada com sucesso para o arquivo: '{nome_arquivo_limpo}'")
except Exception as e:
    print(f"Erro ao exportar o arquivo: {e}")

print("\n" + "="*78)
print(" ANÁLISE EXPLORATÓRIA CONCLUÍDA COM SUCESSO! ")
print(" Verifique o arquivo README.md para a reflexão teórica e os insights.")
print("="*78 + "\n")


# =====================================================================
# DASHBOARD GRÁFICO (VISUALIZAÇÃO DOS DADOS)
# =====================================================================
print("\n--- GERANDO DASHBOARD GRÁFICO ---\n")

# Cria uma figura grande para acomodar 3 gráficos diferentes (1 linha, 3 colunas)
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(18, 6))
fig.canvas.manager.set_window_title('Dashboard de Análise de Varejo') # Título da janela


# =====================================================================
# ANÁLISE 1: Produtos mais vendidos (Volume de compras por Categoria)
# =====================================================================
# Agrupado por Categoria do Produto e contamos quantas Notas Fiscais (CO_ID) existem
vendas_por_categoria_grafico = df.groupby('PR_CAT')['CO_ID'].count().sort_values(ascending=False)

# Gerado um gráfico de barras no primeiro espaço (axes[0])
vendas_por_categoria_grafico.plot(kind='bar', ax=axes[0], color='skyblue', edgecolor='black')
axes[0].set_title('Top Categorias Mais Vendidas', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Categoria do Produto')
axes[0].set_ylabel('Quantidade de Vendas (Notas)')
axes[0].tick_params(axis='x', rotation=45) # Inclina o texto do eixo X para não encavalar


# =====================================================================
# ANÁLISE 2: Distribuição de Clientes por Classe Econômica
# =====================================================================
# Agrupado pela Classe (CL_SEG) e contamos os clientes ÚNICOS (nunique)
# Usado nunique() no CL_ID para não contar o mesmo cliente duas vezes se ele comprou mais de uma vez.
clientes_por_segmento = df.groupby('CL_SEG')['CL_ID'].nunique()

# Gerado um gráfico de pizza no segundo espaço (axes[1])
clientes_por_segmento.plot(kind='pie', ax=axes[1], autopct='%1.1f%%', startangle=90, cmap='Set3')
axes[1].set_title('Divisão de Clientes por Classe (A, B, C)', fontsize=12, fontweight='bold')
axes[1].set_ylabel('') # Tira o rótulo lateral do eixo Y que fica feio em gráfico de pizza


# =====================================================================
# ANÁLISE 3: Preferência de Categoria por Gênero
# =====================================================================
# Agrupado por Categoria E Gênero, contamos as vendas e usamos .unstack() 
# para colocar os Gêneros lado a lado nas colunas
cat_por_genero = df.groupby(['PR_CAT', 'CL_GENERO'])['CO_ID'].count().unstack()

# Gerado um gráfico de barras agrupadas no terceiro espaço (axes[2])
cat_por_genero.plot(kind='bar', ax=axes[2], stacked=False, colormap='viridis', edgecolor='black')
axes[2].set_title('Vendas por Categoria e Gênero', fontsize=12, fontweight='bold')
axes[2].set_xlabel('Categoria do Produto')
axes[2].set_ylabel('Quantidade de Vendas')
axes[2].legend(title='Gênero')
axes[2].tick_params(axis='x', rotation=45)


# =====================================================================
# AJUSTES FINAIS E EXIBIÇÃO DA TELA
# =====================================================================
# Ajusta o espaçamento entre os gráficos para não ficar nada sobreposto
plt.tight_layout()

# Mantendo a janela aberta após execução script para que o usuário possa analisar os gráficos.
# Ele exibe a interface gráfica e "trava" o script até você fechar no 'X' da janela.
print("\nAbrindo os gráficos... Feche a janela de gráficos para encerrar o script.")
plt.show()

print("\n(Versão incremental: SPRINT 6 - DASHBOARD ativado neste commit.)")
