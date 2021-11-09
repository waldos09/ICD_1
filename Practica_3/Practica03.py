# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 16:16:28 2021

@author: waldo
"""
import pandas as pd
import matplotlib.pyplot as plot
import sklearn.cluster as skl

#datos del csv
dataset = pd.read_csv('data1.csv')

x = dataset['Cientifico de Datos']
y = dataset['Experiencia']


#Inicializacion del cluster
cluster = skl.KMeans(n_clusters=5)

#entrena el algoritmo con los datos
cluster.fit(dataset)

#obtencion de los centroides
cnt = cluster.cluster_centers_

#obtiene una lista con etiquetas de los datos
etiquetas = cluster.predict(dataset)

#agrega al frame de datos una nueva columna para las etiquetas
dataset['etiquetas'] = etiquetas


#tabla de colores
colores = ['red','orange','green','pink','blue']

colores_datos=[]
colores_cnt = []

for row in etiquetas:
    colores_datos.append(colores[row])
    
for i in range(len(cnt)):
    colores_cnt.append(colores[i])    

#Grafica de dispersión

plot.scatter(x, y, c=colores_datos, marker='o', s=40)
plot.scatter(cnt[:,0], cnt[:,1], c=colores_cnt, marker='*', s=200)
plot.xlabel('Salario')
plot.ylabel('Experiencia')
plot.title('K-Means Clustering Salarios vs Experiencia (Pedagogos)')
plot.grid(color='gray', linestyle='--', linewidth = 0.5)
plot.show()