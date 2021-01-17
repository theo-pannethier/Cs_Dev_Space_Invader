# -*- coding: utf-8 -*-
"""
Programme contenant la classe ilot et ainsi permettant la creationet la gestion
de la vie des ilots


ToDo:
    
    
Theo Pannethier / Jeffrey Simon
17/01/2021
"""
import tkinter as tk

class ilot(tk.Tk):
    """classe permettant l'apparition de bloc"""
    def __init__(self,canva):
        """initialisation de la classe avec notamment la creation visuelle des blocs"""
        self.canva=canva
        self.x=500
        self.y=400
        self.vie = [1,1,1]
        self.carréC = [0,self.canva.create_rectangle(self.x, self.y, self.x + 20, self.y + 20, fill="brown")]
        self.carréD = [1,self.canva.create_rectangle(self.x+20, self.y, self.x + 20+20, self.y + 20, fill="brown")]
        self.carréG = [2,self.canva.create_rectangle(self.x -20, self.y, self.x + 20 - 20, self.y + 20, fill="brown")]
        self.liste=[self.carréC,self.carréD,self.carréG]

    def toucheIlot(self,pIndice):
        """permet de reduire la vie d'un ilot si celui-ci est touché
        Entrée:
            -pIndice : indice de l'ilot touché"""
        if self.vie[pIndice] >= 2 :
            self.vie[pIndice] = self.vie[pIndice] - 1
        else:
            for carre in [self.carréC,self.carréD,self.carréG]:
                if carre[0] == pIndice :
                   self.canva.delete(carre[1])
                   self.liste.remove(carre)
                   
    def ilotCoord(self):
        """permet la recuperation à l'exterieur de la classe des coordonnées 
        des ilots encore en vie (present dans self.iste)"""
        coord=[]
        for carre in self.liste:
            coord.append([carre[0],self.canva.coords(carre[1])])
        return coord

