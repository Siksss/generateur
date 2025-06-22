import math
import turtle
import io
import os
import uuid
from PIL import Image

def generateur_png(nbr_cote, nbr_rep, taille, angle, couleur, reduction=0.9):
    turtle.TurtleScreen._RUNNING = True
    screen = turtle.Screen()
    screen.setup(width=500, height=500)
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.pencolor(couleur)

    for i in range(nbr_rep):
        current_taille = taille * (reduction ** i)
        current_angle = angle * i

        coords = []
        for j in range(nbr_cote + 1):
            theta = 2 * math.pi * j / nbr_cote + math.radians(current_angle)
            x = current_taille * math.cos(theta)
            y = current_taille * math.sin(theta)
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

    # --- Ouverture sécurisée de l'image ---
    with Image.open(filename) as image:
        output = io.BytesIO()
        image.save(output, format="PNG")
        output.seek(0)

    # Le fichier est libéré à la sortie du with
    os.remove(filename)

    return output





# import turtle
# import math
# from svg_turtle import SvgTurtle


# def generateur(t,nbr_cote, nbr_rep, taille, angle, couleur, reduction=0.9):
#     """
#     Génère une spirale de polygones réguliers superposés, tournés et réduits avec turtle, puis enregistre en PNG.

#     Args:
#         nbr_cote (int): Nombre de côtés du polygone.
#         nbr_rep (int): Nombre de répétitions.
#         taille (float): Rayon du polygone.
#         angle (float): Angle de rotation entre répétitions.
#         couleur (str): Couleur du trait.
#         reduction (float): Facteur de réduction.
        

#     Returns:
#         None
#     """
#     screen = turtle.Screen()
#     screen.bgcolor("white")
#     t.speed(0)
#     t.hideturtle()
#     t.pencolor(couleur)

#     for i in range(nbr_rep):
#         current_taille = taille * (reduction ** i)
#         current_angle = angle * i

#         coords = []
#         for j in range(nbr_cote + 1):
#             theta = 2 * math.pi * j / nbr_cote + math.radians(current_angle)
#             x = current_taille * math.cos(theta)
#             y = current_taille * math.sin(theta)
#             coords.append((x, y))

#         t.penup()
#         t.goto(coords[0])
#         t.pendown()
#         for (x, y) in coords[1:]:
#             t.goto(x, y)
#     turtle.done()

# def write_file(draw_func, filename, width, height):
#     t = SvgTurtle(width, height)
#     draw_func(t,4, 9, 200, 128, 'red')
#     t.save_as(filename)

# def main():
#     write_file(generateur, 'C:/Users/matia/OneDrive/Bureau/generateur/generateur/server/.venv/formes_generes/test4.svg', 500, 500)
#     print('Done.')

# if __name__ == '__main__':
#     main()