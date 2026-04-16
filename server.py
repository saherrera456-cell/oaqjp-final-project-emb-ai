from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Iniciar la aplicación Flask
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detector():
    """
    Esta ruta recibe el texto de la interfaz HTML, llama a la API de Watson
    y devuelve el texto formateado con las emociones.
    """
    # Obtener el texto que el usuario ingresó en la página web
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Ejecutar la función que creaste en las Tareas 2 y 3
    response = emotion_detector(text_to_analyze)
    
    # Extraer los valores del diccionario
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    
    # Formatear la respuesta exactamente como lo pide el proyecto
    return f"For the given statement, the system response is 'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    """
    Esta ruta renderiza la página web principal (index.html)
    """
    return render_template('index.html')

if __name__ == "__main__":
    # Ejecutar la aplicación en el puerto 5000
    app.run(host="0.0.0.0", port=5000)
