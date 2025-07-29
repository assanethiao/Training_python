"""
Une horloge analogique fonctionnelle avec Turtle, qui affiche :

- Un cadran circulaire 

- Les chiffres de 1 à 12

- Les aiguilles des heures, minutes, secondes

- Et qui se met à jour en temps réel

"""
import math
import turtle
import time 
from datetime import datetime

# la fenetre principale
screen = turtle.Screen()
screen.title("Horloge Analogique")
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)  

# le cadran
def draw_clock_face():
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(3)
    pen.penup()
    pen.goto(0, -250)
    pen.pendown()
    pen.circle(250)

    # Positionner les chiffres
    pen.penup()
    for hour in range(1, 13):
        angle = (hour / 12) * 360
        x = 200 * math.sin(math.radians(angle))
        y = 200 * math.cos(math.radians(angle))

        pen.goto(x - 10, y - 10)
        pen.write(str(hour), align="center", font=("Arial", 14, "normal"))
        

# defintion des aiguilles
def create_hand(length, color, width):
    hand = turtle.Turtle()
    hand.shape("arrow")
    hand.color(color)
    hand.shapesize(stretch_wid=0.3, stretch_len=length)
    hand.pensize(width)
    hand.speed(0)
    return hand


# Mettre à jour les aiguilles
def update_hands():
    now = datetime.now()
    second = now.second
    minute = now.minute
    hour = now.hour % 12

    second_angle = second * 6
    minute_angle = (minute + second / 60) * 6
    hour_angle = (hour + minute / 60) * 30

    second_hand.setheading(90 - second_angle)
    minute_hand.setheading(90 - minute_angle)
    hour_hand.setheading(90 - hour_angle)

    screen.update()
    screen.ontimer(update_hands, 1000)


# Créer les aiguilles
second_hand = create_hand(15, "red", 27)
minute_hand = create_hand(17, "blue", 28)
hour_hand = create_hand(19, "black", 30)

draw_clock_face()
update_hands()

screen.mainloop()

