"""
Programme gerant la partie graphique.

ToDo:
    -faire le bouton qui relance la partie ~ 
    -alien special
    -vie
    -score
    -modifie trajectoire de l'alien'
    -inserer image alien et vaisseau
Theo Pannethier / Jeffrey Simon
14/01/2021
"""
import tkinter as tk
from random import randint

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


        
class vaisseau(tk.Tk):
    def __init__(self,pListeAlien):
        self.imageVaisseau = PhotoImage(file = "vaisseau.png")  #création image de fond du vaisseau
        self.x=w//2
        self.y=550
        self.listeAlien=pListeAlien
        self.vivant=True
        self.listeIndice=[]
        self.listeInterdite=[]
        self.vaisseaux=canva.create_rectangle(self.x, self.y, self.x+40, self.y+40, fill="red")
        self.lmissile=[]
        self.listeIndiceAlien()
        self.dynmissile(self.listeAlien,self.listeIndice,self.listeInterdite)
        canva.bind_all("<Left>", lambda direction='Left':self.bouger(direction))
        canva.bind_all("<Right>", lambda direction='Right':self.bouger(direction))
        canva.bind_all("<Key>", self.missiles)
        
    def listeIndiceAlien(self):
        for i in range ( len(self.listeAlien) ):
            self.listeIndice.append(i+1)
        
    def destructionDuVaisseau(self):
        canva.delete(self.vaisseaux)
        self.vivant=False
        return 'perdu'
    def CoordsX(self):
        if canva.coords(self.vaisseaux) :
            return canva.coords(self.vaisseaux)[0]
       
    def CoordsX2(self):
        if canva.coords(self.vaisseaux) :
            return canva.coords(self.vaisseaux)[2]
        
    def bouger(self, event):
        x,y=0,0
        if event.keysym == 'Left':
           x=-10
        if event.keysym == 'Right':
            x=10

        canva.move(self.vaisseaux,x,y)



    def missiles(self, event):
        
        if  self.vivant and  event.keysym=='space':
    
            xmissile=canva.coords(self.vaisseaux)[0]+(canva.coords(self.vaisseaux)[2]-
                                            canva.coords(self.vaisseaux)[0])/2
            ymissile = canva.coords(self.vaisseaux)[1]
            self.missile = canva.create_rectangle(xmissile-5, ymissile, xmissile + 5, ymissile - 20, fill="blue")
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
            canva.move(objetMissile,0,-10)
            if canva.coords(objetMissile)[1]<=0:
                canva.delete(objetMissile)
                self.lmissile.pop(i - w)
                w = w + 1
            if self.lmissile != []:


                for k in range( len(listeIndice)):
                    objetMissile=self.lmissile[i - w]
                    if canva.coords(objetMissile)[0] >= Listecoord[k][0] and canva.coords(objetMissile)[
                        2] <= Listecoord[k][1] and ((canva.coords(objetMissile)[1] >= Listecoord[k][2] and
                                             canva.coords(objetMissile)[1] <= Listecoord[k][3]) or (
                                                    canva.coords(objetMissile)[3] >= Listecoord[k][2] and
                                                    canva.coords(objetMissile)[3] <= Listecoord[k][3])):
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




class Alien(tk.Tk):
    def __init__(self,n):

        self.n = n
        self.x = 100+self.n*100
        self.y = 30
        self.dx = 10
        self.allee = 0
        self.alien = canva.create_rectangle(self.x, self.y, self.x + 20, self.y + 20, fill="white")
        self.move(self.dx, self.allee)





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
    


    def move (self, dx, allee):

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
            if canva.coords(self.alien)[1]>400:
                a = leVaisseau.destructionDuVaisseau()
                return a

        canva.after(100, lambda : self.move(dx, allee) )

class tirer(tk.Tk):
    def __init__(self,pListe) :
        self.ListeAlien=pListe
        self.listeLaser = []
        self.laser()
        self.permissionDeTirer()
        
        
    def laser(self):
            i=0
            while i<len(self.ListeAlien):

                Alien = self.ListeAlien[i]
                
                nbrAlea=randint(0, 100)
                if nbrAlea>90 and Alien:
                    xlaser = Alien.donneCoordsX() + (Alien.donneCoordsX2() - Alien.donneCoordsX()) / 2
                    ylaser = Alien.donneCoordsY()
                    self.rayonLaser = canva.create_rectangle(xlaser, ylaser+20, xlaser + 10, ylaser + 40, fill="green")
                    self.listeLaser = self.listeLaser + [self.rayonLaser]
                i+=1
            canva.after(0, self.tir)
            canva.after(100, self.laser)
        
    def permissionDeTirer(self):
        canva.after(1000, self.tir)


    def tir(self):


        x1Vaisseau = leVaisseau.CoordsX()
        x2Vaisseau = leVaisseau.CoordsX2()
        coordIlot=ilot1.ilotCoord()
        
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
                while  k<len(coordIlot):
                    if coordlaser[0] >= coordIlot[k][1][0] and ( 
                       coordlaser[2] <= coordIlot[k][1][2] and (
                       coordlaser[3] >= coordIlot[k][1][1] )):
                        
                        canva.delete(laserIndice)
                        self.listeLaser.pop(i - w)
                        ilot1.toucheIlot( coordIlot[k][0])
                        w = w + 1
                        coordIlot=ilot1.ilotCoord()

                    k+=1
                if x1Vaisseau and x2Vaisseau:
    
                    if coordlaser[0] >= x1Vaisseau and ( 
                       coordlaser[2] <= x2Vaisseau and (
                       coordlaser[3] >= 550 )) :
                        
                        canva.delete(laserIndice)
                        self.listeLaser.pop(i - w)
                        w = w + 1
        
                        leVaisseau.destructionDuVaisseau()
            i+=1






class ilot(tk.Tk):
    def __init__(self):
        self.x=500
        self.y=400
        self.vie = [1,1,1]
        self.carréC = [0,canva.create_rectangle(self.x, self.y, self.x + 20, self.y + 20, fill="brown")]
        self.carréD = [1,canva.create_rectangle(self.x+20, self.y, self.x + 20+20, self.y + 20, fill="brown")]
        self.carréG = [2,canva.create_rectangle(self.x -20, self.y, self.x + 20 - 20, self.y + 20, fill="brown")]
        self.liste=[self.carréC,self.carréD,self.carréG]

    def toucheIlot(self,pIndice):
        if self.vie[pIndice] >= 2 :
            self.vie[pIndice] = self.vie[pIndice] - 1
        else:
            for carre in [self.carréC,self.carréD,self.carréG]:
                if carre[0] == pIndice :
                   canva.delete(carre[1])
                   self.liste.remove(carre)
                   
    def ilotCoord(self):
        coord=[]
        for carre in self.liste:
            coord.append([carre[0],canva.coords(carre[1])])
        return coord


        
listeAlien = []
nbrAlienLigne = 8       

      
for i in range(nbrAlienLigne):
    listeAlien.append(Alien(i))

leVaisseau = vaisseau(listeAlien)
ilot1=ilot()
tire2=tirer(listeAlien)
print(listeAlien[0].donneCoordsX())


#afficher la fenetre
Fenetre.mainloop()

