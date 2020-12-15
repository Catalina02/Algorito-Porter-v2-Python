# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 00:07:55 2020

@author: Catalina  Bustos Zurita
"""


import re
import string

'''xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'''

def REGEX(TEXTO):
    def Normalizar(TEXTO):
        TEXTO=" "+TEXTO+" " #Añadir espacio despues del texto
        #Convierte todo en Minusculas
        TEXTO=TEXTO.lower() 
        #TEXTO = re.compile("\d").sub("", TEXTO)#Elimina numeros
        #Elimina puntuacion y numero
        TEXTO = re.sub("["+string.punctuation+"]|\d|–|!|¡|´","",TEXTO)
        #Elimina Tildes
        TEXTO=re.sub("[á|ä|à|â]","a",TEXTO)
        TEXTO=re.sub("[é|ë|ê|è]","e",TEXTO)
        TEXTO=re.sub("[í|ï|î|ì]","i",TEXTO)
        TEXTO=re.sub("[ó|ö|ô|ò]","o",TEXTO)
        TEXTO=re.sub("[ú|ü|û|ù]","u",TEXTO)
        #Elimina S
        TEXTO=re.sub("[s]\s"," ",TEXTO)
        return(TEXTO)
    
    def Dimunutivos(TEXTO):
        TEXTO=re.sub("(a-z)*"+"cito"+"\s","so ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"ito"+"\s","o ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"cita"+"\s","sa ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"ita"+"\s","a ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"illo"+"\s","o ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"illa"+"\s","a ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"ico"+"\s","o ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"ica"+"\s","a ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"uelo"+"\s","o ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"uela"+"\s","a ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"in"+"\s","o ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"ina"+"\s","a ",TEXTO)
        TEXTO=re.sub("\s([a-z])\s"," ",TEXTO)
        TEXTO=re.sub("\s([a-z][a-z])\s"," ",TEXTO)
        TEXTO=re.sub("\s([a-z][a-z][a-z])\s"," ",TEXTO)
        TEXTO=re.sub("\n"," ",TEXTO)
        return(TEXTO)
    
    def Despectivos(TEXTO):
        TEXTO=re.sub("(a-z)*"+"ac"+"\s","o ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"ac"+"\s","a ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"ach"+"\s","o ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"ach"+"\s","a ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"aj"+"\s","o ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"aj"+"\s","a ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"astr"+"\s","o ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"astr"+"\s","a ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"uch"+"\s","o ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"uch"+"\s","a ",TEXTO)
        return TEXTO
        
    def Aumentativo(TEXTO):
        TEXTO=re.sub("(a-z)*"+"azo"+"\s","a ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"on"+"\s","a ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"ona"+"\s","a ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"ote"+"\s","a",TEXTO)
        TEXTO=re.sub("(a-z)*"+"ota"+"\s","a",TEXTO)
        return(TEXTO)
     
    def SufVerbos(TEXTO):
        TEXTO=re.sub("(a-z)*"+"ear"+"\s","r ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"ecer"+"\s","r ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"ificaer"+"\s","r ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"izar"+"\s","r ",TEXTO)
        return(TEXTO)
    
    def Articulos(TEXTO):
        TEXTO=re.sub("\s"+"en"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"de|del"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"el"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"la"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"lo"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"un"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"uno"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"una"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"[y]"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"que"+"\s"," ",TEXTO)
        return(TEXTO)
    
    def Adjetivos(TEXTO):
        TEXTO=re.sub("(a-z)*"+"able"+"\s"," ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"ient(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"able"+"\s","r",TEXTO)
        TEXTO=re.sub("(a-z)*"+"il"+"\s","",TEXTO)
        TEXTO=re.sub("(a-z)*"+"in(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"iz(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"os(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"ud(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"ible"+"\s","",TEXTO)
        TEXTO=re.sub("(a-z)*"+"ad(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"id(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"an(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"al(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"ar(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"ens(a|e)"+"\s"," ",TEXTO)
        TEXTO=re.sub("(a-z)*"+"eñ(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s([a-z])\s"," ",TEXTO)
        TEXTO=re.sub("\s([a-z][a-z])\s"," ",TEXTO)
        TEXTO=re.sub("\s([a-z][a-z][a-z])\s"," ",TEXTO)
        return(TEXTO)
    
    def Prefijos(TEXTO):
        #TEXTO=re.sub("\s"+"an|a"+"(a-z)*","",TEXTO)
        TEXTO=re.sub("\s"+"ante"+"(a-z)*"," ",TEXTO)
        TEXTO=re.sub("\s"+"anti"+"(a-z)*"," ",TEXTO)
        TEXTO=re.sub("\s"+"bis|bi"+"(a-z)*"," ",TEXTO)
        TEXTO=re.sub("\s"+"con|co"+"(a-z)*"," ",TEXTO)
        TEXTO=re.sub("\s"+"contra"+"(a-z)*"," ",TEXTO)
        TEXTO=re.sub("\s"+"des|de"+"(a-z)*"," ",TEXTO)
        TEXTO=re.sub("\s"+"en|entre"+"(a-z)*"," ",TEXTO)
        TEXTO=re.sub("\s"+"ex|extra"+"(a-z)*"," ",TEXTO)
        TEXTO=re.sub("\s"+"hiper"+"(a-z)*"," ",TEXTO)
        TEXTO=re.sub("\s"+"hipo"+"(a-z)*"," ",TEXTO)
        TEXTO=re.sub("\s"+"in|inter"+"(a-z)*"," ",TEXTO)
        TEXTO=re.sub("\s"+"post|pos"+"(a-z)*"," ",TEXTO)
        TEXTO=re.sub("\s"+"pre"+"(a-z)*"," ",TEXTO)
        TEXTO=re.sub("\s"+"re"+"(a-z)*"," ",TEXTO)
        TEXTO=re.sub("\s"+"sub"+"(a-z)*"," ",TEXTO)
        TEXTO=re.sub("\s"+"super"+"(a-z)*"," ",TEXTO)
        return(TEXTO)
    
    def SufSustantivo(TEXTO):
        TEXTO=re.sub("(a-z)*"+"aje"+"\s"," ",TEXTO)   
        TEXTO=re.sub("(a-z)*"+"(e|a)ncia"+"\s"," ",TEXTO)   
        TEXTO=re.sub("(a-z)*"+"(a|e|ie)nte"+"\s"," ",TEXTO)   
        TEXTO=re.sub("(a-z)*"+"a(l|r)"+"\s"," ",TEXTO)   
        TEXTO=re.sub("(a-z)*"+"ari(a|e)"+"\s"," ",TEXTO)   
        TEXTO=re.sub("(a-z)*"+"cion"+"\s"," ",TEXTO)   
        TEXTO=re.sub("(a-z)*"+"dad"+"\s"," ",TEXTO)   
        TEXTO=re.sub("(a-z)*"+"do(r|ra)"+"\s"," ",TEXTO)   
        TEXTO=re.sub("(a-z)*"+"eda"+"\s"," ",TEXTO)   
        TEXTO=re.sub("(a-z)*"+"eria"+"\s"," ",TEXTO)   
        TEXTO=re.sub("(a-z)*"+"er(a|o)"+"\s"," ",TEXTO)   
        TEXTO=re.sub("(a-z)*"+"ez"+"\s"," ",TEXTO)   
        TEXTO=re.sub("(a-z)*"+"ista"+"\s"," ",TEXTO)   
        TEXTO=re.sub("(a-z)*"+"ura"+"\s"," ",TEXTO)   
        TEXTO=re.sub("(a-z)*"+"emo"+"\s"," ",TEXTO) 
        return(TEXTO)
        
    def Pronombres(TEXTO):
        TEXTO=re.sub("\s"+"(est)+(a|e|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"es(a|e|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"aquel+(la|lo)"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"(v|n)+uestr+(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"mi+(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"(t|s)+uy+(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"dos"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"tres"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"cuatro"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"cinco"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"seis"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"siete"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"ocho"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"nueve"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"tercer+(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"segund(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"primer"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"primer+(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"alguien"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"nadie"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"nada"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"algo"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"algun+(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"algun"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"otr+(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"vari+(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"much+(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"poc+(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"para"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"yo"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"me"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"mi"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"conmigo"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"consigo"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"t+(a|e|i)"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"(v|n)+osotr+(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"ell+(a|o)"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"s+(e|i)"+"\s"," ",TEXTO)
        TEXTO=re.sub("\s"+"le"+"\s"," ",TEXTO)  
        return(TEXTO)
    
    TEXTO=Normalizar(TEXTO)
    TEXTO=Pronombres(TEXTO)
    TEXTO=Articulos(TEXTO)
    TEXTO=SufSustantivo(TEXTO)  
    TEXTO=Prefijos(TEXTO)
    TEXTO=Adjetivos(TEXTO)
    TEXTO=SufVerbos(TEXTO)
    TEXTO=Aumentativo(TEXTO)
    TEXTO=Despectivos(TEXTO)
    TEXTO=Dimunutivos(TEXTO)      
    return TEXTO

def remove_values_from_list(the_list, val): 
    return [value for value in the_list if value != val] 

'''xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'''

from tkinter import *
from tkinter import messagebox as MessageBox
from tkinter import filedialog as FileDialog
from functools import partial
import tkinter as tk

cfondo="lavender"
ctitulos="mediumpurple4"
cboton="purple4"
cletraboton="lavender"
root=Tk()
#root.iconbitmap("icono.ico")
#root.tk.call("wm","iconphoto",root._w,tk.PhotoImage(file"icono.png"))
root.title("Algoritmo de Porter")

root.resizable(0,0)

frame=Frame(root,width=300,height=300)
frame.pack()
frame.config(bg=cfondo,bd=5,relief="groove")
    #titulo
label1=Label(root,text="Algoritmo de Porter", 
                 foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",16))
label1.place(x=38, y=10)

'''xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'''

def ListaPalabras(TEXTO):
    FREC=[]
    for k in TEXTO:
        FREC.append(TEXTO.count(k))
    return dict(list(zip(TEXTO,FREC)))

def ordenaDicFrec(dicfrec):
    aux = [(dicfrec[key], key) for key in dicfrec]
    aux.sort()
    aux.reverse()
    return aux

'''xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'''



def MenuDesplegable(TEXTO):
    frame.destroy()
    frame2=Frame(root,width=300,height=475)
    frame2.pack()
    
    frame2.config(bg=cfondo)     
    
    label1=Label(root,text="Algoritmo de Porter", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",16))
    label1.place(x=30, y=10)
    
    frame3=Frame(root,width=200,height=375)
    
    frame3.config(bg=cfondo,relief="groove",bd=2)  
    frame3.place(x=50, y=60)
    
    label2=Label(root, text="15 Palabras más Utilizadas",bg=cfondo,
                 font=("Arial Black",8)) 
    label2.place(x=65, y=65)
    
    label3=Label(root, text="Frecuencia",foreground="black",bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=60, y=100)
    
    label3=Label(root, text="Palabras",foreground="black",bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=170, y=100)
    
   
    #etiqueta 15 frecuencias
    label3=Label(root, text=TEXTO[0][0],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=90, y=120)
    label3=Label(root, text=TEXTO[1][0],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=90, y=140)
    label3=Label(root, text=TEXTO[2][0],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=90, y=160)
    label3=Label(root, text=TEXTO[3][0],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=90, y=180)
    label3=Label(root, text=TEXTO[4][0],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=90, y=200)
    label3=Label(root, text=TEXTO[5][0],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=90, y=220)
    label3=Label(root, text=TEXTO[6][0],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=90, y=240)
    label3=Label(root, text=TEXTO[7][0],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=90, y=260)
    label3=Label(root, text=TEXTO[8][0],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=90, y=280)
    label3=Label(root, text=TEXTO[9][0],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=90, y=300)
    label3=Label(root, text=TEXTO[10][0],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=90, y=320)
    label3=Label(root, text=TEXTO[11][0],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=90, y=340)
    label3=Label(root, text=TEXTO[12][0],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=90, y=360)
    label3=Label(root, text=TEXTO[13][0],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=90, y=380)
    label3=Label(root, text=TEXTO[14][0],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=90, y=400)
   
    #etiqueta 15 Palabras
    label3=Label(root, text=TEXTO[0][1],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=180, y=120)
    label3=Label(root, text=TEXTO[1][1],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=180, y=140)
    label3=Label(root, text=TEXTO[2][1],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=180, y=160)
    label3=Label(root, text=TEXTO[3][1],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=180, y=180)
    label3=Label(root, text=TEXTO[4][1],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=180, y=200)
    label3=Label(root, text=TEXTO[5][1],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=180, y=220)
    label3=Label(root, text=TEXTO[6][1],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=180, y=240)
    label3=Label(root, text=TEXTO[7][1],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=180, y=260)
    label3=Label(root, text=TEXTO[8][1],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=180, y=280)
    label3=Label(root, text=TEXTO[9][1],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=180, y=300)
    label3=Label(root, text=TEXTO[10][1],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=180, y=320)
    label3=Label(root, text=TEXTO[11][1],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=180, y=340)
    label3=Label(root, text=TEXTO[12][1],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=180, y=360)
    label3=Label(root, text=TEXTO[13][1],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=180, y=380)
    label3=Label(root, text=TEXTO[14][1],foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8)) 
    label3.place(x=180, y=400)
   
    
    root.mainloop()     

'''xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx''' 

def error(cadenaString):
     if(len(cadenaString)<15):
       MessageBox.showerror("Error", "Minimo Ingrese 15 Palabras distintas")
       frame.destroy()
       frame2=Frame(root,width=300,height=300)
       frame2.place(x=0,y=0)
       frame2.config(bg=cfondo)     
       label1=Label(root,text="Algoritmo de Porter", 
                     foreground=ctitulos,bg=cfondo,
                     font=("Arial Black",16))
       label1.place(x=30, y=10)
       Menu()

'''xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx''' 
def LeerTexto(TEXTO):
   texto=TEXTO.get(1.0,END)
   textoNormalizado=REGEX(texto)
   cadenaString=textoNormalizado.split(" ")
   cadenaString=remove_values_from_list(cadenaString, "") 
   
   cadenaString=ListaPalabras(cadenaString)
   cadenaString=ordenaDicFrec(cadenaString)
   
   error(cadenaString)
  
   MenuDesplegable(cadenaString)
 

'''xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'''   

def IngresarTXT():
    fichero = FileDialog.askopenfilename(title="Abrir un txt")
    archivo=open(fichero,"r", encoding="utf8")
    texto=archivo.read()
    archivo.close()
    textoNormalizado=REGEX(texto)
    cadenaString=textoNormalizado.split(" ")
    cadenaString=remove_values_from_list(cadenaString, "") 
   
    cadenaString=ListaPalabras(cadenaString)
    cadenaString=ordenaDicFrec(cadenaString)
    error(cadenaString)
    MenuDesplegable(cadenaString)
 

'''xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'''
    
def IngresarManual():
        texto = Text(root)
    
        texto.config(width=30, height=10, 
                  selectbackground="lavender",font=("Arial",11))
        texto.place(x=28, y=50)
        boton=Button(root,text="Resultados",
                     foreground=cletraboton,bg=cboton ,
                     command=partial(LeerTexto,texto),
                     font=("Arial",10),bd=3)
        boton.place(x=109,y=230)
       
'''xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'''
        
def Menu():
    
    #cuadro
    
    #bajada
    label1=Label(root,text="Programa entrega las 15 palabras\nmás repetidas de un texto", 
                 foreground=ctitulos,bg=cfondo,
                 font=("Arial",8))
    label1.place(x=65, y=45)
    
    #botones
    button1=Button(root,text="Ingreso por .txt", 
                 foreground=cletraboton,bg=cboton,
                 font=("Arial",10),command=IngresarTXT,bd=3)
    button1.place(x=100, y=120)
    
    button2=Button(root,text=" Ingreso Manual ", 
                 foreground=cletraboton,bg=cboton,
                 font=("Arial",10),command=IngresarManual,bd=3)
    button2.place(x=95, y=170)
    
    label3=Label(root,text="Autora Catalina Bustos Zurita", 
                 foreground=ctitulos,bg=cfondo,
                 font=("Arial Black",8))
    label3.place(x=58, y=270)
    
    root.mainloop()

Menu()