from tkinter import *
import tkinter as tk
from random import *
from time import time
nbrAlienLigne=4
#création de la fenetre
maFenetre= Tk()
#personalisation fenetre
maFenetre.title('Space invaders')
maFenetre.geometry('800x600+300+100')
maFenetre.config(background='ivory')
labelHello = Label(maFenetre, text="Space Invaders", fg='blue')


#canvas
w,h=500,500
Canvas = Canvas(maFenetre, width=w, height=h, bg='black')
Canvas.pack()
Canvas.place(x=00,y=00)


class vaisseau(tk.Tk):
    def __init__(self):

        self.w=500
        self.x=w//2
        self.y=400
        self.liste=[1,2,3,4]

        self.vaisseaux=Canvas.create_rectangle(self.x, self.y, self.x+40, self.y+40, fill="red")
        self.lmissile=[]
        self.dynmissile(self.liste)
        Canvas.bind_all("<Key>", self.bouger)
        Canvas.bind_all("w", self.missiles)
    def destructionDuVaisseau(self):
        Canvas.delete(self.vaisseaux)
        return 'perdu'
    def CoordsX(self):
        return Canvas.coords(self.vaisseaux)[0]
    def CoordsX2(self):
        return Canvas.coords(self.vaisseaux)[2]
    def bouger(self, event):
        x,y=0,0
        if event.char=='q':
           x=-10
        if event.char=='d':
            x=10

        Canvas.move(self.vaisseaux,x,y)

    def missiles(self, event):
        xmissile=Canvas.coords(self.vaisseaux)[0]+(Canvas.coords(self.vaisseaux)[2]-Canvas.coords(self.vaisseaux)[0])/2
        ymissile = Canvas.coords(self.vaisseaux)[1]
        self.missile = Canvas.create_rectangle(xmissile, ymissile, xmissile + 10, ymissile - 20, fill="blue")
        self.lmissile=self.lmissile+[self.missile]


    def dynmissile(self,liste):

        for n in liste:
            if n==1:

                axAlien=alien1.donneCoordsX()
                axAlien1 =alien1.donneCoordsX2()
                ayAlien= alien1.donneCoordsY()
                ayAlien1=alien1.donneCoordsY2()

            elif n==2:
                bxAlien = alien2.donneCoordsX()

                bxAlien1 = alien2.donneCoordsX2()
                byAlien = alien2.donneCoordsY()
                byAlien1 = alien2.donneCoordsY2()

            elif n==3:
                cxAlien = alien3.donneCoordsX()
                cxAlien1 = alien3.donneCoordsX2()
                cyAlien = alien3.donneCoordsY()
                cyAlien1 = alien3.donneCoordsY2()


            elif n==4:
                dxAlien = alien4.donneCoordsX()
                dxAlien1 = alien4.donneCoordsX2()
                dyAlien = alien4.donneCoordsY()
                dyAlien1 = alien4.donneCoordsY2()


            elif n==5:
                exAlien = alien5.donneCoordsX()
                exAlien1 = alien5.donneCoordsX2()
                eyAlien = alien5.donneCoordsY()
                eyAlien1 = alien5.donneCoordsY2()


            elif n==6:
                fxAlien = alien6.donneCoordsX()
                fxAlien1 = alien6.donneCoordsX2()
                fyAlien = alien6.donneCoordsY()
                fyAlien1 = alien6.donneCoordsY2()




        w=0

        for i in range (0,len(self.lmissile)):
            Canvas.move(self.lmissile[i-w],0,-10)
            if Canvas.coords(self.lmissile[i-w])[1]<=80:
                Canvas.delete(self.lmissile[i - w])
                self.lmissile.pop(i - w)
                w = w + 1
            if self.lmissile != []:


                for k in liste:

                    if k == 1:

                        if Canvas.coords(self.lmissile[i - w])[0] >= axAlien and Canvas.coords(self.lmissile[i - w])[
                            2] <= axAlien1 and ((Canvas.coords(self.lmissile[i - w])[1] >= ayAlien and
                                                 Canvas.coords(self.lmissile[i - w])[1] <= ayAlien1) or (
                                                        Canvas.coords(self.lmissile[i - w])[3] >= ayAlien and
                                                        Canvas.coords(self.lmissile[i - w])[3] <= ayAlien1)):
                            liste.remove(1)
                            Canvas.delete(self.lmissile[i - w])
                            self.lmissile.pop(i - w)
                            w = w + 1
                            a = alien1.destroyAlien()

                            break

                    if k == 2:
                        if Canvas.coords(self.lmissile[i - w])[0] >= bxAlien and Canvas.coords(self.lmissile[i - w])[
                            2] <= bxAlien1 and ((Canvas.coords(self.lmissile[i - w])[1] >= byAlien and
                                                 Canvas.coords(self.lmissile[i - w])[1] <= byAlien1) or (
                                                        Canvas.coords(self.lmissile[i - w])[3] >= byAlien and
                                                        Canvas.coords(self.lmissile[i - w])[3] <= byAlien1)):
                            Canvas.delete(self.lmissile[i - w])
                            self.lmissile.pop(i - w)
                            liste.remove(2)
                            w = w + 1
                            a = alien2.destroyAlien()
                            print(a)

                            break

                    if k == 3:
                        if Canvas.coords(self.lmissile[i - w])[0] >= cxAlien and Canvas.coords(self.lmissile[i - w])[
                            2] <= cxAlien1 and ((Canvas.coords(self.lmissile[i - w])[1] >= cyAlien and
                                                 Canvas.coords(self.lmissile[i - w])[1] <= cyAlien1) or (
                                                        Canvas.coords(self.lmissile[i - w])[3] >= cyAlien and
                                                        Canvas.coords(self.lmissile[i - w])[3] <= cyAlien1)):
                            Canvas.delete(self.lmissile[i - w])
                            self.lmissile.pop(i - w)
                            liste.remove(3)
                            w = w + 1
                            a = alien3.destroyAlien()
                            print(a)

                    if k == 4:
                        if Canvas.coords(self.lmissile[i - w])[0] >= dxAlien and Canvas.coords(self.lmissile[i - w])[
                            2] <= dxAlien1 and ((Canvas.coords(self.lmissile[i - w])[1] >= dyAlien and
                                                 Canvas.coords(self.lmissile[i - w])[1] <= dyAlien1) or (
                                                        Canvas.coords(self.lmissile[i - w])[3] >= dyAlien and
                                                        Canvas.coords(self.lmissile[i - w])[3] <= dyAlien1)):
                            Canvas.delete(self.lmissile[i - w])
                            self.lmissile.pop(i - w)
                            liste.remove(4)
                            w = w + 1
                            a = alien4.destroyAlien()
                            print(a)
                    if k == 5:
                        if Canvas.coords(self.lmissile[i - w])[0] >= exAlien and Canvas.coords(self.lmissile[i - w])[
                            2] <= dxAlien1 and ((Canvas.coords(self.lmissile[i - w])[1] >= dyAlien and
                                                 Canvas.coords(self.lmissile[i - w])[1] <= dyAlien1) or (
                                                        Canvas.coords(self.lmissile[i - w])[3] >= dyAlien and
                                                        Canvas.coords(self.lmissile[i - w])[3] <= dyAlien1)):
                            Canvas.delete(self.lmissile[i - w])
                            self.lmissile.pop(i - w)
                            liste.remove(5)
                            w = w + 1
                            a = alien5.destroyAlien()
                            print(a)

                    if k == 6:
                        if Canvas.coords(self.lmissile[i - w])[0] >= fxAlien and Canvas.coords(self.lmissile[i - w])[
                            2] <= fxAlien1 and ((Canvas.coords(self.lmissile[i - w])[1] >= fyAlien and
                                                 Canvas.coords(self.lmissile[i - w])[1] <= fyAlien1) or (
                                                        Canvas.coords(self.lmissile[i - w])[3] >= fyAlien and
                                                        Canvas.coords(self.lmissile[i - w])[3] <= fyAlien1)):
                            Canvas.delete(self.lmissile[i - w])
                            self.lmissile.pop(i - w)
                            liste.remove(6)
                            w = w + 1
                            a = alien6.destroyAlien()
                            print(a)

        Canvas.after(50,self.dynmissile,liste)




class Alien(tk.Tk):
    def __init__(self,n):



        self.n = n
        self.x= 100+self.n*100


        self.y = 200
        self.dx = 10
        self.allee=0

        self.alien = Canvas.create_rectangle(self.x, self.y, self.x + 20, self.y + 20, fill="white")
        self.move(self.dx, self.allee)
        self.lLaser=[]
        #self.laser()


       # self.tir()
    def donneCoordsX(self):
        return Canvas.coords(self.alien)[0]
    def donneCoordsX2(self):
        return Canvas.coords(self.alien)[2]
    def donneCoordsY(self):
        return Canvas.coords(self.alien)[1]
    def donneCoordsY2(self):
        return Canvas.coords(self.alien)[3]
    def destroyAlien(self):
        Canvas.delete(self.alien)
        return 'gagné'
    def laser(self):
        nbrAlea=randint(0, 100)
        if nbrAlea>80:

            xlaser = Canvas.coords(self.alien)[0] + (
                    Canvas.coords(self.alien)[2] - Canvas.coords(self.alien)[0]) / 2
            ylaser = Canvas.coords(self.alien)[1]
            self.rayonLaser = Canvas.create_rectangle(xlaser, ylaser, xlaser + 10, ylaser - 20, fill="green")
            self.lLaser = self.lLaser + [self.rayonLaser]
        Canvas.after(500, self.laser)

    """
         def tir(self):
            x1Vaisseau = leVaisseau.CoordsX()
            x2Vaisseau = leVaisseau.CoordsX2()

            w = 0

            for i in range(0, len(self.lLaser)):
                Canvas.move(self.lLaser[i - w], 0, 10)
                if Canvas.coords(self.lLaser[i - w])[1] >= 400:
                    Canvas.delete(self.lLaser[i - w])
                    self.lLaser.pop(i - w)
                    w = w + 1
                if self.lmissile != []:
                    if Canvas.coords(self.lLaser[i - w])[0] >= x1Vaisseau and Canvas.coords(self.lLaser[i - w])[2] <= x2Vaisseau and ((Canvas.coords(self.laser[i - w])[1] >= 300)):
                        Canvas.delete(self.lLaser[i - w])
                        self.lLaser.pop(i - w)
                        w = w + 1
                        a = leVaisseau.destroyvaisseau()

                Canvas.after(50, self.tir)
           """
    def move (self, dx, allee):

        if Canvas.coords(self.alien)==[]:
            return "gagné"
        Canvas.move(self.alien, dx, 0)
        if Canvas.coords(self.alien)[2]>400:
            dx=-10
            allee=allee+1
        if Canvas.coords(self.alien)[0]<100:
            dx=10
            allee=allee+1

        if allee==2:
            allee=0
            Canvas.move(self.alien, 0, 30)
            if Canvas.coords(self.alien)[1]>400:
                a =leVaisseau.destructionDuVaisseau()
                return a




        Canvas.after(100, self.move, dx, allee)

#alien1=Alien(0)
#alien2=Alien(1)
#alien3=Alien(2)
listeAlien=[]
ldd=[]


for i in range (1,nbrAlienLigne+1):
    valien="alien" + str(i)+ "=Alien("+str(i-1)+")"
    listeAlien=listeAlien+[valien]


for i in range(0,len(listeAlien)):
    ldd=ldd+[exec(listeAlien[i])]

leVaisseau=vaisseau()




#boutton quiter

buttonQuit = Button(maFenetre, text="quitter", fg='red', command=maFenetre.destroy)
buttonQuit.pack()
buttonQuit.place(x=700,y=00)
#afficher la fenetre
maFenetre.mainloop()

