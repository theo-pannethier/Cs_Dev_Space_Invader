"""
Programme gerant la partie graphique.

ToDo:
    -faire le bouton qui relance la partie ~ 
    -alien special
    -vie vaisseau
    -score

Theo Pannethier / Jeffrey Simon
17/01/2021
"""
import tkinter as tk
from random import randint

score=10
score= str(score)
from  tkinter import Tk,Button,Frame,PhotoImage,Canvas,Label
import tkinter.font as tkFont



        
class vaisseau(tk.Tk):
    """classe gerant le vaisseau et sa dynamique"""
    def __init__(self,pListeAlien):
        """initialisation de toutes les variables utiles à vaisseau"""
        self.x = w//2
        self.y=550
        self.listeAlien=pListeAlien
        self.vivant=True
        self.listeIndice = []
        self.listeInterdite = []
        self.affichage=Label(menu , text='vie : ' + '3' , font=normal )  
        self.vie=3
        self.vaisseaux=canva.create_rectangle(self.x, self.y, self.x+40, self.y+40, fill="red")
        self.lmissile=[]
        self.listeIndiceAlien()
        self.status = True
        self.dynmissile(self.listeAlien,self.listeIndice,self.listeInterdite)
        canva.bind_all("<Left>", lambda direction='Left':self.bouger(direction))
        canva.bind_all("<Right>", lambda direction='Right':self.bouger(direction))
        canva.bind_all("<Key>", self.missiles)
        self.affichage.pack()
    def listeIndiceAlien(self):
        """Programme donnant la liste des  indices des aliens"""
        for i in range ( len(self.listeAlien) ):
            self.listeIndice.append(i+1)
        
    def destructionDuVaisseau(self):
        """"permet de faire disparaitre la vaisseau en cas defaite"""
        canva.delete(self.vaisseaux)
        self.vivant=False
        return 'perdu'
    
    def CoordsX(self):
        """donne la coordonnée x1 (c'est  a dire le x à gauche du vaisseau)"""
        if canva.coords(self.vaisseaux) :
            return canva.coords(self.vaisseaux)[0]
       
    def CoordsX2(self):
        """donne la coordonnée x2 (c'est  a dire le x à droite du vaisseau)"""
        if canva.coords(self.vaisseaux) :
            return canva.coords(self.vaisseaux)[2]
        
    def bouger(self, event):
        """permet d'enregistrer la demande de deplacement du vaisseau
        Entrée : event car permet de donner la touche appuyée"""
        x,y=0,0
        if event.keysym == 'Left':
           x=-10
        if event.keysym == 'Right':
            x=10

        canva.move(self.vaisseaux,x,y)



    def missiles(self, event):
        """permet de cree les missiles du vaisseau
        Entrée : event car permet de donner la touche appuyée"""
        
        if  self.vivant and  event.keysym == 'space':
    
            xmissile=canva.coords(self.vaisseaux)[0]+(canva.coords(self.vaisseaux)[2]-
                                            canva.coords(self.vaisseaux)[0])/2
            ymissile = canva.coords(self.vaisseaux)[1]
            self.missile = canva.create_rectangle(xmissile-5, ymissile, xmissile + 5, ymissile - 20, fill="blue")
            self.lmissile=self.lmissile+[self.missile]


    def dynmissile(self,liste,listeIndice,listeInterdite):
        """permet de faire bouger les missile du vaisseau
        Entrée :
            -liste : liste des aliens
            -listeIndice : Liste de la liste des aliens
            -listeInterdite: Liste des indices des aliens detruits"""
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
            canva.move(objetMissile,0,-10)
            if canva.coords(objetMissile)[1] <= 0:
                canva.delete(objetMissile)
                self.lmissile.pop(i - w)
                w = w + 1
            if self.lmissile != []:


                for k in range( len(listeIndice)):
                    objetMissile=self.lmissile[i - w]
                    coordMissile=canva.coords(objetMissile)
                    if coordMissile[0] >= Listecoord[k][0] and (
                       coordMissile[2] <= Listecoord[k][1] and (
                       coordMissile[1] >= Listecoord[k][2] and (
                       coordMissile[1] <= Listecoord[k][3]) or (
                       coordMissile[3] >= Listecoord[k][2] and (
                       coordMissile[3] <= Listecoord[k][3])))):
                        val=listeIndice[k]
                        val=listeIndice[k]


                        if val not in listeInterdite:
                            liste[k].destroyAlien()
                            liste.pop(k)
                            listeIndice.remove(val)

                            canva.delete(self.lmissile[i - w])
                            self.lmissile.pop(i - w)
                            w = w + 1


                            listeInterdite.append(val)
                            annule = True
                            break
                if annule == True:
                    break


        canva.after(50,self.dynmissile,liste,listeIndice,listeInterdite)

    def getVie(self):
        """permet de recuperer le nombre de point de vie"""
        return self.vie

    def vivre(self):
        """permet de tuer le vaisseau si self.vie < 1 """

        if self.vie <= 1:
            self.vie =self.vie - 1
            self.destructionDuVaisseau()
            canva.after(100,self.fin)
        else :
            self.vie =self.vie - 1

        self.affichage.destroy()
        self.affichage=Label(menu , text='vie : ' + str(self.vie) , font=normal ) 
        self.affichage.pack()

    def fin(self):
        canva.destroy()
    
    
    
class Alien(tk.Tk):
    """classe permettant la gestion des aliens
    (chaque alien est independant et representeun appel à Alien)"""
    
    def __init__(self,n):
        """initialisation de la classe alien
        Entrée:
            -n : indice de l'alien crée"""
        self.n = n
        self.x = 100+self.n*100
        self.y = 30
        self.dx = 10
        self.allee = 0
        self.alien = canva.create_rectangle(self.x, self.y, self.x + 20, self.y + 20, fill="white")
        self.move(self.dx, self.allee)




    """les methodes suivantes permettent de recuperer les coordonnées de chaque
    alien à l'exterieur de la classe """
    def donneCoordsX(self):
        return canva.coords(self.alien)[0]
    def donneCoordsX2(self):
        return canva.coords(self.alien)[2]
    def donneCoordsY(self):
        return canva.coords(self.alien)[1]
    def donneCoordsY2(self):
        return canva.coords(self.alien)[3]
    
    
    
    
    def destroyAlien(self):
        """programme qui appelé, permet de supprimer l'alien"""
        canva.delete(self.alien)
        return 'gagné'
    


    def move (self, dx, allee):
        """programme gerant le deplacement horizontale et verticale de l'alien
        Entrée:
            -dx : permet de donner la vitesse à l'alien, ici soit 10 soit -10 
                  en fonction de la direction de deplacement.
            -allee : permet de compter le nombre d'aller effectué"""
        if canva.coords(self.alien) == []:
            return "gagné"
        canva.move(self.alien, dx, 0)
        if canva.coords(self.alien)[2] > 1050:
            dx=-10
            allee=allee+1

        if canva.coords(self.alien)[0] < 50:
            dx=10
            allee=allee+1

        if allee == 2 :
            allee = 0
            
            canva.move(self.alien, 0, 30)
            if canva.coords(self.alien)[1] > 400 :
                leVaisseau.destructionDuVaisseau()
                

        canva.after(100, lambda : self.move(dx, allee) )

class tirer(tk.Tk):
    """"classe permettant le tire des aliens
        A l'origine, cette classe etait une methode de alien, mais pour une separation en fichier, 
        sa creation s'imposait"""
        
        
    def __init__(self,pListe,leVaisseau,ilot) :
        """initialisation de la classe tirer
        Entrée:
            -pListe: liste des aliens"""
        self.ListeAlien=pListe
        self.listeLaser = []
        self.laser()
        self.leVaisseau=leVaisseau
        self.ilot=ilot
    def laser(self):
            """methode permettant la géneration des lasers """
            i=0
            while i < len(self.ListeAlien):

                Alien = self.ListeAlien[i]
                
                nbrAlea=randint(0, 100)
                if nbrAlea > 90 and Alien:
                    xlaser = Alien.donneCoordsX() + (Alien.donneCoordsX2() - Alien.donneCoordsX()) / 2
                    ylaser = Alien.donneCoordsY()
                    self.rayonLaser = canva.create_rectangle(xlaser, ylaser+20, xlaser + 10, ylaser + 40, fill="green")
                    self.listeLaser = self.listeLaser + [self.rayonLaser]
                i+=1
            canva.after(0, self.tir)
            canva.after(100, self.laser)
        


    def tir(self):
        """methode permettant le deplacement des missiles des aliens, ainsi que 
        leur gestion dynamique (colision avec le vaisseau,les blocs,sortie du canva)"""

        x1Vaisseau = self.leVaisseau.CoordsX()
        x2Vaisseau = self.leVaisseau.CoordsX2()
        coordIlot=self.ilot.ilotCoord()
        
        w = 0
        i=0
        while i < len(self.listeLaser):
            laserIndice=self.listeLaser[i - w]
            coordlaser=canva.coords(laserIndice)
            canva.move(self.listeLaser[i], 0, 10)

            if coordlaser[1] >= 600:
                canva.delete(laserIndice)
                self.listeLaser.pop(i - w)
                w = w + 1
                
            if self.listeLaser != []:
                k=0
                while  k < len(coordIlot):
                    if coordlaser[0] >= coordIlot[k][1][0] and ( 
                       coordlaser[2] <= coordIlot[k][1][2] and (
                       coordlaser[3] >= coordIlot[k][1][1] )):
                        
                        canva.delete(laserIndice)
                        self.listeLaser.pop(i - w)
                        self.ilot.toucheIlot( coordIlot[k][0])
                        w = w + 1
                        coordIlot=self.ilot.ilotCoord()

                    k+=1
                if x1Vaisseau and x2Vaisseau:
    
                    if coordlaser[0] >= x1Vaisseau and ( 
                       coordlaser[2] <= x2Vaisseau and (
                       coordlaser[3] >= 550 )) :
                        
                        canva.delete(laserIndice)
                        self.listeLaser.pop(i - w)
                        w = w + 1
                        self.leVaisseau.vivre()
                        
            i+=1






class ilot(tk.Tk):
    """classe permettant l'apparition de bloc"""
    def __init__(self):
        """initialisation de la classe avec notamment la creation visuelle des blocs"""
        self.x=500
        self.y=400
        self.vie = [2,2,2]
        self.carréC = [0,canva.create_rectangle(self.x, self.y, self.x + 20, self.y + 20, fill="brown")]
        self.carréD = [1,canva.create_rectangle(self.x+20, self.y, self.x + 20+20, self.y + 20, fill="brown")]
        self.carréG = [2,canva.create_rectangle(self.x -20, self.y, self.x + 20 - 20, self.y + 20, fill="brown")]
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
                   canva.delete(carre[1])
                   self.liste.remove(carre)
                   
    def ilotCoord(self):
        """permet la recuperation à l'exterieur de la classe des coordonnées 
        des ilots encore en vie (present dans self.iste)"""
        coord=[]
        for carre in self.liste:
            coord.append([carre[0],canva.coords(carre[1])])
        return coord





 
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
score = Label(menu , text='score : ' + score , font=normal )

NewGameBouton.pack(padx=0,pady=0)
QuitBouton.pack(padx=0,pady=100)
score.pack()
w=1100
height=600


        

listeAlien = []
nbrAlienLigne = 8       

      
for i in range(nbrAlienLigne):
    listeAlien.append(Alien(i))

leVaisseau = vaisseau(listeAlien)
ilot1=ilot()
tire2=tirer(listeAlien,leVaisseau,ilot1)







#afficher la fenetre
Fenetre.mainloop()

