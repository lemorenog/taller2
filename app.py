import os
import random
from flask import Flask, jsonify, render_template_string

# Inicializar la aplicación Flask
app = Flask(__name__)

# Obtener el ID del contenedor (hostname)
container_id = os.hostname()

# --- Base de datos "quemada" de Pokeneas ---
# RECUERDA: Reemplaza las URLs de 'imagen' con las URLs públicas de tu bucket S3.
pokeneas = [
    {
        "id": 1,
        "nombre": "Pikachu Nea",
        "altura": "0.4m",
        "habilidad": "Estatico (pero en la moto)",
        "imagen": "https://pokedex323.s3.us-east-1.amazonaws.com/nea1.jpg",
        "frase_filosofica": "Más vale calambre en mano que cien corrientazos volando."
    },
    {
        "id": 2,
        "nombre": "Charmander de Bello",
        "altura": "0.6m",
        "habilidad": "Llama (pero no de la policía)",
        "imagen": "https://pokedex323.s3.us-east-1.amazonaws.com/nea2.jpg",
        "frase_filosofica": "No dejes para mañana el asado que puedes hacer hoy."
    },
    {
        "id": 3,
        "nombre": "Snorlax de Envigado",
        "altura": "2.1m",
        "habilidad": "Ronquido (en plena ciclovía)",
        "imagen": "https://pokedex323.s3.us-east-1.amazonaws.com/nea3.jpg",
        "frase_filosofica": "El que madruga... encuentra todo cerrado."
    },
    {
        "id": 4,
        "nombre": "Psyduck de Itagüí",
        "altura": "0.8m",
        "habilidad": "Confusión (después de la rotonda)",
        "imagen": "https://pokedex323.s3.us-east-1.amazonaws.com/nea4.jpg",
        "frase_filosofica": "¿Yo qué sé, güevón? Pregúntele a otro."
    },
    {
        "id": 5,
        "nombre": "Mewtwo del Poblado",
        "altura": "2.0m",
        "habilidad": "Presión (social)",
        "imagen": "https://pokedex323.s3.us-east-1.amazonaws.com/nea5.jpg",
        "frase_filosofica": "Existir es resistir... en tacones."
    },
    {
        "id": 6,
        "nombre": "Gengar de Aranjuez",
        "altura": "1.5m",
        "habilidad": "Sombra Vil (en el callejón)",
        "imagen": "https://pokedex323.s3.us-east-1.amazonaws.com/nea6.jpg",
        "frase_filosofica": "El que ríe de último, ríe mejor (y asusta)."
    },
    {
        "id": 7,
        "nombre": "Bulbasaur de Sabaneta",
        "altura": "0.7m",
        "habilidad": "Espesura (como el tráfico en hora pico)",
        "imagen": "https://pokedex323.s3.us-east-1.amazonaws.com/nea7.jpg",
        "frase_filosofica": "Crecer es como un tamal, lo importante es lo de adentro."
    }
]


# --- Ruta 1: JSON con información del Pokenea ---
@app.route("/api/pokenea")
def pokenea_json():
    # Selecciona un Pokenea al azar
    pokenea = random.choice(pokeneas)
    
    # Prepara la respuesta JSON como se pide
    response_data = {
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "id_contenedor": container_id  
    }
    
    return jsonify(response_data)

# --- Ruta 2: Visual con imagen y frase ---

@app.route("/")
def pokenea_visual():
    # Selecciona un Pokenea al azar
    pokenea = random.choice(pokeneas)
    
    # HTML para mostrar la imagen y la frase
    html_template = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-B">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pokenea Aleatorio</title>
        <style>
            body { 
                font-family: Arial, sans-serif; 
                display: grid;
                place-items: center;
                min-height: 90vh;
                background-color: #f0f0f0;
                color: #333;
                text-align: center;
            }
            .card {
                background-color: #fff;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                padding: 20px;
                max-width: 400px;
            }
            img {
                max-width: 100%;
                height: auto;
                border-radius: 5px;
            }
            h1 {
                color: #e44d26;
            }
            blockquote {
                font-style: italic;
                font-size: 1.2em;
                margin: 15px 0;
            }
            .container-id {
                font-size: 0.8em;
                color: #777;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>{{ pokenea.nombre }}</h1>
            <img src="{{ pokenea.imagen }}" alt="Imagen de {{ pokenea.nombre }}">
            <blockquote>"{{ pokenea.frase_filosofica }}"</blockquote>
            <div class="container-id">
                ID del Contenedor: {{ container_id }}
            </div>
        </div>
    </body>
    </html>
    """
    
    # Muestra la plantilla con los datos del Pokenea
    return render_template_string(
        html_template, 
        pokenea=pokenea, 
        container_id=container_id
    )

# --- Iniciar la aplicación ---
if __name__ == "__main__":
    # Corre en el puerto 80, accesible desde fuera del contenedor
    app.run(host="0.0.0.0", port=80)