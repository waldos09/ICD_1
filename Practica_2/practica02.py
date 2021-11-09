# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import matplotlib.pyplot as plot
import statistics as st
import seaborn as sns
import numpy as np
import os
from tkinter import *
import pandas as pd


dataset = pd.read_csv('data1.csv')
cd = dataset['Cientifico de Datos']
cd1 = dataset.sort_values('Cientifico de Datos')
"""
print(dataset)
print('<<<<>>>>')
print(dataset.keys())
print(cd)
print('<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>')
print(cd1)
"""
#data = []

#file = open('data1.csv', 'r')

##for line in file:
##    data.append(int(line))

##file.close()

##sorted(data)

q1,q3 = np.percentile(cd,[25 , 75])

iqr = q3 - q1

os.system('cls')
print('Analisis de salarios de Cientificos de Datos')
print("<<Datos de entrada>>")
print(cd)
print('\n <<Resultados>>')

#medidas de centralidad
print('Media = ',cd.mean())
print('Mediana = ',cd.median())
#print('Media = ',st.mean(cd1))
#print('Mediana = ', st.median(cd1))

#Mediddas  de Dispersion
print('Desviacion Estandar = ',cd.std())
#print('Desviacion Estandar = ', st.stdev(data))
print('Q1 y Q3 = ',q1, q3)
print('Distancia intercuartil = ',iqr )
print('\n')


#Grafica de caja y vigote 
sns.boxplot(cd);
plot.xlabel('Salarios')
sns.swarmplot(cd, color='r')

# Histograma y curva de densidad
sns.displot(cd, kde='true', rug='true')
plot.xlabel('Salarios')
plot.ylabel('Frecuencia')
plot.axvline(cd.mean(), color='red', linestyle='--')
plot.axvline(cd.median(), color='green', linestyle='--')
#plot.axvline(st.mean(data), color='red', linestyle='--')
#plot.axvline(st.median(data), color='green', linestyle='--')
plot.show


##################################################


igs = dataset['Ing Sistemas']
igs1 = dataset.sort_values('Ing Sistemas')
"""
print(dataset)
print('<<<<>>>>')
print(dataset.keys())
print(cd)
print('<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>')
print(cd1)
"""
#data = []

#file = open('data1.csv', 'r')

##for line in file:
##    data.append(int(line))

##file.close()

##sorted(data)

q1,q3 = np.percentile(igs,[25 , 75])

iqr = q3 - q1

os.system('cls')
print('Analisis de salarios de Ing de Sistemas')
print("<<Datos de entrada>>")
print(igs)
print('\n <<Resultados>>')

#medidas de centralidad
print('Media = ',igs.mean())
print('Mediana = ',igs.median())
#print('Media = ',st.mean(cd1))
#print('Mediana = ', st.median(cd1))

#Mediddas  de Dispersion
print('Desviacion Estandar = ',igs.std())
#print('Desviacion Estandar = ', st.stdev(data))
print('Q1 y Q3 = ',q1, q3)
print('Distancia intercuartil = ',iqr )
print('\n')


#Grafica de caja y vigote 
sns.displot(cd, kde='true', rug='true')
sns.boxplot(igs);
plot.xlabel('Salarios')
sns.swarmplot(igs, color='r')

# Histograma y curva de densidad
sns.displot(igs, kde='true', rug='true')
plot.xlabel('Salarios')
plot.ylabel('Frecuencia')
plot.axvline(igs.mean(), color='red', linestyle='--')
plot.axvline(igs.median(), color='green', linestyle='--')
#plot.axvline(st.mean(data), color='red', linestyle='--')
#plot.axvline(st.median(data), color='green', linestyle='--')
plot.show

