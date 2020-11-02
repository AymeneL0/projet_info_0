## Projet informatique

## importation
import numpy as np
from numpy import arange
import pandas as pd
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
from datetime import datetime
import math as m
from math import *
## Importation et lecture de fichier csv
dn=pd.read_excel (r'C:\Users\MOI\Desktop\cours EIVP\cours S1\Algorithmique Programmation\projet info\EIVP_donnée_.xlsx')
print(dn)
x=dn.values
#### Afficher des courbes montrant l’évolution d’une variable en fonction du temps.

## Etape 1: convertir les colonnes en liste et les séparer
id=[]
noise=[]
temp=[]
humidity=[]
lum=[]
co2=[]
time=[]
for i in range(len(x)):
    id.append(x[i][0])
    noise.append(x[i][1])
    temp.append(x[i][2])
    humidity.append(x[i][3])
    lum.append(x[i][4])
    co2.append(x[i][5])
    time.append(x[i][6])

## Etape 2: séparer les listes de données en focntion de l'id
time1=[]
time2=[]
time3=[]
time4=[]
time5=[]
time6=[]
for i in range(len(time)):
    if id[i]==1:
        time1.append(time[i])
    elif id[i]==2:
        time2.append(time[i])
    elif id[i]==3:
        time3.append(time[i])
    elif id[i]==4:
        time4.append(time[i])
    elif id[i]==5:
        time5.append(time[i])
    else:
        time6.append(time[i])

##
noise1=[]
noise2=[]
noise3=[]
noise4=[]
noise5=[]
noise6=[]
for i in range(len(time)):
    if id[i]==1:
        noise1.append(noise[i])
    elif id[i]==2:
        noise2.append(noise[i])
    elif id[i]==3:
        noise3.append(noise[i])
    elif id[i]==4:
        noise4.append(noise[i])
    elif id[i]==5:
        noise5.append(noise[i])
    else:
        noise6.append(noise[i])

##
temp1=[]
temp2=[]
temp3=[]
temp4=[]
temp5=[]
temp6=[]
for i in range(len(time)):
    if id[i]==1:
        temp1.append(temp[i])
    elif id[i]==2:
        temp2.append(temp[i])
    elif id[i]==3:
        temp3.append(temp[i])
    elif id[i]==4:
        temp4.append(temp[i])
    elif id[i]==5:
        temp5.append(temp[i])
    else:
        temp6.append(temp[i])

##
humidity1=[]
humidity2=[]
humidity3=[]
humidity4=[]
humidity5=[]
humidity6=[]
for i in range(len(time)):
    if id[i]==1:
        humidity1.append(humidity[i])
    elif id[i]==2:
        humidity2.append(humidity[i])
    elif id[i]==3:
        humidity3.append(humidity[i])
    elif id[i]==4:
        humidity4.append(humidity[i])
    elif id[i]==5:
        humidity5.append(humidity[i])
    else:
        humidity6.append(humidity[i])

##
co2_1=[]
co2_2=[]
co2_3=[]
co2_4=[]
co2_5=[]
co2_6=[]
for i in range(len(time)):
    if id[i]==1:
        co2_1.append(co2[i])
    elif id[i]==2:
        co2_2.append(co2[i])
    elif id[i]==3:
        co2_3.append(co2[i])
    elif id[i]==4:
        co2_4.append(co2[i])
    elif id[i]==5:
        co2_5.append(co2[i])
    else:
        co2_6.append(co2[i])


##
time1str=[]
for i in range(len(time1)):
    time1str.append(datetime.strptime(time1[i],'%Y-%m-%d %H:%M:%S %z'))
##
time2str=[]
for i in range(len(time2)):
    time2str.append(datetime.strptime(time2[i],'%Y-%m-%d %H:%M:%S %z'))
##
time3str=[]
for i in range(len(time3)):
    time3str.append(datetime.strptime(time3[i],'%Y-%m-%d %H:%M:%S %z'))
##
time4str=[]
for i in range(len(time4)):
    time4str.append(datetime.strptime(time4[i],'%Y-%m-%d %H:%M:%S %z'))
##
time5str=[]
for i in range(len(time5)):
    time5str.append(datetime.strptime(time5[i],'%Y-%m-%d %H:%M:%S %z'))
##
time6str=[]
for i in range(len(time6)):
    time6str.append(datetime.strptime(time6[i],'%Y-%m-%d %H:%M:%S %z'))
## tracer les grahiques
##
def tracer_graph(l,L):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(l,L)
    plt.xlabel("temps")
    plt.ylabel("co2")
    plt.xticks(rotation=90)
    plt.title("Evolution d'une variabe en fonction du temps selon l'identifiant du capteur")
    plt.show()
##
print(tracer_graph(time4str,co2_4))
## Tracer graphique en affichant des valeurs statistiques
def tracer_graph_max(l,L):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(l,L)
    plt.xlabel("temps")
    plt.ylabel("variable")
    plt.xticks(rotation=90)
    plt.title("Evolution dune variable en fonction du temps et les données statistiques selon l'identifiant du capteur")

    ymax = max(L)
    xpos = L.index(ymax)
    xmax = l[xpos]

    ax.annotate('max', xy=(xmax, ymax), xytext=(xmax, ymax+1),
               arrowprops=dict(facecolor='green', shrink=0.01),
               )

    plt.show()
##
print(tracer_graph_max(time4str,noise4))
##
def tracer_graph_min(l,L):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(l,L)
    plt.xlabel("temps")
    plt.ylabel("variable")
    plt.xticks(rotation=90)
    plt.title("Evolution dune variable en fonction du temps et les données statistiques selon l'identifiant du capteur")

    ymin = min(L)
    xpos = L.index(ymin)
    xmin = l[xpos]

    ax.annotate('min', xy=(xmin, ymin), xytext=(xmin, ymin+1),
               arrowprops=dict(facecolor='red', shrink=0.01),
               )

    plt.show()
##
print(tracer_graph_min(time5str,humidity5))
##
def tracer_graph_moyenne(l,L):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(l,L)
    plt.xlabel("temps")
    plt.ylabel("variable")
    plt.xticks(rotation=90)
    plt.title("Evolution dune variable en fonction du temps et les données statistiques selon l'identifiant du capteur")

    y_mean = [np.mean(L)]*len(l)
    mean_line = ax.plot(l,y_mean, label='MOYENNE', linestyle='--')
    legend = ax.legend(loc='upper right')
    plt.show()
##
print(tracer_graph_moyenne(time2str,temp2))
##
def tracer_graph_variance(l,L):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(l,L)
    plt.xlabel("temps")
    plt.ylabel("variable")
    plt.xticks(rotation=90)
    plt.title("Evolution dune variable en fonction du temps et les données statistiques selon l'identifiant du capteur")

    variance=np.var(L)
    ax.text(min(l),max(L), variance,bbox=dict(boxstyle = "square",facecolor = "yellow"))
    plt.show()
##
print(tracer_graph_variance(time6str,noise6))
##
def tracer_graph_ecarttype(l,L):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(l,L)
    plt.xlabel("temps")
    plt.ylabel("variable")
    plt.xticks(rotation=90)
    plt.title("Evolution dune variable en fonction du temps et les données statistiques selon l'identifiant du capteur")

    variance=np.var(L)
    ecarttype=sqrt(variance)
    ax.text(min(l),max(L), ecarttype,bbox=dict(boxstyle = "square",facecolor = "yellow"))
    plt.show()
##
print(tracer_graph_ecarttype(time6str,noise6))
##
def calcul_median(liste):
    if len(liste)%2!=0:
        med1=(len(liste)-1)/2
        return liste[med1]
    elif len(liste)%2==0:
        med2=len(liste)/2
        med3=(len(iste)/2)-1
        return np.mean(liste[med2],liste[med3])

def tracer_graph_medianne(l,L):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(l,L)
    plt.xlabel('temps')
    plt.ylabel('variable')
    plt.xticks(rotation=90)
    plt.title("Evolution dune variable en fonction du temps et les données statistiques selon l'identifiant du capteur")

    median_line = ax.plot(l[calcul_median(L)], label='MEDIANE', linestyle='--')
    legend = ax.legend(loc='upper right')

    plt.show()
##
print(tracer_graph_medianne(time5str,noise5))

## Calculer la température de rosée et en déduire l'humidex
##id1
    a=17.27
    b=237.7
    t_ros1=[]
    for X in temp1:
        for Y in humidity1:
            c1=(((a*X)/(b+X))+m.log(Y))
        t_ros1.append((b*c1)/(a-c1))
##
    humidex1=[]
    for X in temp1:
        for Y in t_ros1:
            c2=(0.555*(6.11*m.exp((1/273.16)-(1/Y))-10))
        humidex1.append(X+c2)

##id2
    t_ros2=[]
    for X in temp2:
        for Y in humidity2:
            c1=(((a*X)/(b+X))+m.log(Y))
        t_ros2.append((b*c1)/(a-c1))
##
    humidex2=[]
    for X in temp2:
        for Y in t_ros2:
            c2=(0.555*(6.11*m.exp((1/273.16)-(1/Y))-10))
        humidex2.append(X+c2)
##id3
    t_ros3=[]
    for X in temp3:
        for Y in humidity3:
            c1=(((a*X)/(b+X))+m.log(Y))
        t_ros3.append((b*c1)/(a-c1))
##
    humidex3=[]
    for X in temp3:
        for Y in t_ros3:
            c2=(0.555*(6.11*m.exp((1/273.16)-(1/Y))-10))
        humidex3.append(X+c2)
##id4
    t_ros4=[]
    for X in temp4:
        for Y in humidity4:
            c1=(((a*X)/(b+X))+m.log(Y))
        t_ros4.append((b*c1)/(a-c1))
##
    humidex4=[]
    for X in temp4:
        for Y in t_ros4:
            c2=(0.555*(6.11*m.exp((1/273.16)-(1/Y))-10))
        humidex4.append(X+c2)
##id5
    t_ros5=[]
    for X in temp5:
        for Y in humidity5:
            c1=(((a*X)/(b+X))+m.log(Y))
        t_ros5.append((b*c1)/(a-c1))
##
    humidex5=[]
    for X in temp5:
        for Y in t_ros5:
            c2=(0.555*(6.11*m.exp((1/273.16)-(1/Y))-10))
        humidex5.append(X+c2)
##id6
    t_ros6=[]
    for X in temp6:
        for Y in humidity6:
            c1=(((a*X)/(b+X))+m.log(Y))
        t_ros6.append((b*c1)/(a-c1))
##
    humidex6=[]
    for X in temp6:
        for Y in t_ros6:
            c2=(0.555*(6.11*m.exp((1/273.16)-(1/Y))-10))
        humidex6.append(X+c2)
##
def tracer_humidex(l,L):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(l,L)
    plt.xlabel("température")
    plt.ylabel("humidex")
    plt.xticks(rotation=90)
    plt.title("Evolution de l'humidex en fonction de la température selon l'identifiant' ")
    plt.show()
##
print(tracer_humidex(temp6,humidex6))
## Calculer l’indice de corrélation entre un couple de variables
def calculer_correlation(liste1,liste2):
    cov=np.cov(liste1, liste2, ddof=0)[0][1]
    cor=cov/(sqrt((np.var(liste1))*(np.var(liste2))))
    return cor
##
print(calculer_correlation(temp1,noise1))

##on décompose les dates
date=[]
heure=[]
n=len(time)
for i in range(n):
    date.append(time[i][:10])
    heure.append(time[11:19])