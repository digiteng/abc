
from flask import Flask, request, jsonify
import requests
import os
GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
GITHUB_URL = os.environ.get('GITHUB_URL')
TMDB_API = os.environ.get('TMDB_API')
VERCEL_SIFRE = os.environ.get('MY_APP_PASSWORD')
app = Flask(__name__)

@app.route('/')
def home():
    gelen_sifre = request.headers.get('X-Api-Key')
    if not VERCEL_SIFRE or gelen_sifre != VERCEL_SIFRE:
        return jsonify({"ERROR": "Unauthorized Access"})
    lang = "en"
    title = "joker"
    year = "2019"
    srch = "movie"
    headers = {
    'user-agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 12_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Instagram 105.0.0.11.118 (iPhone11,8; iOS 12_3_1; en_US; en-US; scale=2.00; 828x1792; 165586599)',
    }
    base_tmdb_url = "https://api.themoviedb.org/3/"
    url=f"{base_tmdb_url}search/{srch}?api_key={TMDB_API}&language={lang}&query={title}&year={year}"
    req = requests.get(url, headers=headers).json()
    
    return req

@app.route('/about')
def about():
    return "by digiteng"

if __name__ == '__main__':
    app.run()

