# -*- coding: utf-8 -*-
"""
Programme gerant la partie graphique.

ToDo:
    -faire le bouton qui declanche la partie ~ 
    -menu proposant differantes possibilitées
    -inserer image alien et vaisseau
Theo Pannethier / Jeffrey Simon
17/12/2020
"""


from  tkinter import Tk,Button,Frame,PhotoImage,Canvas


    
Fenetre = Tk()
Fenetre.geometry('1200x600+75+20')
Fond = PhotoImage(file = 'FondJeu.gif')

canva = Canvas(Fenetre,height=600 , width=1100)
item = canva.create_image(0,0,anchor='nw',image = Fond )
canva.grid(row=0, column=0)

menu = Frame(Fenetre)
menu.grid(row=0, column=1)
QuitBouton = Button(menu,text= "Quit", fg = 'red',width=10,
                    command = Fenetre.destroy)
NewGameBouton = Button(menu,text= "New game", fg = 'red',width=10)
NewGameBouton.pack(padx=0,pady=0)
QuitBouton.pack(padx=0,pady=100)


Fenetre.mainloop()



#Fenetre.coords