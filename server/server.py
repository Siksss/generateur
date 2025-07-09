from flask import Flask, request, send_file
from flask_cors import CORS
from generateur import generateur_png
from generateur_fractale import generateur_fractale_koch

app = Flask(__name__)
CORS(app)

@app.route("/generer", methods=["POST"])
def generer():
    data = request.get_json()
    image_io = generateur_png(
        int(data["nbr_cote"]),
        int(data["nbr_rep"]),
        int(data["taille"]),
        int(data["angle"]),
        data["couleur"]
    )
    return send_file(image_io, mimetype="image/png")

@app.route("/generer_fractales", methods=["POST"])
def generer_fractales():
    data = request.get_json()
    image_io = generateur_fractale_koch(
        int(data["taille"]),
        int(data["nbr_rep"]),
        data["couleur"]
    )
    return send_file(image_io, mimetype="image/png")

if __name__ == "__main__":
    app.run(debug=True)
