# Importaciones
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS 
from openai import OpenAI

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

@app.route('/chatgpt', methods=['POST'])
def chatgpt():
  client = OpenAI(api_key='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')
  data = request.get_json()

  chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "user", 
        "content": data['text']
      }
    ]
  )

  print(chat_completion.json())

  return jsonify(chat_completion.json())

# Arrancar la aplicacion de Python
if __name__ == '__main__':
    app.run(debug=True)