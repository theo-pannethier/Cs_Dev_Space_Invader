# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:26:51 2021

@author: Theo Pannethier
"""



from random import randint
import tkinter as tk
from vaisseau import vaisseau2
from ilot import ilot


class Alien(tk.Tk):
    def __init__(self,n,canva):

        self.n = n
        self.canva=canva
        self.x = 100+self.n*100
        self.y = 30
        self.dx = 10
        self.allee = 0
        self.alien =  self.canva.create_rectangle(self.x, self.y, self.x + 20, self.y + 20, fill="white")
        self.move(self.dx, self.allee)
        self.listeLaser = []
        self.laser()
        self.permissionDeTirer()




    def donneCoordsX(self):
        return  self.canva.coords(self.alien)[0]
    def donneCoordsX2(self):
        return  self.canva.coords(self.alien)[2]
    def donneCoordsY(self):
        return  self.canva.coords(self.alien)[1]
    def donneCoordsY2(self):
        return  self.canva.coords(self.alien)[3]
    def destroyAlien(self):
         self.canva.delete(self.alien)
         return 'gagné'
    
    def laser(self):

        coordAlien =  self.canva.coords(self.alien)
        nbrAlea=randint(0, 100)
        if nbrAlea>90 and coordAlien:
            xlaser = coordAlien[0] + (coordAlien[2] - coordAlien[0]) / 2
            ylaser = coordAlien[1]
            self.rayonLaser =  self.canva.create_rectangle(xlaser, ylaser+20, xlaser + 10, ylaser + 40, fill="green")
            self.listeLaser = self.listeLaser + [self.rayonLaser]

        self.canva.after(0, self.tir)
        self.canva.after(100, self.laser)

    def permissionDeTirer(self):
         self.canva.after(1000, self.tir)


    def tir(self):

        leVaisseau=vaisseau2()
        x1Vaisseau = leVaisseau.CoordsX()
        x2Vaisseau = leVaisseau.CoordsX2()
        coordIlot=ilot.ilotCoord()
        
        w = 0
        i=0
        while i < len(self.listeLaser):
            laserIndice=self.listeLaser[i - w]
            coordlaser= self.canva.coords(laserIndice)
            self.canva.move(self.listeLaser[i], 0, 10)

            if coordlaser[1] >= 600:
                self.canva.delete(laserIndice)
                self.listeLaser.pop(i - w)
                w = w + 1
                
            if self.listeLaser != []:
                k=0
                while  k<len(coordIlot):
                    if coordlaser[0] >= coordIlot[k][1][0] and ( 
                       coordlaser[2] <= coordIlot[k][1][2] and (
                       coordlaser[3] >= coordIlot[k][1][1] )):
                        
                        self.canva.delete(laserIndice)
                        self.listeLaser.pop(i - w)
                        ilot.toucheIlot( coordIlot[k][0])
                        w = w + 1
                        coordIlot=ilot.ilotCoord()

                    k+=1
                if x1Vaisseau and x2Vaisseau:
    
                    if coordlaser[0] >= x1Vaisseau and ( 
                       coordlaser[2] <= x2Vaisseau and (
                       coordlaser[3] >= 550 )) :
                        
                        self.canva.delete(laserIndice)
                        self.listeLaser.pop(i - w)
                        w = w + 1
        
                        vaisseau2.destructionDuVaisseau()
            i+=1


    def move (self, dx, allee):

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
            if self.canva.coords(self.alien)[1]>400:
                a = vaisseau2.destructionDuVaisseau()
                return a

        self.canva.after(100, lambda : self.move(dx, allee) )