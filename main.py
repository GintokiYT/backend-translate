# Importaciones
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS 

# Asignar el servidor a la variable app
app = Flask(__name__)
# Habilitar cors para consultas externas
CORS(app)

# Direccion del servidor de la api de google translate
url = "https://translate281.p.rapidapi.com/"
# Configuracion para usar la api
headers = {
	"content-type": "application/x-www-form-urlencoded",
	"X-RapidAPI-Key": "49dfd91cccmshe2562acc5b7d6d4p13f504jsnf7507c35264d",
	"X-RapidAPI-Host": "translate281.p.rapidapi.com"
}

# Ruta para recibir y devolver la traduccion
@app.route('/translate', methods=['POST'])
def translate():
  # Obtenemos el request body
  data = request.get_json()
  # Usamos la API de translate
  response = requests.post(url, data=data, headers=headers)
  # Devolvemos en formato JSON la respuesta de la API
  return jsonify(response.json())

# Arrancar la aplicacion de Python
if __name__ == '__main__':
    app.run(debug=True)