# Petit exercice utilisant la bibliothèque graphique Tkinter
from tkinter import *
from random import randrange

# --- définition des fonctions gestionnaires d'événements : ---
def drawline():
    "Tracé d'une ligne dans le canevas can1"
    global x1, y1, x2, y2, coul
    can1.create_line(x1,y1,x2,y2,width=2,fill=coul)
    # modification des coordonnées pour la ligne suivante :
    y2, y1 = y2+10, y1+10


def changecolor():
    "Changement aléatoire de la couleur du tracé"
    global coul
    pal=['purple','cyan','maroon','green','red','blue','orange','yellow']
    c = randrange(8) #
    coul = pal[c]

def drawline2() :
    global j,k,l,m
    can1.create_line(j,k,l,m,width=2,fill=coul)
    j,k,l,m = l,k,j,m
    can1.create_line(j,k,l,m,width=2,fill=coul)
    # modification des coordonnées pour la ligne suivante :
    j,k,l,m=j+10,k+10, l-10, m-10


#------ Programme principal -------
# les variables suivantes seront utilisées de manière globale :
x1, y1, x2, y2 = 0, 10, 600, 10 # coordonnées de la ligne
j,k,l,m = 0,0,600,600
coul = 'dark green' # couleur de la ligne
# Création du widget principal ("maître") :
fen1 = Tk()
# création des widgets "esclaves" :
can1 = Canvas(fen1,bg='dark grey',height=600,width=600)
can1.pack(side=LEFT)
bou1 = Button(fen1,text='Quitter',command=fen1.quit)
bou1.pack(side=BOTTOM)
bou2 = Button(fen1,text='Tracer une ligne',command=drawline)
bou2.pack()
bou3 = Button(fen1,text='Autre couleur',command=changecolor)
bou3.pack()
bou4 = Button(fen1,text='Tracer deux ligne au centre',command=drawline2)
bou4.pack()
fen1.mainloop() # démarrage du réceptionnaire d’événements
fen1.destroy() # destruction (fermeture) de la fenêtre


