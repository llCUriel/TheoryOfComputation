from Tkinter import *
import math
import random


def crearPasto(w,x,y,l,a,sl,da,n):
    if n==0:
        return
    color='green'
    x2=x+l
    y2=y
    ar=math.radians(a)
    coseno=math.cos(ar)
    seno=math.sin(ar)
    xrot= (x2-x)*seno + (y2-y)*coseno
    yrot= (x2-x)*coseno - (y2-y)*seno
    x2=xrot + x
    y2=yrot + y
    w.create_line(x,y,x2,y2,fill=color)
    crearPasto(w,x2,y,l*sl,a-da,sl,da,n-1)
    crearPasto(w,x2,y2,l*sl,a+da,sl,da,n-1)
    crearPasto(w,x2,y,l*sl,a,sl,da,n-1)
    return


def crearNube(w,x,y,l,a,sl,da,n):
    if n==0:
        return
    color='black'
    x2=x+l
    y2=y
    ar=math.radians(a)
    coseno=math.cos(ar)
    seno=math.sin(ar)
    xrot= (x2-x)*seno + (y2-y)*coseno
    yrot= (x2-x)*coseno - (y2-y)*seno
    x2=xrot + x
    y2=yrot + y
    w.create_line(x,y,x2,y2,fill=color)
    w.create_oval((x-l/2),(y-l/2),(x+l/2),(y+l/2),fill='white') 
    crearNube(w,x2,y2,l*sl,a-da,sl,da,n-1)
    crearNube(w,x2,y2,l*sl,a-2*da,sl,da,n-1)
    crearNube(w,x2,y2,l*sl,a-3*da,sl,da,n-1)
    return

def crearGota(w,x,y,l,a,sl,da,n):
    if n==0:
        return

    color='blue'

    if n>5:
        color='blue'
    elif n>2:
        color='blue'
    elif n>0:
        color='blue'

    x2=x+l
    y2=y
    ar=math.radians(a)

    coseno=math.cos(ar)
    seno=math.sin(ar)
    xrot= (x2-x)*seno + (y2-y)*coseno
    yrot= (x2-x)*coseno - (y2-y)*seno
    x2=xrot + x
    y2=yrot + y
    w.create_line(x,y,x2,y2,fill=color)
    crearGota(w,x2,y2,l*sl,a-da,sl,da,n-1)
    return


def crearArbol(w,x,y,l,a,sl,da,n):
    if n==0:
        return
    color='black'
    if n>5:
        color='brown'
    elif n>2:
        color='magenta'
    elif n>0:
        color='magenta'
    x2=x+l
    y2=y
    ar=math.radians(a)
    coseno=math.cos(ar)
    seno=math.sin(ar)
    xrot= (x2-x)*seno + (y2-y)*coseno
    yrot= (x2-x)*coseno - (y2-y)*seno
    x2=xrot + x
    y2=yrot + y
    w.create_line(x,y,x2,y2,fill=color)
    crearArbol(w,x2,y2,l*sl,a-da,sl,da,n-1)
    crearArbol(w,x2,y2,l*sl,a+da,sl,da,n-1)
    crearArbol(w,x2,y2,l*sl,a,sl,da,n-1)

    return


master = Tk()
xmax=1400
ymax=720
w = Canvas(master, width=xmax, height=ymax)
w.pack()

w.create_rectangle(0, 0, 1400, 800, fill='light green')
w.create_rectangle(0, 0, 1400, 200, fill='light sky blue')
for t in range(30):
        for n in range(25):
            crearGota(w,random.randint(0, 100)+-50+(t*100),150+(n*20),1,180,0.99,33,600)
for i in range(20):
        crearNube(w,-100+(i*110),-100,150,120,0.8,30,7)

for k in range(5):
        aux = random.randint(0, 50)
        crearArbol(w,100+aux+(340*k),460+aux,100,180,0.7,23,10)
        crearArbol(w,100+aux+(340*k),460+aux,100,180,0.6,23,10)
        crearArbol(w,100+aux+(340*k),460+aux,100,180,0.5,23,10)

        crearArbol(w,aux+(340*k),650+aux,100,180,0.7,23,10)
        crearArbol(w,aux+(340*k),650+aux,100,180,0.6,23,10)
        crearArbol(w,aux+(340*k),650+aux,100,180,0.5,23,10)


for m in range(30):
        crearPasto(w,150+(m*50),1000,150,180,0.7,20,8)
        
mainloop()
