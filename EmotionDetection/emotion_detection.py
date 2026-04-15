import requests  # Importar la biblioteca requests para realizar peticiones HTTP
import json      # Importar json para manejar el formato de los datos

def emotion_detector(text_to_analyse):
    """
    Función que envía un texto a la API de Watson NLP para detección de emociones.
    """
    # URL del servicio de predicción de emociones de Watson
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Cabeceras (headers) necesarias para que la API identifique el modelo a utilizar
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Diccionario con el texto que el usuario desea analizar
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # Realizar la petición POST enviando el JSON y las cabeceras
    response = requests.post(url, json=myobj, headers=headers)
    
    # Retornar el texto de la respuesta (formato JSON crudo)
    return response.text
