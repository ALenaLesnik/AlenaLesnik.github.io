# Импортируем подмодули Flask для запуска веб-сервиса
from flask import Flask, request, redirect, session, url_for
import json

app = Flask(__name__)

@app.route("/", methods=['POST'])
def main():
# Функция получает тело запроса и возвращает ответ
    response = {
        "version": request.json['version'],
        "session": request.json['session'],
        "response": {
            "end_session": False
        }
    }
    response['response']['text'] = 'Все говорят купи слона!'
    return json.dumps(response)
