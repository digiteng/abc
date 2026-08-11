from flask import Flask
import requests
app = Flask(__name__)

@app.route('/')
def home():
	#return {"status": "Python projesi Vercel üzerinde çalışıyor!"}
	url = 'https://api.github.com/repos/digiteng/xe8/contents/xtra.py'
	header={'accept': 'application/vnd.github.v3.raw', 'authorization': 'token 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'}
	req = requests.get(url, stream=True, allow_redirects=True, headers=header).text
	return req

@app.route('/about')
def about():
	return "Hakkımızda sayfası"

# Vercel için bu kısım önemlidir
if __name__ == '__main__':
	app.run()
