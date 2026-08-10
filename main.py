from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
	return {"status": "Python projesi Vercel üzerinde çalışıyor!"}

@app.route('/about')
def about():
	return "Hakkımızda sayfası"

# Vercel için bu kısım önemlidir
if __name__ == '__main__':
	app.run()
