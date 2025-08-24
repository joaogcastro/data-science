import pandas as pd

# Carregar o dataset enviado
file_path = "dataset/Salaries.csv"
# Campos com number e string na mesma coluna, precisa normalizar 
# DtypeWarning: Columns (3,4,5,6,12) have mixed types. Specify dtype option on import or set low_memory=False.
df = pd.read_csv(file_path, low_memory=False)

# Visualizar primeiras linhas antes da limpeza
print(df.head())

# Limpeza simples: remover valores nulos e duplicados
df_clean = df.dropna().drop_duplicates()

# Mostrar informações do dataset limpo
print(df_clean.info())
df_clean_info = {
    "shape_antes": df.shape,
    "shape_depois": df_clean.shape,
    "colunas": df.columns.tolist()
}

df_clean_info

#