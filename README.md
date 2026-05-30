## **Análise Exploratória de Dados (AED) - Varejo** 🛒📊

Aluno(a): PAULO ROBERTO SERAFIM

Turma: Análise de Dados com Python [T1]

Módulo: 1 - Semana 07

## 🎯 **Sobre o Projeto**

Este repositório contém um mini-projeto de Análise Exploratória de Dados (AED) aplicado a uma base de dados de varejo. O objetivo é demonstrar a aplicação prática de processos de ETL (Extract, Transform, Load) utilizando Python. O script processa os dados brutos, realiza tratamentos e limpezas avançadas, extrai estatísticas, exporta uma base higienizada e, por fim, gera um Dashboard interativo com os resultados.

## 🚀 **Como executar este projeto**

Para rodar este script localmente na sua máquina, siga o passo a passo abaixo:

**1. Pré-requisitos**

Certifique-se de ter o Python (versão 3.8 ou superior) instalado no seu computador.
Você precisará de duas bibliotecas externas: pandas (para manipulação de dados) e matplotlib (para geração dos gráficos).

Abra o terminal do seu sistema ou do VS Code e instale as dependências com o comando:
```bash
pip install pandas matplotlib
```

**2. Executando o Script**

Faça o download ou clone este repositório.

Certifique-se de que os arquivos ```main.py``` e ```base_varejo.csv``` estão na mesma pasta.

No terminal, navegue até a pasta do projeto e execute:
```bash
python main.py
```

Acompanhe o log (relatório) gerado no terminal detalhando todas as etapas de limpeza.

Ao final, a janela do Dashboard será aberta com 3 gráficos. Feche a janela dos gráficos para que o script seja encerrado e o arquivo base_varejo_limpa.csv seja salvo na sua pasta.

## 🔍 **Entendendo o Código Passo a Passo**

O script principal (main.py) foi estruturado em 5 Sprints e um bloco final de visualização. Abaixo, detalhamos o que cada função e parte do código realiza:

## 📥 **SPRINT 1: Importação e Exploração Inicial**

import pandas as pd e import matplotlib.pyplot as plt: Importa as bibliotecas fundamentais do projeto.

pd.read_csv(..., sep=';'): Função do pandas responsável por carregar o arquivo CSV para a memória, criando um "DataFrame" (uma tabela de dados). O parâmetro sep=';' garante que as colunas sejam separadas corretamente, já que a base usa ponto e vírgula.

df.shape: Retorna uma tupla contendo o número total de linhas e colunas da tabela.

df.dtypes: Lista o tipo de dado de cada coluna (ex: inteiro, texto/objeto, decimal), ajudando a identificar o que precisa ser convertido nas próximas etapas.

## 🧹 **SPRINT 2: Transformação de Dados e Regex**

Nesta etapa, formatamos os dados para os tipos corretos do Python:

pd.to_datetime(..., dayfirst=True, errors='coerce'): Converte a coluna de data (que vem como texto) para o formato oficial de data do Python. O coerce transforma formatos inválidos em nulos (NaT) para não quebrar o código.

.str.strip().str.title(): Encadeamento de métodos de texto que removem espaços em branco nas pontas e padronizam a escrita (Primeira Letra Maiúscula) das categorias.

.str.replace(r'\D', '', regex=True): Uso de Expressões Regulares (Regex). O \D encontra "tudo que não for número" e substitui por vazio, garantindo que o ID da compra contenha apenas números puros.

## 🧽 **SPRINT 3: Tratamento de Nulos e Duplicatas**

df.isnull().sum() e df.duplicated().sum(): Funções de diagnóstico para contar onde estão os "buracos" e as repetições na base de dados.

df.drop_duplicates(): Remove todas as linhas que são cópias exatas de outra, mantendo apenas a primeira ocorrência.

Função Condicional preencher_categoria(valor): Uma função customizada aplicada através de df.apply(). Ela usa a lógica if/else para verificar se a categoria está nula (pd.isna) ou vazia. Se estiver, preenche automaticamente com a string "Sem Categoria".

df.fillna(0): Preenche valores nulos em colunas numéricas (como dimensões físicas, se existissem) com zero, justificando que a ausência de valor significa ausência da medida.

## 📈 **SPRINT 4: Estatística Descritiva e Agrupamentos**

Estatísticas (Média, Moda, Quartis): O código aplica funções matemáticas nativas do pandas sobre a coluna de número de filhos: .mean() (média), .median() (mediana), .std() (desvio padrão), .min() / .max(), e .quantile(0.25) para calcular os quartis estatísticos.

df.groupby('PR_CAT')['CO_ID'].count(): Agrupa os dados por Categoria e conta o número de IDs, respondendo à pergunta "Quantos produtos foram vendidos por categoria?".

pd.pivot_table(..., aggfunc=['count', 'mean']): Cria uma tabela dinâmica (pivot) cruzando o "Gênero" com a coluna de "Filhos", aplicando duas operações simultâneas: contagem de clientes e a média de filhos por gênero.

## 💾 **SPRINT 5: Relatório e Exportação (Load)**

df.to_csv('base_varejo_limpa.csv', index=False): Pega todo o DataFrame limpo que está na memória do Python e cria um novo arquivo CSV físico na pasta do computador. O index=False impede que o índice numérico do pandas vire uma coluna inútil no arquivo final.

## 📊 **DASHBOARD: Visualização de Dados (Matplotlib)**

plt.subplots(nrows=1, ncols=3): Cria a "tela" do nosso painel com espaço para 3 gráficos alinhados lado a lado.

.plot(kind='bar') e .plot(kind='pie'): Usa a integração do pandas com o matplotlib para gerar rapidamente gráficos de barras e de pizza a partir dos agrupamentos que fizemos.

plt.show(): É o comando que efetivamente renderiza a janela na tela do usuário e pausa a execução do script até a janela ser fechada.


## 💡 **Reflexão e Principais Insights**

O tratamento de dados (ETL) provou-se essencial. A limpeza eliminou distorções e garantiu métricas precisas para a análise. A partir dos dados higienizados, observamos que:

Eficiência do Tratamento: A etapa de limpeza identificou e removeu 96.553 linhas duplicadas da base bruta original, evitando um superdimensionamento irreal das métricas e garantindo a qualidade da informação analisada.

Categorias de Maior Impacto: A categoria mais vendida foi corretamente identificada como Alimentos, liderando o ranking de forma isolada com 384.197 vendas registradas.

Perfil Familiar: O perfil médio do cliente analisado possui cerca de 1.15 filhos, com um desvio padrão de 1.42. No entanto, a moda (valor mais repetido) ficou em 0, indicando que a maioria absoluta das transações é feita por clientes que não declaram filhos.

Comportamento por Gênero: O cruzamento de dados na Pivot Table revelou que o público Feminino (F) lidera o volume de compras na base, com um total de 382.427 registros válidos. Por outro lado, o público Masculino (M) apresenta uma média ligeiramente maior de filhos (1.21 contra 1.09).
