# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 15:40:37 2021

@author: Theo Pannethier
"""

import tkinter as tk

class ilot(tk.Tk):
    def __init__(self,canva):
        self.canva=canva
        self.x=500
        self.y=400
        self.vie = [1,1,1]
        self.carréC = [0,self.canva.create_rectangle(self.x, self.y, self.x + 20, self.y + 20, fill="brown")]
        self.carréD = [1,self.canva.create_rectangle(self.x+20, self.y, self.x + 20+20, self.y + 20, fill="brown")]
        self.carréG = [2,self.canva.create_rectangle(self.x -20, self.y, self.x + 20 - 20, self.y + 20, fill="brown")]
        self.liste=[self.carréC,self.carréD,self.carréG]

    def toucheIlot(self,pIndice):
        if self.vie[pIndice] >= 2 :
            self.vie[pIndice] = self.vie[pIndice] - 1
        else:
            for carre in [self.carréC,self.carréD,self.carréG]:
                if carre[0] == pIndice :
                   self.canva.delete(carre[1])
                   self.liste.remove(carre)
                   
    def ilotCoord(self):
        coord=[]
        for carre in self.liste:
            coord.append([carre[0],self.canva.coords(carre[1])])
        return coord

