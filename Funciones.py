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
    
def cambiocoma_punto(df,col):
    """Cambia el símbolo , por ."""
    if col in df.columns:
        df[col] = df[col].astype(str).str.replace(',', '.', regex=False).astype(float)
        return df    

def espacios(df,col):
    """Elimina espacios en blanco de columna."""
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()
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

def informe(df):
    """Muestra información detallada sobre el DataFrame."""
    print("Información del DataFrame:")
    print(df.info())
    print("Valores nulos:")
    print(df.isnull().sum())
    print("Tipos de datos:")
    print(df.dtypes)
    print("Primeras 5 filas:")
    print(df.head())
    print("Últimas 5 filas:")
    print(df.tail())
    print("Forma del DataFrame:")
    print(df.shape)
    print("columnas")
    print(df.columns)
    print("numericos")
    print(df.select_dtypes(include=["number"]).columns)


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
    """Cambia el valor de una fila con un valor específico."""
    df[col] = df[col].replace(valor1, valor2)
    return df

def estadisticos(df):
    print(df.describe())
    print(df.select_dtypes(include=["number"]).describe())
    

def asignar_secciones(df):
    mapeo_productos = {
        'Arroz': 'Arroz, legumbres y pasta',
        'Harinas y otros cereales': 'Arroz, legumbres y pasta',
        'Pan': 'Panadería y pastelería',
        'Otros productos de panadería': 'Panadería y pastelería',
        'Otros productos elaborados con cereales n.c.o.p.': 'Cereales y galletas',
        'Pizzas y quiches': 'Pizzas y platos preparados',
        'Pastas alimenticias y cuscús': 'Arroz, legumbres y pasta',
        'Cereales de desayuno': 'Cereales y galletas',
        'Carne de vacuno': 'Carne', 'Carne de porcino': 'Carne', 
        'Carne de ovino y caprino': 'Carne', 'Carne de ave': 'Carne',
        'Otras carnes': 'Carne', 'Despojos y menudillos': 'Carne',
        'Charcutería y carne seca, salada o ahumada': 'Charcutería y quesos',
        'Carne procesada y otras preparaciones a base de carne': 'Carne',
        'Pescado fresco o refrigerado': 'Marisco y pescado',
        'Pescado congelado': 'Congelados',
        'Pescado y marisco seco, ahumado o salado': 'Marisco y pescado',
        'Pescado y marisco procesado y otras preparaciones de pescado y marisco': 'Marisco y pescado',
        'Marisco fresco o refrigerado': 'Marisco y pescado',
        'Marisco congelado': 'Congelados',
        'Leche entera': 'Huevos, leche y mantequilla',
        'Leche semidescremada y descremada': 'Huevos, leche y mantequilla',
        'Leche conservada': 'Huevos, leche y mantequilla',
        'Yogures': 'Postres y yogures','Queso': 'Charcutería y quesos',
        'Huevos': 'Huevos, leche y mantequilla',
        'Otros productos a base de leche' : 'Huevos, leche y mantequilla',
        'Mantequilla y otras grasas animales': 'Huevos, leche y mantequilla',
        'Margarina y otras grasas vegetales': 'Huevos, leche y mantequilla',
        'Aceite de oliva': 'Aceite, especias y salsas',
        'Otros aceites': 'Aceite, especias y salsas',
        'Cítricos (frescos o refrigerados)': 'Fruta y verdura',
        'Platanos (frescos o refrigerados)': 'Fruta y verdura',
        'Manzanas (frescas o refrigeradas)': 'Fruta y verdura',
        'Legumbres y hortalizas secas': 'Arroz, legumbres y pasta',
        'Peras (frescas o refrigeradas)': 'Fruta y verdura',
        'Frutas con hueso (frescas o refrigeradas)': 'Fruta y verdura',
        'Bayas (fresas, frambuesas, uvas, etc.) (frescas o refrigeradas)': 'Fruta y verdura',
        'Otras frutas (frescas o refrigeradas)': 'Fruta y verdura',
        'Frutos secos': 'Aperitivos',
        'Frutas preparadas, en conserva y congeladas': 'Fruta y verdura',
        'Hortalizas de hoja o de tallo (frescas o refrigeradas)': 'Fruta y verdura',
        'Hortalizas cultivadas por su fruto (tomates, judías verdes, calabacines, etc.)': 'Fruta y verdura',
        'Hortalizas cultivadas por su fruto (tomates, judías verdes, calabacines, etc.) (frescas o refrigeradas)': 'Fruta y verdura',
        'Bolsas de mezcla de lechugas (frescas o refrigeradas)': 'Fruta y verdura',
        'Coles (frescas o refrigeradas)': 'Fruta y verdura',
        'Patatas': 'Fruta y verdura', 
        'Productos derivados de las patatas, mandioca y otros tubérculos': 'Fruta y verdura',
        'Hortalizas con raíz o bulbo y setas (frescas o refrigeradas)': 'Fruta y verdura',
        'Legumbres y hortalizas secas': 'Fruta y verdura',
        'Legumbres y hortalizas procesadas y otras preparaciones a base de legumbres y hortalizas': 'Fruta y verdura',
        'Legumbres y hortalizas congeladas': 'Fruta y verdura',
        'Aceitunas': 'Aperitivos',
        'Snacks': 'Aperitivos',
        'Azúcar': 'Azúcar, caramelos y chocolate',
        'Confitura, mermelada y miel': 'Azúcar, caramelos y chocolate',
        'Chocolate': 'Azúcar, caramelos y chocolate',
        'Café en cápsulas': 'Cacao, café e infusiones',
        'Agua mineral': 'Agua y refrescos',
        'Helados': 'Congelados',
        'Hortalizas cultivadas por su fruto (tomates, judías verdes, calabacines, etc.) (frescas o refrigeradas)': 'Fruta y verdura',
        'Edulcorantes': 'Azúcar, caramelos y chocolate',
        'Café, no en cápsulas': 'Cacao, café e infusiones',
        'Café en cápsulas': 'Cacao, café e infusiones',
        'Té e infusiones': 'Cacao, café e infusiones',
        'Bebidas refrescantes con o sin gas': 'Agua y refrescos',
        'Bebidas energéticas': 'Agua y refrescos',
        'Bebidas isotónicas': 'Agua y refrescos',
        'Bebidas de cacao y chocolate en polvo': 'Cacao, café e infusiones',
        'Zumos de frutas y/o vegetales': 'Zumos'
        }
    

    df['seccion'] = df['Producto'].map(mapeo_productos)
    return df



def ver_nulos(df):
    df_con_nulos = df[df.isnull().any(axis=1)]
    display(df_con_nulos)
    return df_con_nulos
    
    

