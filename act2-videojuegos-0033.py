# Keyla Paola NC = 0033 | Fecha 9/nov/2026
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#crearemos nuestra tabla y la guardaremos con pandas
# Tenemos 5 listas de Video Juegos con 4 elementos por lista 
# Problema 3: Juegos (Nombre, copias vendidas en millones, es multijugador, año lanzamiento)
mc  = ['Minecraft', 300, True, 2011]
gta = ['GTA V', 190, True, 2013]
tet = ['Tetris', 100, False, 1984]
wii = ['Wii Sports', 82.9, True, 2006]
pub = ['PUBG', 75, True, 2017]
cyc = ["Candy Crush", 10, False, 2012]
# Creamos una lista de listas (conformando la tabla)
lista_video_juegos = [mc,gta,tet,wii,pub,cyc]
# print(lista_video_juegos)
# Utilizar Pandas para organizar la tabla (dataframe o marco de datos)
# a cada columna le agregan nombre 
df_video_juegos = pd.DataFrame(lista_video_juegos,columns=["Nombre","Jugadores (mil)","Es_Online","Año"])
#Creamos el archivo CSV y lo guardamos en CS
df_video_juegos.to_csv("videojuegos.csv", index=False)
print(df_video_juegos)
#Crear grafica de lineas
# donde X es nombre en el eje horizontal 
# donde Y es Jugadores (mil) en el eje vertical
plt.plot(df_video_juegos["Nombre"], df_video_juegos["Jugadores (mil)"])
plt.title ("Grafica Video Juegos 0033")
plt.xlabel ("Nombre de los juegos")
plt.ylabel ("Jugadores (mil) de usuarios")
# Mostrar Grafica
plt.show()

#Creamos una Grafica de Puntos 
plt.scatter(df_video_juegos["Nombre"],df_video_juegos["Jugadores (mil)"])
plt.title ("Grafica Video Juegos 0033")
plt.xlabel ("Nombre de los juegos")
plt.ylabel ("Jugadores (mil) de usuarios")
# Mostrar grafica
plt.show()

# Creamos una Grafica de barras 
plt.bar(df_video_juegos["Nombre"],df_video_juegos["Jugadores (mil)"])
plt.title ("Grafica Video Juegos 0033")
plt.xlabel ("Nombre de los Juegos")
plt.ylabel ("Jugadores (mil) de usuarios")
# Mostrar grafica
plt.show()
# Ordenar la grafica de barras de manera horizontal
# de la mas grande la mas pequeña
df_rs_ordenar = df_video_juegos.sort_values("Jugadores (mil)",ascending = False)
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Jugadores (mil)"])
plt.title ("Grafica Video Juegos 0033")
plt.xlabel ("Nombre de los juegos")
plt.ylabel ("Jugadores (mil) de usuarios")
plt.show()

# Grafica con color 
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Jugadores (mil)"],
        color = [ "b", "g", "c", "m", "y", "r"])
plt.title ("Grafica Video Juegos 0033")
plt.xlabel ("Nombre de los juegos")
plt.ylabel ("Jugadores (mil) de usuarios")
plt.show()
print(" ")
# Grafica de pastel
plt.pie(df_video_juegos["Jugadores (mil)"],
        labels=df_video_juegos["Nombre"])
plt.title("grafica de pastel Video Juegos  NC = 0033")
plt.show()
print("Keyla Paola NC = 0033 | Fecha 9/nov/2026")