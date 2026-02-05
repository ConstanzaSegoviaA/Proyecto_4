## Proyecto 3
Proyecto de la semana 4 bootcamp Data

## TÍTULO 
Análisis del precio de consumo de la canasta básica en Madrid

## Objetivo del proyecto
Aumentar la calidad de vida de los residentes de Madrid al disminuir los gastos de consumo de la canasta básica.


## Contexto del negocio
Este proyecto se plantea como una idea de negocio que busca mejorar la calidad de vida de los residentes de Madrid al disminuir los gastos de consumo de la canasta básica. Esta idea nace debido al aumento significativo y constante de los alimentos.
Implementar una plataforma de mercado que ofrece a pequeños comercios y cadenas de restauración en Madrid un índice de competitividad en tiempo real y al cliente identificar donde se encuentran los precios más bajos.



----


## Dataset
Los datasets utilizados recogen registros de precios de productos en Mercadona y el IPC de Madrid. Estos datos han sido obtenidos de la web de Mercadona, el INE, información de ISTAC y la web de la comunidad de Madrid mediante la encuesta de gastos de consumo.
Contiene información sobre:

- Precios de productos en Mercadona
- IPC de Madrid
- Datos de gastos de consumo de la encuesta de la comunidad de Madrid
- Productos de la canasta básica

Las variables principales utilizadas en el análisis son:  
"precio", "Grupo ECOICOP", "Anyo","Producto", "seccion"


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
1. El aumento de los alimentos en los diferentes comercios es debido al aumento del IPC, haciendo a los Madrileños gastar gan parte de su salario en la canasta básica de alimentos. ¿Es a nivel general el aumento del IPC o solamente en los alimentos?¿Que ocurre con el IPC con otros grupos del hogar?

2. Al observar los precios de la canasta básica en Madrid, notamos productos más elevados que otros. ¿Si analizamos un supermercado como Mercadona, los precios estarán en base al promedio general de Madrid? 


## Proceso de análisis
El análisis incluye:
- Exploración inicial del dataset (EDA).
- Limpieza y estandarización de variables.
- Datos de la canasta básica.
- Creación de nuevas variables/columnas (Seccion para los productos).
- Análisis descriptivo y comparativo mediante tablas y gráficos.


## Resultados / Insights
- Hay una subida generalizada de precios en la mayoría de los productos alimenticios, lo que genera frustración en el consumidor. No asi en otros productos como son los muebles o electrodomésticos.A lo largo de los años podemos ver que donde más se siente el aumento del IPC es en los alimentos básicos de un hogar. Creando un problema de calidad de vida para los residentes de Madrid, pues deben dedicar más horas al trabajo para poder cubrir los gastos de la canasta básica. 
-La comparación Mercadona versus el promedio de los años anteriores nos hace entender que hay diferentes cadenas que tal vez son las más baratas. Con todo esto vemos que tiempo para poder comparar precios en diferentes supermercados no nos alcanza por lo que la plataforma podría identificar si Mercadona es consistentemente la opción más económica en Madrid para la canasta básica o si existen alternativas más baratas, optimizando el tiempo de los Madrileños y mejorando la calidad de vida.


---


## Recomendaciones de negocio
- Con el estudio realizado podemos ver que donde más afecta el aumento de IPC es en los productos de consumo diario como son los alimentos de la canasta básica. El poder implementar esta plataforma hará que los Madrileños puedan tener un mejor control de sus gastos de consumo y mejorar su calidad de vida, optimizando el tiempo que destinan a comprar obteniendo los mejores precios y ahorrando algunos euros para emplear en lo que estimen conveniente.


## Limitaciones
- Información un poco acotada de los datos, ya que INE entrega los datos generalizados por grupos ECOICOP lo que hace un poco dificil desglozarlo en la canasta básica de alimentos.
- Los precios en los supermercados cambian diariamente o semanalmente debido a ofertas, cambios de stock y estrategias de la competencia, por tanto, recopilar y mantener esta información actualizada manualmente o mediante métodos no automatizados es una limitación importante.
-Las encuestas de gastos de consumo son de años anteriores, que pueden no ser completamente representativos de la realidad de todos los distritos de Madrid.
- Definición subjetiva de "Canasta Básica", no existe una definición única y universal de esta haciendo la selección de los productos algo subjetiva y puede no reflejar las pautas de consumo exactas de toda la población de Madrid.



## Próximos pasos
- Tal vez la información de precios de supermercados se debería ampliar a más cadenas de supermercados haciendo este estudio más robusto y poder comparar precios de diferentes cadenas en la plataforma.
- Validación y Normalización de la Canasta Básica, es decir, definir un listado estándar y fijo de entre 30 y 50 productos esenciales que conformen la "canasta básica" del estudio. Además validar este listado mediante encuestas a consumidores reales en Madrid para asegurar su relevancia.
- Tal vez Realizar un estudio de mercado más profundo para determinar la inversión inicial necesaria para desarrollar la plataforma tecnológica (app/web) y calcular el potencial retorno de la inversión.
- Partir con un producto mínimo viable de desarrollar y lanzar una versión básica de la plataforma que cubra solo 3-5 códigos postales de Madrid y compare 20 productos en 2 supermercados, para probar la aceptación del mercado y la usabilidad antes de una expansión completa.



---


## Cómo replicar el proyecto
1. Clonar el repositorio.
2. Instalar las librerías necesarias (`pandas`, `Funciones`, `numpy`, `matplotlib`, `seaborn`).
3. Ejecutar el notebook a través de github.

