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
dn=pd.read_excel (r'C:\Users\MOI\Desktop\cours EIVP\cours S1\Algorithmique Programmation\projet info\EIVP_donnée_.xlsx') ## on ouvre le ficher excel contenant toutes les données
x=dn.values ## chaque colonne du tableau est transformée en une liste. x est une liste de listes

#### Afficher des courbes montrant l’évolution d’une variable en fonction du temps.
## Etape 1: convertir les colonnes en liste et les séparer

id=[] ## on cherche à avoir une liste pour chaque colonne
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
time1=[] ## Les données sont relevées par plusieurs capteurs. Donc on sépare chaque liste en 6 listes chacunes correspondant à un identifiant (on réalise ce programme pour toutes les données)
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
temp2=[
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
lum1=[]
lum2=[]
lum3=[]
lum4=[]
lum5=[]
lum6=[]
for i in range(len(time)):
    if id[i]==1:
        lum1.append(lum[i])
    elif id[i]==2:
        lum2.append(lum[i])
    elif id[i]==3:
        lum3.append(lum[i])
    elif id[i]==4:
        lum4.append(lum[i])
    elif id[i]==5:
        lum5.append(lum[i])
    else:
        lum6.append(lum[i])
  
##
time1str=[] ## afin de pouvoir traiter le format dates et l'afficher sur les courbes on a transformé en format str.
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
def tracer_graph(l,L): ## Pour le trcé de toutes les courbes il faut que les listes soient relatives aux mêmes identifiants et que utiliser les liste temps en format str
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(l,L)
    plt.xlabel("temps")
    plt.ylabel("co2")
    plt.xticks(rotation=90)
    plt.title("Evolution d'une variabe en fonction du temps selon l'identifiant du capteur")
    plt.show()
##
print(tracer_graph(time4str,co2_4)) ## test
    
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
print(tracer_graph_max(time4str,noise4)) ## test
    
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

               
    plt.show()

##
print(tracer_graph_min(time5str,humidity5)) ## test

##
def tracer_graph_moyenne(l,L): ## Cette moyenne concerne toutes les données à part la donnée acoustique, pour laquelle il ne serait pas logique de faire une moyenne qui n'est pas logarithmique.
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
    ax.text(min(l),max(L),np.mean(L),bbox=dict(boxstyle = "square",facecolor = "yellow"))
    plt.show()
##
print(tracer_graph_moyenne(time2str,temp2)) ## test

##

def tracer_graph_moyenne_acoustique(l,L): ## Cette moyenne concerne la donnée acoustique on applique la formule de la moyenne énérgetique
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(l,L)
    plt.xlabel("temps")
    plt.ylabel("variable")
    plt.xticks(rotation=90)
    plt.title("Evolution du bruit en fonction du temps et les données statistiques selon l'identifiant du capteur")

    liste1=[]
    for i in range (len(L)):
        int=L[i]/10
        liste1.append(10**int)

    acoustqique_mean=[10*(m.log10(np.mean(liste1)))]*len(l)
                
    ax.text(min(l),max(L),np.mean(L),bbox=dict(boxstyle = "square",facecolor = "yellow"))
    plt.show()
##
print(tracer_graph_moyenne_acoustique(time2str,lum2))

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
print(tracer_graph_variance(time6str,noise6)) ## test

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
print(tracer_graph_ecarttype(time6str,noise6)) ## test

##
def calcul_median(liste): ## on distibgue la cas où la liste a une longueur paire et le cas où la longueur est impaire
    n=len(liste)
    if n%2==1:
        return liste[int(n/2)]
    else:
        return ((liste[(n//2)-1]+liste[n//2])/2)
##
print(calcul_median(humidity2)) ## test


## Calculer la température de rosée et en déduire l'humidex
##id1
    a=17.27 ## on utilise la formule de l'humidex disponible sur internet, sauf que pour calculer l'humidex il faut calculer d'abord la temperature de rosée. On reproduit la même fopnction 6 fois (pour chaque capteur).
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
print(tracer_humidex(temp6,humidex6)) ## test

## Calculer l’indice de corrélation entre un couple de variables
def calculer_correlation(liste1,liste2):
    cov=np.cov(liste1, liste2, ddof=0)[0][1]
    cor=cov/(sqrt((np.var(liste1))*(np.var(liste2))))
    return cor
##
print(calculer_correlation(temp1,noise1)) ## test
                
##
def tracer_graph_anomalie(l,L,p):
    anomalies_L=[]
    anomalies_l=[]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.plot(l,L)
    plt.xlabel("temps")
    plt.ylabel(L)
    plt.xticks(rotation=90)
    plt.title("Evolution d'une variabe en fonction du temps selon l'identifiant du capteur")

    for i in range (1,len(l)-1):
        min=((L[i-1]+L[i+1])/2)-((L[i-1]+L[i+1])/2)*(p/100)
        max=((L[i-1]+L[i+1])/2)+((L[i-1]+L[i+1])/2)*(p/100)
        if min>L[i] or max<L[i]:
            anomalies_L.append(L[i])
            anomalies_l.append(l[i])

    for i in range (0,len(anomalies_l)):
        plt.scatter(x=anomalies_l[i], y=anomalies_L[i], color='red')


    plt.show()

##
def horaires():
    ouverture=[]#on crée une liste des horaires des ouvertures et des fermetures que chaque méthodes nous renvoit
    fermeture=[]
    for i in range(len(time1)):
        if noise1[i-1]<28 and noise1[i+1]>28:#on repere que le bruit se stabilise à 27 la nuit, on utilise la meme logique pour les autres paramètres
            ouverture.append(time1[i])
        if lum1[i-1]<5 and lum[i+1]>5:
            ouverture.append(time1[i])
        if co2_1[i-1]<425 and co2_1[i+1]>425:
            ouverture.append(time1[i])
        if noise1[i-1]>28 and noise1[i+1]<28:
            fermeture.append(time1[i])
        if lum1[i-1]>5 and lum[i+1]<5:
            fermeture.append(time1[i])
        if co2_1[i-1]>425 and co2_1[i+1]<425:
            fermeture.append(time1[i])
    return "les horaires d'ouverture estimés sont", np.median(np.array(ouverture)), np.median(np.array(fermeture))#on retourne la médiane des valeurs deja obtenues

