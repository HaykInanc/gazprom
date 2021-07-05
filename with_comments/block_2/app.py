# импорт класса Flask и метода render_template, который позволит 
# использовать шаблоны для вывода результата

from flask import Flask, render_template

# библиотека json позволяет преобразовать строку в json формате в питоновский словарь
import json

# создание объекта app, который отвечает за работу нашего сервера
app = Flask(__name__)


# связь ссылки с контроллером (этот контроллер необходим для корректной работы
# статических файлов)
@app.route('/<path:path>')
def static_file(path):
	 return app.send_static_file(path)


# связка URL с контроллером, который выводит home page при обращении к адресу 
# локального сервера
@app.route('/')
def home_page():
	return 'home page'


# связка URL с контроллером, который выводит goods page при обращении к адресу 
# /goods локального сервера
@app.route('/goods')
def goods_page():
	return 'goods page'


# связка URL с контроллером, с передачей параметра в контроллер из URL
# обратите внимание, что функция контроллера принимает аргумент name
@app.route('/hello/<name>')
def about_page(name):
	return f'hello page {name}'


# связка URL с контроллером, который отображает шаблон index.html из папки templates
# при обращении по адресу /main
@app.route('/main')
def main_page():
	return render_template('index.html')


# связка URL с контроллером, который 
# 1) считывает данные из model/data.json и преобразовывает содержимое файла 
#    в питоновский словарь
# 2) отображает шаблон index_1.html из папки templates и передает туда 
#    список с данными о карточках для дальнейшего формирования HTML страницы

@app.route('/main_1')
def main_page_1():
	with open('model/data.json', 'r') as f:
		data = json.load(f)['data']


	return render_template('index_1.html', data=data)



# запуск приложения в виде сервера 
# (приложение будет находится в постоянном ожидании http запроса и в случае его 
#  возникновения будет возвращать ответ)
app.run()