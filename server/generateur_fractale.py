import turtle
import math
import io
import os
import uuid
from PIL import Image

def koch(t, taille, nbr_rep):
    if nbr_rep == 0: # plus de recursion, on trace un segment
        t.forward(taille)
    else: # appel recursif pour creer la fractale
        taille /= 3.0
        koch(t, taille, nbr_rep - 1)
        t.left(60)
        koch(t, taille, nbr_rep - 1)
        t.right(120)
        koch(t, taille, nbr_rep - 1)
        t.left(60)
        koch(t, taille, nbr_rep - 1)

def generateur_fractale_koch(taille, nbr_rep, couleur):
    turtle.TurtleScreen._RUNNING = True
    screen = turtle.Screen() # nouvelle fenetre
    screen.setup(width=600, height=600)
    screen.tracer(0, 0) # desactive l'animation 
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pencolor(couleur)
    hauteur_triangle = taille * math.sqrt(3) / 2
    #centrage
    x = -taille / 2
    y = -hauteur_triangle / 3  
    t.penup()
    t.goto(x, y)
    t.pendown()
    #boucle pour dessiner la fractale
    for i in range(3):
        koch(t, taille, nbr_rep)
        t.right(120)
    screen.update()
    #genere un nom de fichier unique
    filename = f"temp_{uuid.uuid4().hex}.ps"
    canvas = screen.getcanvas()
    canvas.postscript(file=filename, colormode='color') #sauvegarde en PostScript
    turtle.bye() 
    #convertit PostScript en PNG
    with Image.open(filename) as image:
        output = io.BytesIO()
        image.save(output, format="PNG")
        output.seek(0)
    os.remove(filename) #supprime le fichier .ps
    return output
