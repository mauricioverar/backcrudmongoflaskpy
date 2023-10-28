""" nombre = "Laxmy"
print("Mi nombre es " + nombre)

lista_super = ["Pan","manzanas", "leche"]
print(lista_super)
print(type(lista_super))

print(type(nombre))
print(lista_super[2])

lista_super.append("bebida")
print(lista_super) """ # ['Pan', 'manzanas', 'leche', 'bebida']

""" mi_texto = "ME GUSTA PYTHON"
print(mi_texto.lower()) """ # me gusta python

# Variable flotante -> float
""" b = 5/2
print(b) # 2.5 """

# Variable entero -> int
# a = 4

# Variable texto -> string
""" c="Hola"
d= "Mundo"

diccionario_datos = {(a,b,c), (1,2,3), "Hola"}

numero_pi = np.pi
print(numero_pi) """

#Importemos algunas de las librerías más clásicas para el manejo de datos en Python

#Pandas es la librería básica para la manipulación y análisis de datos
import pandas as pd # pip install pandas

# pd.melt(df) # convierte columnas en filas
# pd.pivot(df) # filas en columnas
# pd.concat([df1, df2]) # apila 2 dataset q tengan la misma columna y convierte en uno
# pd.concat([df1, df2], axis=1) # 2 q tengan la misma fila y los junta
# df.sort_values("variable") # ordena las filas
# df.rename(columns={"nombre" : "nombre nuevo"}) # renombra
# df.sort_index() # ordena el indice de un DataFrame
# df.reset_index() # redefineelíndicedeunDataFrame
# df.drop(columns=[”var1”,“var2”]) # eliminadelDataFrame
# df[df.columna2<10] # extraelasfilasquecumplenelcriterio
# df.drop_duplicates() # remuevelasfilasduplicadas
# df.sample(frac=0.5) # seleccionalafraccióndedatos(enestecaso50%)
# df.sample(n=10) # seleccionanfilasdemaneraaleatoria
# df.head(n) # muestralasnprimerasfilasdelDataFrame
# df.tail(n) # muestralasnúltimasfilasdelDataFrame
# df[[“columna1”,“columna2”,“columna4”]] # seleccionamúltiplescolumnas
# df[“columna2”] # seleccionaunacolumnaespecífica
# df.filter(regex=”texto”) #seleccionalascolumnasenlascualesestápresenteel“texto"
# df.value_counts() #cuentaelnúmerodefilasconvaloresúnicosenelDataFrame
# df[“columna3”].value_counts() #cuentaelnúmerodefilasconvaloresúnicosdela“columna3”
# len(df) #entregaelnúmerodefilasenelDataFrame
# df.shape #entrega unatupladelnúmerodefilasyelnúmerodecolumnasenelDataFrame
# df[“columna1”].nunique() #númerodevaloresúnicosenlacolumna1
# df.describe() #entregaestadísticosdescriptivosbásicosdecadacolum
# df.groupby(by=”col) #entregaunobjetoagrupadosegúnlacolumna“col”
# df.groupby(level=“index”) # entrega unobjetoagrupadoporlosvaloresdelindexdelDataFrame

#Numpy es la biblioteca para crear vectores y matrices, además de un conjunto grande de funciones matemáticas
import numpy as np # pip install numpy

#Seaborn es una librería que usamos para graficar
import seaborn as sns # pip install seaborn

#Statsmodels es la biblioteca para realizar modelos
import statsmodels.formula.api as smf # pip install statsmodels


# ****************************************************



from flask import Flask, render_template
# los templates ponerlos dentro de una subcarpeta
# ej: templates
app = Flask(__name__)

df_nations = pd.read_csv("https://raw.githubusercontent.com/DireccionAcademicaADL/Nations-DB/main/nations.csv", encoding="ISO-8859-1")

# Routes
@app.route('/')
def index():
  # return '<h1>{% df_nations %}</h1>'
  return render_template("index.html",nombre='Nations', df=df_nations, ej=ej) #, variable='12345')

print(df_nations)

# El método 'head()' nos permite ver "la cabecera (los primeros 5)" del dataset
# print(df_nations.head())
# print(df_nations.tail()) # ultimos 5

# elimar columna
df_nations.drop(columns=["Unnamed: 0"], inplace = True)

# df_nations.columns # ver columnas
# df_nations["region"] # ver esta columna

# df_nations["gdp_pesos2021"] = df_nations["gdp"]*850

#-- 1 ¿que tipos de atributos encontramos en el dataset?

# df_nations.info() # tipos de att contenidos
# print(df_nations.info())
# df_nations.describe() # att numéricos contenidos

# df_nations["gini"].describe() # ver solo 1 att

# También se pueden usar métodos específicos como count(), mean(),  min() o max() para saber el valor específico del estadístico en una variable
# df_nations["gini"].mean() # promedio
# df_nations["gini"].count()

#Para observar un atributo categórico usaremos una tabla de frecuencias

#-- 2 ¿cuantos datos tenemos en cada región?

# df_nations["region"].value_counts()

# Otra forma de hacer este conteo, puede ser a través de una agrupación
# df_nations.groupby(["region"])[["country"]].count()

# Usando where(), crearemos una variable nueva de co2, en dónde identifiquemos qué países están por debajo de la media, y qué países por sobre la media.
# df_nations["co2_recodificada"] = np.where(df_nations["co2"]> df_nations["co2"].mean(), 1, 0)
# df_nations.head()

# Para observar los resultados, podemos hacer una tabla de frecuencias
# df_nations["co2_recodificada"].value_counts()
# CON INDICES DE CO2 MAYORES A LA MEDIA

#-- 3 ¿ cuantos paises tienen indices de co2 mayor al promedio?

# df_nations['co2_recodificada'].value_counts()[1] # 64

# print("Existen " + str(df_nations['co2_recodificada'].value_counts()[1]) + " países con índices de co2 mayores a la media")

# Una variación del método value_counts() es que si pones un caracter dentro del paréntesis, te mostrará los datos en porcentaje:
# df_nations["co2_recodificada"].value_counts("%") # en porcentaje

#-- 4 ¿que se puede decir del alfabetismo en Africa o Europa?

# Filtro por variable "Region"
# df_nations[df_nations["region"]=="Africa"]
df_africa = df_nations[df_nations["region"]=="Africa"]
df_europa = df_nations[df_nations["region"]=="Europe"] # con e


# Para analizar el alfabestimo en áfrica, podemos usar el método mean() en la variable "literacy" para la muestra "África"
# df_africa["literacy"].mean()
# df_europa["literacy"].mean()

#-- gráficos

# Establecer color fondo a todos graficos
# sns.set_style(rc = {'axes.facecolor': 'red'})
sns.set_style(rc = {'axes.facecolor': 'lightsteelblue'})

# Comenzaremos con crear un histograma que nos muestre la distribución del índice gini
graf=sns.displot(df_nations["gini"], kind="hist")

# graf=sns.displot(df_nations["gini"], kind="hist", binwidth = 0.5) # grosor barra

# graf=sns.displot(df_nations["gini"], kind="hist", color='red') # color barras


import matplotlib.pyplot as plt

# sns.displot(df_nations["gini"], kind="hist") # sin red line promedio
plt.axvline(df_nations["gini"].mean(), color = "tomato") # red line




#Graficamos
df_euafr = df_nations.loc[df_nations["region"].isin(["Europe","Africa"])]
sns.barplot(data=df_euafr, x="region", y="chldmort")

# Otro gráfico de barras: Alfabetismo promedio entre Americas y el resto del mundo

# Filtrar los datos para las Americas y el resto del mundo
df_americas = df_nations[df_nations['region'] == 'Americas']
df_resto_mundo = df_nations[df_nations['region'] != 'Americas']

# Calcular el alfabetismo promedio para cada grupo
alfabetismo_promedio_americas = df_americas['literacy'].mean()
alfabetismo_promedio_resto_mundo = df_resto_mundo['literacy'].mean()

# Crear el gráfico de barras utilizando sns.barplot
# sns.<tipo_grafico>(x, y) *******************************************************************************************

# sns.barplot(x=['Americas', 'Rest of the world'], y=[alfabetismo_promedio_americas, alfabetismo_promedio_resto_mundo])

# Ahora usando gráfico Boxplot para observar la distribución de la escolaridad por región

sns.boxplot(x=df_nations["region"], y=df_nations["school"])

#Otra forma de observar la información es a traves de los diagramas de dispersión, pero para usar estos necesitamos eliminar datos perdidos en el dataset.
df_limpia = df_nations.dropna()

df_limpia # datos dispersion

# sns.scatterplot(x=df_limpia["school"], y=df_limpia["literacy"])

# ¿Cómo se podría crear un diagrama de dispersión de la tasa de escolaridad ("school") versus el pib ("gdp")?


# corr = df_nations.corr()

""" <ipython-input-20-3ed480d8f3ae>:1: FutureWarning: The default value of numeric_only in DataFrame.corr is deprecated. In a future version, it will default to False. Select only valid columns or specify the value of numeric_only to silence this warning.
  corr = df_nations.corr() """

""" plt.rcParams["figure.figsize"] =(8,8)
sns.heatmap(corr, cmap="Greens", annot=True) """



# ¿Cual es la relación CO2 y el GDP? ~ (altGR+4)
# modelo de regresion lineal

modelo1 = smf.ols("gdp ~ co2", data=df_limpia)

modelo1 = modelo1.fit()

modelo1.summary() # regresion summary = resumen ***


""" Fórmula: "gdp ~ chldmort + life + school + co2" y data utilizada es "df_limpia". """
# Ajustar el modelo con fit()
# Mostrar resultados

modelo2 = smf.ols("gdp ~ chldmort + life + school + co2", data=df_limpia)

modelo2 = modelo2.fit()

modelo2.summary() # regresion

# ej=modelo2.summary()

# from gpcharts import figure
fig, ax = plt.subplots()
ax.plot(range(5), marker = "o")

# plt.title('Título del gráfico')
plt.title('Título del gráfico', fontdict = {'fontsize': 20, 
                              'fontweight': 'bold', # Estilo
                              'color': 'red'})

ej=plt.show() # muestra grafico

# ej=sns.boxplot(x=df_nations["region"], y=df_nations["school"])


""" sns.displot(
    df_nations["gini"], x="flipper_length_mm", col="species", row="sex",
    binwidth=3, height=3, facet_kws=dict(margin_titles=True),
) """
print(df_nations.info())
# ej=df_nations
# ej=df_nations.head()

# inicializar
if __name__ == "__main__":
    app.run(debug=True)

#   python src/ej.py
