# -*- coding: utf-8 -*-
"""
Programme contenant la classe alien et ainsi permettant le tire sans deplacement
du missile, le deplacement des aliens, et leur destruction

ToDo:
    
Theo Pannethier / Jeffrey Simon
17/01/2021
"""




import tkinter as tk
from vaisseau import vaisseau2



class Alien(tk.Tk):
    """classe permettant la gestion des aliens
    (chaque alien est independant et representeun appel à Alien)"""
    def __init__(self,n,canva):
        """initialisation de la classe alien
        Entrée:
            -n : indice de l'alien crée"""
        self.n = n
        self.canva=canva
        self.x = 100+self.n*100
        self.y = 30
        self.dx = 10
        self.allee = 0
        self.alien =  self.canva.create_rectangle(self.x, self.y, self.x + 20, self.y + 20, fill="white")
        self.move(self.dx, self.allee)
#         self.listeLaser = []
        # self.laser()
        # self.permissionDeTirer()


    """les methodes suivantes permettent de recuperer les coordonnées de chaque
    alien à l'exterieur de la classe """

    def donneCoordsX(self):
        return  self.canva.coords(self.alien)[0]
    def donneCoordsX2(self):
        return  self.canva.coords(self.alien)[2]
    def donneCoordsY(self):
        return  self.canva.coords(self.alien)[1]
    def donneCoordsY2(self):
        return  self.canva.coords(self.alien)[3]
    
    
    
    
    def destroyAlien(self):
        """programme qui appelé, permet de supprimer l'alien"""
        self.canva.delete(self.alien)
        return 'gagné'

    def move (self, dx, allee):
        """programme gerant le deplacement horizontale et verticale de l'alien
        Entrée:
            -dx : permet de donner la vitesse à l'alien, ici soit 10 soit -10 
                  en fonction de la direction de deplacement.
            -allee : permet de compter le nombre d'aller effectué"""
        if  self.canva.coords(self.alien) == []:
            return "gagné"
        self.canva.move(self.alien, dx, 0)
        if  self.canva.coords(self.alien)[2] > 1050:
            dx=-10
            allee=allee+1
        if  self.canva.coords(self.alien)[0] < 50:
            dx=10
            allee=allee+1

        if allee == 2 :
            allee = 0
           
            self.canva.move(self.alien, 0, 30)
            if self.canva.coords(self.alien)[1] > 400:
                a = vaisseau2.destructionDuVaisseau()
                return a

        self.canva.after(100, lambda : self.move(dx, allee) )
