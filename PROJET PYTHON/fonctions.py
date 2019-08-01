
from tkinter import *
import tkinter as tk
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from tkinter.messagebox import *



"""  
    Text1 = tk.Text(fenetrePari)
    Text1.place(relx=0.086, rely=0.044, relheight=0.809, relwidth=0.755)
    




    Text1.configure(background="white")
    Text1.configure(font="TkTextFont")
    Text1.configure(foreground="black")
    Text1.configure(highlightbackground="#d9d9d9")
    Text1.configure(highlightcolor="black")
    Text1.configure(insertbackground="black")
    Text1.configure(selectbackground="#c4c4c4")
    Text1.configure(selectforeground="black")
    Text1.configure(width=524)
    Text1.configure(wrap="word")
    Text1.set("Bonnjour")
"""



def recupData():
    global pays, annee
    with open('Enjeux_hippiques.csv','r') as f:
        reader = csv.reader(f)
        data =list(reader)
    datas = [d[0].split(';') for d in data]
    pays = [p[0] for p in datas]
    pays = pays[2:]
    annees = datas[0]
    annee = [int(i) for i in annees if i != '']

    titre = datas[1]
    titre = titre[1:4]
    datas = datas[2:]
    datas = [i[1:] for i in datas]

    tab =[]
    data = []
    for d in datas:
        for i in d:
            if i == 'NC'or i == '':
                tab.append(0)
            else:
                tab.append(float(i))

        data.append(tab)
        tab = []
    return data

def recupPari(data):
    pari2005 = []
    pari2006 = []
    pari2007 = []
    pari2008 = []
    pari2009 = []
    pari2010 = []
    pari2011 = []
    pari2012 = []
    pari2013 = []
    pari2014 = []
    pari2015 = []
    pari2016 = []
    for d in data:
        pari2005.append(d[0])
        pari2006.append(d[3])
        pari2007.append(d[6])
        pari2008.append(d[9])
        pari2009.append(d[12])
        pari2010.append(d[15])
        pari2011.append(d[18])
        pari2012.append(d[21])
        pari2013.append(d[24])
        pari2014.append(d[27])
        pari2015.append(d[30])
        pari2016.append(d[33])

    paris = [pari2005,pari2006, pari2007,pari2008,pari2009,pari2010,pari2011,pari2012,pari2013,pari2014, pari2015, pari2016]
    pari = dict(zip(annee, paris))
    
    return pari


def recupPop(data):
    plt2005 = [] 
    plt2006= []
    plt2007= []
    plt2008= []
    plt2009= []
    plt2010= []
    plt2011= []
    plt2012= []
    plt2013= []
    plt2014= []
    plt2015= []
    plt2016 = []
    for d in data:
        plt2005.append(d[1])
        plt2006.append(d[4])
        plt2007.append(d[7])
        plt2008.append(d[10])
        plt2009.append(d[13])
        plt2010.append(d[16])
        plt2011.append(d[19])
        plt2012.append(d[22])
        plt2013.append(d[25])
        plt2014.append(d[28])
        plt2015.append(d[31])
        plt2016.append(d[34])

    plts = [plt2005,plt2006, plt2007,plt2008,plt2009,plt2010,plt2011,plt2012,plt2013,plt2014, plt2015, plt2016]
    population = dict(zip(annee, plts))
    return population


def recupEnjeu(Data):
    enjeu2005 =[]
    enjeu2006=[]
    enjeu2007=[]
    enjeu2008=[]
    enjeu2009=[]
    enjeu2010=[]
    enjeu2011=[]
    enjeu2012=[]
    enjeu2013=[]
    enjeu2014=[]
    enjeu2015=[]
    enjeu2016=[]
    for d in data:
        enjeu2005.append(d[2])
        enjeu2006.append(d[5])
        enjeu2007.append(d[8])
        enjeu2008.append(d[11])
        enjeu2009.append(d[14])
        enjeu2010.append(d[17])
        enjeu2011.append(d[20])
        enjeu2012.append(d[23])
        enjeu2013.append(d[26])
        enjeu2014.append(d[29])
        enjeu2015.append(d[32])
        enjeu2016.append(d[35])

    enjeu = [enjeu2005,enjeu2006, enjeu2007,enjeu2008,enjeu2009,enjeu2010,enjeu2011,enjeu2012,enjeu2013,enjeu2014, enjeu2015, enjeu2016]
    enjeux = dict(zip(annee, enjeu))
    return enjeux



def etudePari(pari,an):
    etude = {'max':[pays[pari[an].index(np.max(pari[an]))], np.max(pari[an])], 
             'min':[pays[pari[an].index(np.min(pari[an]))], np.min(pari[an])],
             'moyenne':np.mean(pari[an]), 
             'totalpari':np.sum(pari[an]) 
            }
    return etude

def etudePop(enjeux, an):
    etude= {
            'max': [pays[enjeux[an].index(np.max(enjeux[an]))], np.max(enjeux[an])],
            'min': [pays[enjeux[an].index(np.min(enjeux[an]))], np.min(enjeux[an])] ,
            'total': np.sum(enjeux[an])
            }
    return etude


def tracerPari(pari, an):
    pay = [(row[0]+row[1]) for row in pays]
    p1 =plt.plot(pay,pari[an], marker='o')
    plt.xlabel('Pays')
    plt.ylabel('pari mutuel')
    plt.title('COURBE DE PARI EN FONCTION DU PAYS')
    plt.show()

def tracerPop(enjeux, an):
    pay = [(row[0]+row[1]) for row in pays]
    plt.bar(pay,enjeux[an])
    plt.xlabel('Pays')
    plt.ylabel('Enjeux pour 10 000 habitants')
    plt.title('Diagramme de l\'enjeux de la population de pari mutuel')
    plt.show()
"""
def tracerTotalPari():
    tab = []
    for an in annee:
        total = etudePari(pari,an)
        tab.append(total['totalpari'])
    plt.pie(tab, labels=annee, autopct='%1.1f%%', shadow=True, startangle=90)
    plt.show()


def tracerTotalPop():

    def etudePop(enjeux, an):
        etude= {
                'max': [pays[enjeux[an].index(np.max(enjeux[an]))], np.max(enjeux[an])],
                'min': [pays[enjeux[an].index(np.min(enjeux[an]))], np.min(enjeux[an])] ,
                'total': np.sum(enjeux[an])
                }
        return etude

    tab=[]
    for an in annee:
        enjeu = etudePop(enjeux,an)
        tab.append(enjeu['total'])
    plt.bar(annee,tab)
    plt.xlabel('annee')
    plt.ylabel('Enjeux pour 10 000 habitants')
    plt.title('Diagramme de l\'enjeux de la population mondiale de pari mutuel')
    plt.show()
"""


data = recupData()
#print(data[0])

pari = recupPari(data)
enjeux = recupEnjeu(data)
var = enjeux[2010]
#print(var)
#print(np.sum(var))
etude = etudePari(pari,2006)
etudePop = etudePop(enjeux, 2005)
#print(pari[2006])
#print(etudePop)

#tracerPo(enjeux, 2005)
#tracerTotalPari()

#tracerTotalPop(enjeux)
