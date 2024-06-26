# -*- coding: utf-8 -*-
"""modelo k-NN.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cR5JyT6J05NboonYChtbP2isO7K-pV8q

# **MODELO k-NN**
"""

import pandas as pd
data=pd.read_csv('/content/diabetes.csv')
data

#Renombrando a las columnas
columnas=['preg','glu','pres','skin','test','mass','pedi','age','class']
data=pd.read_csv('diabetes.csv',names=columnas)
data=data.drop(0)
data

#Tipo de dato y cantidad
print(data.shape)
data.dtypes

# Cambiamos el tipo de datos con astypes()
v_numericas=['preg','glu','pres','skin','test','mass','pedi','age']
data[v_numericas]=data[v_numericas].astype(float)

data.dtypes

# Hallamos estadísticos descriptivos
from pandas import set_option
set_option('display.width',90) #ancho de pantalla
set_option('display.precision',2)#precision de 2 decimales
print(data.describe())

data.isnull().sum()

#Matriz de correlación
correlaciones=data.corr(method='pearson')
print(correlaciones,'\n')
#no hay corelacion muy marcado por ende no se eliminan variables"

#para hallar sesgo
print(data.skew())

# Gráficos de histogramas
import matplotlib.pyplot as plt
data.hist(figsize=(10,10))
plt.show()

import matplotlib.pyplot as plt
data[['preg','glu']].hist(figsize=(15,9))
plt.show()

# Gráficos de densidad
data.plot(kind='density',subplots=True,layout=(3,3),sharex=False,figsize=(10,10))
plt.show()

# Gráficos de cajas. Visualizar atípicos
data.plot(kind='box',subplots=True,layout=(3,3),sharex=False,figsize=(10,10))
plt.show()

# Gráficos de dispersión
from pandas.plotting import scatter_matrix #matriz de dispersion
scatter_matrix(data,figsize=(10,10),color='red',diagonal='kde',marker='+') #kde es gráfico de densidad
plt.show()

import numpy as np
import csv
with open('diabetes.csv','r',) as file:  #'r'es lectura
    reader=csv.reader(file,delimiter=',')
    cabecera=next(reader)
    data1=list(reader)
    data1=np.array(data1).astype(float)
print(data1.shape)
print(cabecera)
data1

# Mapa de calor
fig=plt.figure(figsize=(10,10))
ax=fig.add_subplot(111)
cax=ax.matshow(correlaciones,vmin=-1,vmax=1)
fig.colorbar(cax)
ticks=np.arange(0,8,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(v_numericas) # dentro de los ejes colocamos los nombres
ax.set_yticklabels(v_numericas)
plt.show()

import seaborn as sns
f,ax=plt.subplots(figsize=(10,10))
sns.heatmap(correlaciones,cmap='coolwarm',vmin=-1,vmax=1,
           linewidths=.5,square=True,annot=True)
plt.show()

# Cantidad de datos por categoría
print(data['class'].value_counts())
sns.countplot(x='class',data=data,palette='hls')
plt.show()

# Separando los datos de entrenamiento 80% y prueba 20%
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test =train_test_split(
data[v_numericas],data['class'],test_size=0.2,random_state=0)
X_train, y_train

# Modelo k-NN
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=2)
knn.fit(X_train,y_train)

# Hacemos predicciones
y_pred=knn.predict(X_test)
print('Valores predichos de prueba:\n {}'.format(y_pred))

#Medimos la precisión de nuestro modelo de entrenamiento y para la prueba
print('Precisión para los datos de entrenamiento:{:.2f}'.format(knn.score(X_train, y_train)))
print('Precisión para los datos de prueba:{:.2f}'.format(knn.score(X_test, y_test)))

print('Precisión para los datos de prueba:'
     ,knn.score(X_test, y_test)*100,"%")