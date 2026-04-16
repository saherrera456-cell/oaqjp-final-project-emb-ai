"""
Servidor Flask para la aplicación de detección de emociones.
Este archivo despliega la aplicación web en localhost:5000
y maneja las peticiones de análisis de texto.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    Recibe el texto de la solicitud, llama al detector de emociones
    y devuelve la respuesta formateada o un mensaje de error.
    """
    # Obtener el texto de la petición
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Obtener la respuesta del detector
    response = emotion_detector(text_to_analyze)
    
    # Manejo de errores si la entrada es inválida
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
        
    # Retornar la cadena formateada (dividida para no exceder límite de línea)
    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Renderiza la página HTML principal de la aplicación.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
