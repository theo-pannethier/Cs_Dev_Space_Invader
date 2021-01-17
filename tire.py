# -*- coding: utf-8 -*-
"""
Programme contenant la classe tirer et ainsi permettant le deplacement
du missile, ainsi que ses effets sur son environement 
(destruction des ilots ou du vaisseau et autodestruction en cas de sorti du canva )

ToDo:
    -regler le probleme du 'kernel died' probablement lié aux performances 
    
Theo Pannethier / Jeffrey Simon
17/01/2021
"""

import tkinter as tk
from random import randint
from vaisseau import vaisseau2
from ilot import ilot



class tirer(tk.Tk):
    """"classe permettant le tire des aliens
    A l'origine, cette classe etait une methode de alien, mais pour une separation en fichier, 
    sa creation s'imposait"""

    def __init__(self,pListe,canva) :
        """initialisation de la classe tirer
        Entrée:
            -pListe: liste des aliens
            -canva: canva du jeu"""
        self.ListeAlien=pListe
        self.listeLaser = []
        self.laser()
        # self.permissionDeTirer()
        self.canva=canva
        self.leVaisseau = vaisseau2(self.ListeAlien,self.canva)
        self.ilot1=ilot(self.canva)

    def laser(self):
            """methode permettant la géneration des lasers """
            i=0
            while i<len(self.ListeAlien):
                
                Alien = self.ListeAlien[i]

                nbrAlea=randint(0, 100)

                if nbrAlea>99 and Alien:

                    xlaser = Alien.donneCoordsX() + (Alien.donneCoordsX2() - Alien.donneCoordsX()) / 2
                    ylaser = Alien.donneCoordsY()
                    self.rayonLaser = self.canva.create_rectangle(xlaser, ylaser+20, xlaser + 10, ylaser + 40, fill="green")

                    self.listeLaser = self.listeLaser + [self.rayonLaser]
                i+=1
            #self.canva.after(0, self.tir)
            #self.canva.after(100, self.laser)

        
    # def permissionDeTirer(self):
    #     self.canva.after(1000, self.tir)


    # def tir(self):
        # """methode permettant le deplacement des missiles des aliens, ainsi que 
        # leur gestion dynamique (colision avec le vaisseau,les blocs,sortie du canva)"""

    #     x1Vaisseau = self.leVaisseau.CoordsX()
    #     x2Vaisseau = self.leVaisseau.CoordsX2()
    #     coordIlot=self.ilot1.ilotCoord()
        
    #     w = 0
    #     i=0
    #     while i < len(self.listeLaser):
    #         laserIndice=self.listeLaser[i - w]
    #         coordlaser=self.canva.coords(laserIndice)
    #         self.canva.move(self.listeLaser[i], 0, 10)

    #         if coordlaser[1] >= 600:
    #             self.canva.delete(laserIndice)
    #             self.listeLaser.pop(i - w)
    #             w = w + 1
                
    #         if self.listeLaser != []:
    #             k=0
    #             while  k<len(coordIlot):
    #                 if coordlaser[0] >= coordIlot[k][1][0] and ( 
    #                     coordlaser[2] <= coordIlot[k][1][2] and (
    #                     coordlaser[3] >= coordIlot[k][1][1] )):
                        
    #                     self.canva.delete(laserIndice)
    #                     self.listeLaser.pop(i - w)
    #                     self.ilot1.toucheIlot( coordIlot[k][0])
    #                     w = w + 1
    #                     coordIlot=self.ilot1.ilotCoord()

    #                 k+=1
    #             if x1Vaisseau and x2Vaisseau:
    
    #                 if coordlaser[0] >= x1Vaisseau and ( 
    #                     coordlaser[2] <= x2Vaisseau and (
    #                     coordlaser[3] >= 550 )) :
                        
    #                     self.canva.delete(laserIndice)
    #                     self.listeLaser.pop(i - w)
    #                     w = w + 1
        
    #                     self.leVaisseau.destructionDuVaisseau()
    #         i+=1




