from tkinter import *
import tkinter as tk
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
from tkinter.messagebox import *
from fonctions import *



def nouvelleFenetrePari(root,pari,an):

    etude = etudePari(pari,an)
    tracerPari(pari, an)
    fenetrePari=Toplevel(root)
    fenetrePari.geometry("694x450+292+105")
    fenetrePari.iconbitmap("cheval.ico")
    fenetrePari.title("Pari Sportif")        
    fenetrePari.configure(background="#d9d9d9")



    Framecontainer = tk.Frame(fenetrePari)
    Framecontainer.place(relx=0.115, rely=0.089, relheight=0.678
                , relwidth=0.785)
    Framecontainer.configure(relief='groove')
    Framecontainer.configure(borderwidth="2")
    Framecontainer.configure(relief="groove")
    Framecontainer.configure(background="#d9d9d9")
    Framecontainer.configure(width=545)

    Labelframegrand = tk.LabelFrame(Framecontainer)
    Labelframegrand.place(relx=0.055, rely=0.098, relheight=0.475
                 , relwidth=0.367)
    Labelframegrand.configure(relief='groove')
    Labelframegrand.configure(foreground="black")
    Labelframegrand.configure(text='''Plus grand pari mutuel''')
    Labelframegrand.configure(background="#d9d9d9")
    Labelframegrand.configure(width=200)
  
    Label1 = tk.Label(Labelframegrand)
    Label1.place(relx=0.05, rely=0.276, height=21, width=94
                 , bordermode='ignore')
    Label1.configure(background="#d9d9d9")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(foreground="#000000")
    Label1.configure(text='''Pays :''')
    Label1.configure(width=94)
  
    Label2 = tk.Label(Labelframegrand)
    Label2.place(relx=0.0, rely=0.552, height=21, width=94
                  , bordermode='ignore')
    Label2.configure(background="#d9d9d9")
    Label2.configure(disabledforeground="#a3a3a3")
    Label2.configure(foreground="#000000")
    Label2.configure(text='''Somme(en $) :''')
    Label2.configure(width=94)
   
    Label3 = tk.Label(Labelframegrand)
    Label3.place(relx=0.55, rely=0.276, height=21, width=64
                 , bordermode='ignore')
    Label3.configure(background="#d9d9d9")
    Label3.configure(disabledforeground="#a3a3a3")
    Label3.configure(foreground="#000000")
    Label3.configure(text= etude['max'][0])
    Label3.configure(width=64)
  
    Label4 = tk.Label(Labelframegrand)
    Label4.place(relx=0.55, rely=0.552, height=21, width=54
                 , bordermode='ignore')
    Label4.configure(background="#d9d9d9")
    Label4.configure(disabledforeground="#a3a3a3")
    Label4.configure(foreground="#000000")
    Label4.configure(text= etude['max'][1])
    Label4.configure(width=54)
  
    LabelframePetit = tk.LabelFrame(Framecontainer)
    LabelframePetit.place(relx=0.514, rely=0.131, relheight=0.443
                 , relwidth=0.422)
    LabelframePetit.configure(relief='groove')
    LabelframePetit.configure(foreground="black")
    LabelframePetit.configure(text='''Plus petit pari''')
    LabelframePetit.configure(background="#d9d9d9")
    LabelframePetit.configure(width=230)
  
    Label5 = tk.Label(LabelframePetit)
    Label5.place(relx=0.043, rely=0.222, height=21, width=64
                  , bordermode='ignore')
    Label5.configure(background="#d9d9d9")
    Label5.configure(disabledforeground="#a3a3a3")
    Label5.configure(foreground="#000000")
    Label5.configure(text='''Pays :''')
    Label5.configure(width=64)
 
    Label6 = tk.Label(LabelframePetit)
    Label6.place(relx=0.600, rely=0.222, height=21, width=100
                  , bordermode='ignore')
    Label6.configure(background="#d9d9d9")
    Label6.configure(disabledforeground="#a3a3a3")
    Label6.configure(foreground="#000000")
    Label6.configure(text= etude['min'][0])
 
    Label7 = tk.Label(LabelframePetit)
    Label7.place(relx=0.043, rely=0.593, height=21, width=83
                 , bordermode='ignore')
    Label7.configure(background="#d9d9d9")
    Label7.configure(disabledforeground="#a3a3a3")
    Label7.configure(foreground="#000000")
    Label7.configure(text='''Somme(en $) :''')
    
    Label8 = tk.Label(LabelframePetit)
    Label8.place(relx=0.652, rely=0.593, height=21, width=44
                  , bordermode='ignore')
    Label8.configure(background="#d9d9d9")
    Label8.configure(disabledforeground="#a3a3a3")
    Label8.configure(foreground="#000000")
    Label8.configure(text= etude['min'][1])
    Label8.configure(width=44)
  
    FrameStat = tk.Frame(Framecontainer)
    FrameStat.place(relx=0.055, rely=0.656, relheight=0.246
                 , relwidth=0.908)
    FrameStat.configure(relief='groove')
    FrameStat.configure(borderwidth="2")
    FrameStat.configure(relief="groove")
    FrameStat.configure(background="#d9d9d9")
    FrameStat.configure(width=495)
 
    Label9 = tk.Label(FrameStat)
    Label9.place(relx=0.02, rely=0.267, height=21, width=114)
    Label9.configure(background="#d9d9d9")
    Label9.configure(disabledforeground="#a3a3a3")
    Label9.configure(foreground="#000000")
    Label9.configure(text='''Pari moyen ($) :''')
    Label9.configure(width=114)
  
    Label10 = tk.Label(FrameStat)
    Label10.place(relx=0.263, rely=0.267, height=21, width=64)
    Label10.configure(background="#d9d9d9")
    Label10.configure(disabledforeground="#a3a3a3")
    Label10.configure(foreground="#000000")
    Label10.configure(text=etude['moyenne'])
    Label10.configure(width=64)
 
    Label11 = tk.Label(FrameStat)
    Label11.place(relx=0.505, rely=0.267, height=31, width=74)
    Label11.configure(background="#d9d9d9")
    Label11.configure(disabledforeground="#a3a3a3")
    Label11.configure(foreground="#000000")
    Label11.configure(text='''Pari total ($):''')
    Label11.configure(width=74)
 
    Label12 = tk.Label(FrameStat)
    Label12.place(relx=0.727, rely=0.267, height=21, width=64)
    Label12.configure(background="#d9d9d9")
    Label12.configure(disabledforeground="#a3a3a3")
    Label12.configure(foreground="#000000")
    Label12.configure(text=etude['totalpari'])
    Label12.configure(width=64)
  
   



def nouvelleFenetrePop(root,enjeux,an):
    def etudePop(enjeu, ann):
        etude= {
                'max': [pays[enjeux[an].index(np.max(enjeux[an]))], np.max(enjeux[an])],
                'min': [pays[enjeux[an].index(np.min(enjeux[an]))], np.min(enjeux[an])] ,
                'total': np.sum(enjeux[an])
                }
        return etude

    etude =  etudePop(enjeux, an)
    tracerPop(enjeux, an)
    fenetrePop=Toplevel(root)
    fenetrePop.geometry("586x450+341+122")
    fenetrePop.iconbitmap("cheval.ico")
    fenetrePop.title("Pari Sportif")        
    fenetrePop.configure(background="#d9d9d9")


    Labelframegrand = tk.LabelFrame(fenetrePop)
    Labelframegrand.place(relx=0.051, rely=0.178, relheight=0.589, relwidth=0.392)
    Labelframegrand.configure(relief='groove')
    Labelframegrand.configure(foreground="black")
    Labelframegrand.configure(text='''Plus grand enjeux(10.000hbts)''')
    Labelframegrand.configure(background="#d9d9d9")
    Labelframegrand.configure(width=200)
  
    Label1 = tk.Label(Labelframegrand)
    Label1.place(relx=0.05, rely=0.276, height=21, width=94
                 , bordermode='ignore')
    Label1.configure(background="#d9d9d9")
    Label1.configure(disabledforeground="#a3a3a3")
    Label1.configure(foreground="#000000")
    Label1.configure(text='''Pays :''')
    Label1.configure(width=94)
  
    Label2 = tk.Label(Labelframegrand)
    Label2.place(relx=0.0, rely=0.552, height=21, width=94
                  , bordermode='ignore')
    Label2.configure(background="#d9d9d9")
    Label2.configure(disabledforeground="#a3a3a3")
    Label2.configure(foreground="#000000")
    Label2.configure(text='''Enjeux ($) :''')
    Label2.configure(width=94)
   
    Label3 = tk.Label(Labelframegrand)
    Label3.place(relx=0.55, rely=0.276, height=21, width=64
                 , bordermode='ignore')
    Label3.configure(background="#d9d9d9")
    Label3.configure(disabledforeground="#a3a3a3")
    Label3.configure(foreground="#000000")
    Label3.configure(text= etude['max'][0])
    Label3.configure(width=64)
  
    Label4 = tk.Label(Labelframegrand)
    Label4.place(relx=0.55, rely=0.552, height=21, width=54
                 , bordermode='ignore')
    Label4.configure(background="#d9d9d9")
    Label4.configure(disabledforeground="#a3a3a3")
    Label4.configure(foreground="#000000")
    Label4.configure(text= '%11.1f'%(etude['max'][1]))
    Label4.configure(width=54)
  
    LabelframePetit = tk.LabelFrame(fenetrePop)
    LabelframePetit.place(relx=0.528, rely=0.178, relheight=0.589  , relwidth=0.409)
    LabelframePetit.configure(relief='groove')
    LabelframePetit.configure(foreground="black")
    LabelframePetit.configure(text='''Plus petit enjeux(10.000hbts)''')
    LabelframePetit.configure(background="#d9d9d9")
    LabelframePetit.configure(width=230)
  
    Label5 = tk.Label(LabelframePetit)
    Label5.place(relx=0.043, rely=0.222, height=21, width=64
                  , bordermode='ignore')
    Label5.configure(background="#d9d9d9")
    Label5.configure(disabledforeground="#a3a3a3")
    Label5.configure(foreground="#000000")
    Label5.configure(text='''Pays :''')
    Label5.configure(width=64)
 
    Label6 = tk.Label(LabelframePetit)
    Label6.place(relx=0.600, rely=0.222, height=21, width=100
                  , bordermode='ignore')
    Label6.configure(background="#d9d9d9")
    Label6.configure(disabledforeground="#a3a3a3")
    Label6.configure(foreground="#000000")
    Label6.configure(text= etude['min'][0])
 
    Label7 = tk.Label(LabelframePetit)
    Label7.place(relx=0.043, rely=0.593, height=21, width=83
                 , bordermode='ignore')
    Label7.configure(background="#d9d9d9")
    Label7.configure(disabledforeground="#a3a3a3")
    Label7.configure(foreground="#000000")
    Label7.configure(text='''Enjeux ($) :''')
    
    Label8 = tk.Label(LabelframePetit)
    Label8.place(relx=0.652, rely=0.593, height=21, width=44
                  , bordermode='ignore')
    Label8.configure(background="#d9d9d9")
    Label8.configure(disabledforeground="#a3a3a3")
    Label8.configure(foreground="#000000")
    Label8.configure(text= '%11.1f'%(etude['min'][1]))
    Label8.configure(width=44)
  
