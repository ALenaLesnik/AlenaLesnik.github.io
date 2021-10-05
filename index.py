# Импортируем подмодули Flask для запуска веб-сервиса
from flask import Flask, request, redirect, session, url_for

app = Flask(__name__)

@app.route("/")
def main():
# Функция получает тело запроса и возвращает ответ
    return "Hello from github"
