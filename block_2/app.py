from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/<path:path>')
def static_file(path):
	 return app.send_static_file(path)

@app.route('/')
def home_page():
	return 'home page'

@app.route('/goods')
def goods_page():
	return 'goods page'

@app.route('/hello/<name>')
def about_page(name):
	return f'hello page {name}'

@app.route('/main')
def main_page():
	return render_template('index.html')

@app.route('/main_1')
def main_page_1():
	with open('model/data.json', 'r') as f:
		data = json.load(f)['data']


	return render_template('index_1.html', data=data)

if __name__ == '__main__':
	app.run()