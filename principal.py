"""
Programme gerant la partie graphique.

ToDo:
    -faire le bouton qui declanche la partie ~ 
    -menu proposant differantes possibilitées
    -inserer image alien et vaisseau
Theo Pannethier / Jeffrey Simon
17/12/2020
"""
import tkinter as tk
from random import *

score=10
score= str(score)
from  tkinter import Tk,Button,Frame,PhotoImage,Canvas,Label
import tkinter.font as tkFont

    
Fenetre = Tk()
Fenetre.geometry('1200x600+75+20')
Fond = PhotoImage(file = 'FondJeu.gif')
normal = tkFont.Font(family='Helvetica',size=12)
ptmarq=tkFont.Font(family='Helvetica',size=14, weight='bold')

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
class vaisseau(tk.Tk):
    def __init__(self,pListeAlien):


        self.x=w//2
        self.y=550
        self.listeAlien=pListeAlien
        self.liste2=[1,2,3,4]
        self.listeInterdite=[]
        self.vaisseaux=canva.create_rectangle(self.x, self.y, self.x+40, self.y+40, fill="red")
        self.lmissile=[]
        self.dynmissile(self.listeAlien,self.liste2,self.listeInterdite)
        canva.bind_all("<Key>", self.bouger)
        canva.bind_all("w", self.missiles)
    def destructionDuVaisseau(self):
        canva.delete(self.vaisseaux)
        return 'perdu'
    def CoordsX(self):
        return canva.coords(self.vaisseaux)[0]
    def CoordsX2(self):
        return canva.coords(self.vaisseaux)[2]
    def bouger(self, event):
        x,y=0,0
        if event.char=='q':
           x=-10
        if event.char=='d':
            x=10

        canva.move(self.vaisseaux,x,y)

    def missiles(self, event):
        xmissile=canva.coords(self.vaisseaux)[0]+(canva.coords(self.vaisseaux)[2]-
                                                  canva.coords(self.vaisseaux)[0])/2
        ymissile = canva.coords(self.vaisseaux)[1]
        self.missile = canva.create_rectangle(xmissile, ymissile, xmissile + 10, ymissile - 20, fill="blue")
        self.lmissile=self.lmissile+[self.missile]


    def dynmissile(self,liste,liste2,listeInterdite):
        annule=False
        Listecoord=[]
        for i in range (len(liste2)):
            '''boucle for permettant la recuperation des coordonées de chaque alien'''

            ListeCoordAlien=[]
            ListeCoordAlien.append(liste[i].donneCoordsX())
            ListeCoordAlien.append(liste[i].donneCoordsX2())
            ListeCoordAlien.append(liste[i].donneCoordsY())
            ListeCoordAlien.append(liste[i].donneCoordsY2())
            Listecoord.append(ListeCoordAlien)


        w=0


        for i in range (0,len(self.lmissile)):
            canva.move(self.lmissile[i-w],0,-10)
            if canva.coords(self.lmissile[i-w])[1]<=0:
                canva.delete(self.lmissile[i - w])
                self.lmissile.pop(i - w)
                w = w + 1
            if self.lmissile != []:


                for k in range( len(liste2)):
                    if canva.coords(self.lmissile[i - w])[0] >= Listecoord[k][0] and canva.coords(self.lmissile[i - w])[
                        2] <= Listecoord[k][1] and ((canva.coords(self.lmissile[i - w])[1] >= Listecoord[k][2] and
                                             canva.coords(self.lmissile[i - w])[1] <= Listecoord[k][3]) or (
                                                    canva.coords(self.lmissile[i - w])[3] >= Listecoord[k][2] and
                                                    canva.coords(self.lmissile[i - w])[3] <= Listecoord[k][3])):
                        val=liste2[k]


                        if val not in listeInterdite:
                            liste[k].destroyAlien()
                            liste.pop(k)
                            liste2.remove(val)

                            canva.delete(self.lmissile[i - w])
                            self.lmissile.pop(i - w)
                            w = w + 1


                            listeInterdite.append(val)
                            annule=True
                            break
                if annule==True:
                    break



        canva.after(50,self.dynmissile,liste,liste2,listeInterdite)




class Alien(tk.Tk):
    def __init__(self,n):

        self.n = n
        self.x= 100+self.n*100
        self.y = 30
        self.dx = 10
        self.allee=0
        self.alien = canva.create_rectangle(self.x, self.y, self.x + 20, self.y + 20, fill="white")
        self.move(self.dx, self.allee)
        self.lLaser=[]
        self.laser()
        self.permissionDeTirer()




    def donneCoordsX(self):
        return canva.coords(self.alien)[0]
    def donneCoordsX2(self):
        return canva.coords(self.alien)[2]
    def donneCoordsY(self):
        return canva.coords(self.alien)[1]
    def donneCoordsY2(self):
        return canva.coords(self.alien)[3]
    def destroyAlien(self):
        canva.delete(self.alien)
        return 'gagné'
    
    def laser(self):


        nbrAlea=randint(0, 100)
        if nbrAlea>80:

            xlaser = canva.coords(self.alien)[0] + (
                    canva.coords(self.alien)[2] - canva.coords(self.alien)[0]) / 2
            ylaser = canva.coords(self.alien)[1]
            self.rayonLaser = canva.create_rectangle(xlaser, ylaser+20, xlaser + 10, ylaser + 40, fill="green")

            self.lLaser = self.lLaser + [self.rayonLaser]




        canva.after(500, self.laser)

    def permissionDeTirer(self):
        canva.after(1000, self.tir)


    def tir(self):


        x1Vaisseau = leVaisseau.CoordsX()
        x2Vaisseau = leVaisseau.CoordsX2()

        w = 0

        for i in range(0, len(self.lLaser)):
            canva.move(self.lLaser[i - w], 0, 10)
            if canva.coords(self.lLaser[i - w])[1] >= 1000:
                canva.delete(self.lLaser[i - w])
                self.lLaser.pop(i - w)
                w = w + 1
            if self.lLaser != []:
                if canva.coords(self.lLaser[i - w])[0] >= x1Vaisseau and canva.coords(self.lLaser[i - w])[2] <= x2Vaisseau and canva.coords(self.lLaser[i - w])[1] >= 980:
                    canva.delete(self.lLaser[i - w])
                    self.lLaser.pop(i - w)
                    w = w + 1
                    leVaisseau.destructionDuVaisseau()



            canva.after(100, self.tir)

    def move (self, dx, allee):

        if canva.coords(self.alien)==[]:
            return "gagné"
        canva.move(self.alien, dx, 0)
        if canva.coords(self.alien)[2]>1050:
            dx=-10
            allee=allee+1
        if canva.coords(self.alien)[0]<50:
            dx=10
            allee=allee+1

        if allee==2:
            allee=0
            canva.move(self.alien, 0, 30)
            if canva.coords(self.alien)[1]>400:
                a =leVaisseau.destructionDuVaisseau()
                return a




        canva.after(100, self.move, dx, allee)


listeAlien=[]

nbrAlienLigne=4


for i in range(nbrAlienLigne):
    listeAlien.append(Alien(i))


leVaisseau=vaisseau(listeAlien)

#boutton quiter


#afficher la fenetre
Fenetre.mainloop()

