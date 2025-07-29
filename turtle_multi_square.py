from turtle import *
def carre(taille, couleur):
    i, j=0,0
    x, y=2,2
    while j<10:
        down()
        while i<4:
            color(couleur)
            forward(taille)
            right(90)
            i+=1
        i=0
        taille+=10
        j+=1
        up()
        forward(taille+10)
        
        


def main():
    up()
    goto(-250, 10)
    carre(10,'red')
    

if __name__ == "__main__":
    main()
