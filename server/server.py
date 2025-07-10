from flask import Flask, request, send_file
from flask_cors import CORS #permet les requetes depuis le frontend
from generateur import generateur
from generateur import generateurFS
from generateur_fractale import generateur_fractale_koch

app = Flask(__name__) #Creation de l'application Flask
CORS(app)#permet les requetes depuis le frontend

@app.route("/generer", methods=["POST"])
def generer():
    data = request.get_json() #on recupere les donnees envoyees par le frontend en JSON
    image_io = generateur(
        int(data["nbr_cote"]),
        int(data["nbr_rep"]),
        int(data["taille"]),
        int(data["angle"]),
        data["couleur"]
    )
    return send_file(image_io, mimetype="image/png") #on renvoie l'image generee en PNG

@app.route("/generer_formes_simples", methods=["POST"])
def generer_formes_simples():
    data = request.get_json() #on recupere les donnees envoyees par le frontend en JSON
    image_io = generateurFS(
        int(data["nbr_cote"]),
        int(data["taille"]),
        int(data["angle"]),
        data["couleur"]
    )
    return send_file(image_io, mimetype="image/png")  #on renvoie l'image generee en PNG

@app.route("/generer_fractales", methods=["POST"])
def generer_fractales():
    data = request.get_json() #on recupere les donnees envoyees par le frontend en JSON
    image_io = generateur_fractale_koch(
        int(data["taille"]),
        int(data["nbr_rep"]),
        data["couleur"]
    )
    return send_file(image_io, mimetype="image/png") #on renvoie l'image generee en PNG

if __name__ == "__main__":
    app.run(debug=True)
