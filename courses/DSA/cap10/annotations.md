# Pandas

DOCS: https://pandas.pydata.org/docs/

O pandas é uma das bibliotecas mais utilizadas para a manipulação de dados.

## Dataframes
Dataframes são tabelas de linha e coluna contendo dados

## funções e atributos
- pd.DataFrame(, dados **columns, **index)
- pd.read_csv()
- df.head()
- df.tail()
- df.dtypes
- df.columns
- df.values
- df.filter()
- df.describe()
- df.isna()
- df.fillna()
- df.value_counts(by="Coluna") -> conta os valores de uma certa coluna
- df.shape -> tamanho do dataframe
- df.isin()
- df.sample()
- df.groupby()
- column.mean()
- column.count()
- columns.std()
- groupby().agg() -> para colocar várias medidas em um groupby só
- df.index -> retorna só os indexes
- df.items() -> retorna o dataframe em lista
- df.tolist() -> tranforma o dataframe em lista
- series.reset_index() -> para transformar um series em dataframe depois de um groupby
- column.str.startswith()
- column.str.endswith()
- column.value_counts()
