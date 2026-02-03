import pandas as pd

def limpiar_nombres_columnas(df):
    """Normaliza nombres de columnas a minúsculas y guiones bajos."""
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]
    return df

def limpiar_clv(df,col):
    """Elimina el símbolo % y lo convierte a float."""
    if col in df.columns:
        df[col] = df[col].astype(str).str.replace('%', '', regex=False)
        df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

def limpiarpuntos(df,col):
    """Elimina el símbolo . de columna."""
    if col in df.columns:
        df[col] = df[col].astype(str).str.replace('.', '', regex=False)
        return df

def gestionar_nulos_y_duplicados(df):
    """Elimina duplicados y filas con valores nulos, reseteando el índice."""
    df = df.drop_duplicates().reset_index(drop=True)
    df = df.dropna().reset_index(drop=True)
    return df

def limpiar_texto(df):
    """Limpia espacios en blanco y pone en mayúsculas las columnas de texto."""
    for col in df.select_dtypes(include=['object']):
        df[col] = df[col].astype(str).str.strip().str.upper()
    return df

def informe_detallado(df):
    """Muestra el resumen final del DataFrame."""
    print("--- INFORME FINAL (2026) ---")
    print(f"Dimensiones finales: {df.shape}")
    print(f"Duplicados: {df.duplicated().sum()}")
    print(f"Nulos totales: {df.isnull().sum().sum()}")
    print("\nPrimeras filas:")
    print(df.head())


def categorico(df,col):
    """Realiza un análisis descriptivo de una columna categórica."""
    print(df[col].value_counts())
    print(df[col].unique())
    print(df[col].nunique())


def datos_nulos(df):
    """Muestra información sobre valores nulos, no nulos y duplicados."""
    print("datos nulos")
    print(df.isnull().sum())
    print("datos totales")
    print(df.count())   
    print("porcentaje de nulos")
    print(df.isnull().sum() / df.shape[0]*100)
    print("datos duplicados")
    print(df.duplicated().sum())


def columnas(df):
    """Muestra las columnas del DataFrame."""
    print(df.columns)
    print(len(df.columns))


def periodo(df,col):
    """Separa mes y año de la columna periodo."""
    df['Anyo'] = df[col].str[:4].astype(int)
    df['Mes'] = df[col].str[5:].astype(int)
    df = df.drop([col], axis=1)
    return df

def filtrar_fila(df,col,lista):
    return df[df[col].isin(lista)]

def completar_nulos(df,col,valor):
    df[col] = df[col].fillna(valor)
    return df

def eliminarletras(df,col):
    df[col] = df[col].str.replace(r'\D', '', regex=True).astype(int)
    return df

def año_estudio(df,col):
    df = df[df[col]>= 2018]
    return df

def cambiar_filas(df,col,valor1,valor2):
    """Cambia el valor de una columna con un valor específico."""
    df[col] = df[col].replace(valor1, valor2)
    return df
