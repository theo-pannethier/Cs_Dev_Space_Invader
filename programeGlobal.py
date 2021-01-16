# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:44:02 2021

@author: Theo Pannethier
"""

import tkinter as tk
from vaisseau import vaisseau2
from ilot import ilot 
from alien import Alien
score=10
score= str(score)
from  tkinter import Tk,Button,Frame,PhotoImage,Canvas,Label
import tkinter.font as tkFont

    
Fenetre = Tk()
Fenetre.geometry('1200x600+75+20')
Fond = PhotoImage(file = 'FondJeu.gif')
normal = tkFont.Font(family = 'Helvetica',size=12)
ptmarq=tkFont.Font(family='Helvetica',size=14, weight='bold')
Fenetre.title('Space Invader ' )
canva = Canvas(Fenetre,height=600 , width=1100)
item = canva.create_image(0,0,anchor='nw',image = Fond )
canva.grid(row=0, column=0)

menu = Frame(Fenetre)
menu.grid(row=0, column=1)
QuitBouton = Button(menu,text= "Quit", fg = 'red',width=10,
                    command = Fenetre.destroy)
NewGameBouton = Button(menu,text= "New game", fg = 'red',width=10)
test = Label(menu , text='score : ' + score , font=normal )
test.config()
NewGameBouton.pack(padx=0,pady=0)
QuitBouton.pack(padx=0,pady=100)
test.pack()
w=1100
height=600



listeAlien = []
nbrAlienLigne = 8                  
for i in range(nbrAlienLigne):
    listeAlien.append(Alien(i,canva))

leVaisseau = vaisseau2(listeAlien,canva)
ilot=ilot(canva)



#afficher la fenetre
Fenetre.mainloop()