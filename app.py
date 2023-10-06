from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

def crear_imagenes(descripcion, num_imagenes):
    openai.api_key = "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"
    openai.Model.list()
    respuestas = []
    for _ in range(num_imagenes):
        respuesta = openai.Image.create(
            prompt=descripcion,
            n=1,  # Generar una imagen a la vez
            size='512x512'
        )
        respuestas.append(respuesta["data"][0]["url"])
    return respuestas

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        data = request.json
        descripcion = data["descripcion"]
        numero_imagenes = int(data["numeroImagenes"])
        try:
            respuestas = crear_imagenes(descripcion, numero_imagenes)
            return jsonify({"respuestas": respuestas})
        except openai.error.APIError as e:
            return jsonify({"error": str(e)})
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
