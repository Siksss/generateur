import math
import turtle
import io
import os
import uuid
from PIL import Image

def generateur(nbr_cote, nbr_rep, taille, angle, couleur, reduction=0.9):
    turtle.TurtleScreen._RUNNING = True
    screen = turtle.Screen()
    screen.setup(width=500, height=500)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pencolor(couleur)
    for i in range(nbr_rep):  #pour chaque rep la taille diminue et l'angle est modifie
        current_taille = taille * (reduction ** i)
        current_angle = angle * i
        #generation des coordonnees des sommets du polygone
        coords = []
        for j in range(nbr_cote + 1):
            theta = 2 * math.pi * j / nbr_cote + math.radians(current_angle)
            x = current_taille * math.cos(theta)
            y = current_taille * math.sin(theta)
            coords.append((x, y))
        #on trace
        t.penup()
        t.goto(coords[0])
        t.pendown()
        for (x, y) in coords[1:]:
            t.goto(x, y)
    #on sauvegarde en PostScript
    filename = f"temp_{uuid.uuid4().hex}.ps"
    canvas = screen.getcanvas()
    canvas.postscript(file=filename, colormode='color')
    turtle.bye()
    #conversion du PostScript en PNG
    with Image.open(filename) as image:
        output = io.BytesIO()
        image.save(output, format="PNG")
        output.seek(0)
    os.remove(filename)
    return output

#meme chose que generateur mais sans plusieurs repetitions
def generateurFS(nbr_cote, taille, angle, couleur, reduction=0.9):
    turtle.TurtleScreen._RUNNING = True
    screen = turtle.Screen()
    screen.setup(width=500, height=500)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pencolor(couleur)
    coords = []
    for j in range(nbr_cote + 1):
        theta = 2 * math.pi * j / nbr_cote + math.radians(angle)
        x = taille * math.cos(theta)
        y = taille * math.sin(theta)
        coords.append((x, y))
    t.penup()
    t.goto(coords[0])
    t.pendown()
    for (x, y) in coords[1:]:
        t.goto(x, y)
    filename = f"temp_{uuid.uuid4().hex}.ps"
    canvas = screen.getcanvas()
    canvas.postscript(file=filename, colormode='color')
    turtle.bye()
    with Image.open(filename) as image:
        output = io.BytesIO()
        image.save(output, format="PNG")
        output.seek(0)
    os.remove(filename)
    return output



