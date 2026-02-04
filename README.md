## Proyecto 3
Proyecto de la semana 4 bootcamp Data

## TÍTULO 
Análisis del precio de consumo de la canasta básica en Madrid

## Objetivo del proyecto
Aumentar la calidad de vida de los residentes de Madrid al disminuir los gastos de consumo de la canasta básica.


## Contexto del negocio
Este proyecto se plantea como una idea de negocio que busca mejorar la calidad de vida de los residentes de Madrid al disminuir los gastos de consumo de la canasta básica.
Implementar una plataforma B2B de inteligencia de mercado que ofrece a pequeños comercios y cadenas de restauración en Madrid un índice de competitividad en tiempo real frente al líder del mercado (Mercadona) y la inflación oficial (IPC).


----


## Dataset
Los datasets utilizados recogen registros de precios de productos en Mercadona y el IPC de Madrid. Estos datos han sido obtenidos de la web de Mercadona, el INE, información de ISTAC y la web de la comunidad de Madrid mediante la encuesta de gastos de consumo.
Contiene información sobre:

- Precios de productos en Mercadona
- IPC de Madrid
- Datos de gastos de consumo de la encuesta de la comunidad de Madrid
- Productos de la canasta básica

Las variables principales utilizadas en el análisis son:  
"precio", "Grupo ECOICOP", "Anyo","Producto"


## Notas sobre la calidad del dato
El dataset presenta problemas de datos faltantes que han requerido procesos de limpieza y agregar columnas:

- Valores nulos en algunas filas y columnas.
- Datos duplicados.
- Datos faltantes, ya que no todos los estudios tienen la misma duración.
- Demasiados datos y columnas que no necesitamos estudiar para nuestras hipótesis.
- Separación de la información para obtener diferentes columnas.
- Problemas en los tipos de datos y los formatos de las variables como paso con la variable Año tuvo que cambiarse a Anyo.

Se han tomado decisiones de limpieza y estandarización para garantizar la coherencia del análisis y la cantidad de datos de estudio por lo que nos hemos centrado en Madrid para el estudio de precios de la canasta básica.


---


## Preguntas clave / Hipótesis
1. 

 Aceleración inflacionaria post-2021: Se observa un salto significativo en los valores a partir de 2022. En "Alimentos", el valor pasa de ~27 a ~36-37. La hipótesis es que factores externos (crisis de suministros o energía) impactaron con mayor fuerza a partir de ese año.
Alimentos como motor del índice: El grupo 01 (Alimentos) muestra un crecimiento acumulado mucho mayor que el Índice General y que el grupo 05 (Muebles). Se puede plantear que la inflación en Canarias (ISTAC) está siendo impulsada principalmente por la cesta de la compra básica.. 
2. En los meses de junio y agosto, la asistencia de las niñas es menor que la de los niños. 


## Proceso de análisis
El análisis incluye:
- Exploración inicial del dataset (EDA).
- Limpieza y estandarización de variables.
- Creación de nuevas variables/columnas (Seccion para los productos).
- Análisis descriptivo y comparativo mediante tablas y gráficos.


## Resultados / Insights
- .


---


## Recomendaciones de negocio
- Implementar esta .


## Limitaciones
- .


## Próximos pasos
- 


---


## Cómo replicar el proyecto
1. Clonar el repositorio.
2. Instalar las librerías necesarias (`pandas`, `Funciones`, `numpy`, `matplotlib`, `seaborn`).
3. Ejecutar el notebook a través de github.

