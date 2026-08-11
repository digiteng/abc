from flask import Flask
import requests
import os # İşletim sistemi modülünü ekleyin
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
#GITHUB_URL = os.environ.get('GITHUB_URL')

app = Flask(__name__)

@app.route('/')
def home():
    req="working..."
    return req

@app.route('/about')
def about():
    return "Hakkımızda sayfası"

if __name__ == '__main__':
    app.run()

