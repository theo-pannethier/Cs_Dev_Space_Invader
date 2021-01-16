# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:35:03 2021

@author: Theo Pannethier
"""


import tkinter as tk



class vaisseau2(tk.Tk):
    def __init__(self,pListeAlien,canva):
        w=1100
        self.canva=canva
        #self.imageVaisseau = PhotoImage(file = "vaisseau.png")  #création image de fond du vaisseau
        self.x=w//2
        self.y=550
        self.listeAlien=pListeAlien
        self.vivant=True
        self.listeIndice=[]
        self.listeInterdite=[]
        self.vaisseaux=self.canva.create_rectangle(self.x, self.y, self.x+40, self.y+40, fill="red")
        self.lmissile=[]
        self.listeIndiceAlien()
        self.dynmissile(self.listeAlien,self.listeIndice,self.listeInterdite)
        self.canva.bind_all("<Left>", lambda direction='Left':self.bouger(direction))
        self.canva.bind_all("<Right>", lambda direction='Right':self.bouger(direction))
        self.canva.bind_all("<Key>", self.missiles)
        
    def listeIndiceAlien(self):
        for i in range ( len(self.listeAlien) ):
            self.listeIndice.append(i+1)
        
    def destructionDuVaisseau(self):
        self.canva.delete(self.vaisseaux)
        self.vivant=False
        return 'perdu'
    def CoordsX(self):
        if self.canva.coords(self.vaisseaux) :
            return self.canva.coords(self.vaisseaux)[0]
       
    def CoordsX2(self):
        if self.canva.coords(self.vaisseaux) :
            return self.canva.coords(self.vaisseaux)[2]
        
    def bouger(self, event):
        x,y=0,0
        if event.keysym == 'Left':
           x=-10
        if event.keysym == 'Right':
            x=10

        self.canva.move(self.vaisseaux,x,y)



    def missiles(self, event):
        
        if  self.vivant and  event.keysym=='space':
    
            xmissile=self.canva.coords(self.vaisseaux)[0]+(self.canva.coords(self.vaisseaux)[2]-
                                            self.canva.coords(self.vaisseaux)[0])/2
            ymissile = self.canva.coords(self.vaisseaux)[1]
            self.missile = self.canva.create_rectangle(xmissile-5, ymissile, xmissile + 5, ymissile - 20, fill="blue")
            self.lmissile=self.lmissile+[self.missile]


    def dynmissile(self,liste,listeIndice,listeInterdite):
        annule=False
        Listecoord=[]
        for i in range (len(listeIndice)):
            '''boucle for permettant la recuperation des coordonées de chaque alien'''

            ListeCoordAlien=[]
            ListeCoordAlien.append(liste[i].donneCoordsX())
            ListeCoordAlien.append(liste[i].donneCoordsX2())
            ListeCoordAlien.append(liste[i].donneCoordsY())
            ListeCoordAlien.append(liste[i].donneCoordsY2())
            Listecoord.append(ListeCoordAlien)


        w=0

        for i in range (0,len(self.lmissile)):
            objetMissile=self.lmissile[i-w]
            self.canva.move(objetMissile,0,-10)
            if self.canva.coords(objetMissile)[1]<=0:
                self.canva.delete(objetMissile)
                self.lmissile.pop(i - w)
                w = w + 1
            if self.lmissile != []:


                for k in range( len(listeIndice)):
                    objetMissile=self.lmissile[i - w]
                    if self.canva.coords(objetMissile)[0] >= Listecoord[k][0] and self.canva.coords(objetMissile)[
                        2] <= Listecoord[k][1] and ((self.canva.coords(objetMissile)[1] >= Listecoord[k][2] and
                                             self.canva.coords(objetMissile)[1] <= Listecoord[k][3]) or (
                                                    self.canva.coords(objetMissile)[3] >= Listecoord[k][2] and
                                                    self.canva.coords(objetMissile)[3] <= Listecoord[k][3])):
                        val=listeIndice[k]


                        if val not in listeInterdite:
                            liste[k].destroyAlien()
                            liste.pop(k)
                            listeIndice.remove(val)

                            self.canva.delete(self.lmissile[i - w])
                            self.lmissile.pop(i - w)
                            w = w + 1


                            listeInterdite.append(val)
                            annule = True
                            break
                if annule == True:
                    break


        self.canva.after(50,self.dynmissile,liste,listeIndice,listeInterdite)