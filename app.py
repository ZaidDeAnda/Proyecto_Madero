from dbutils import MONGO_URI
from dbutils import db_connect
from dbutils import db_insert_user
from dbutils import db_find_all
from form import BuyForm
from form import LoginForm
from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)
users = db_connect(MONGO_URI, 'Proyecto_Madero', 'users')


@app.route('/admin', methods=['GET', 'POST'])
def index():
    form = BuyForm(request.form)
    flag = False
    name = None

    if len(form.errors):
        print(form.errors)
    if request.method == 'POST':
        item = form.item.data
        precio = form.precio.data
        if item != '' and precio != '':
            print(f"Nombre capturado: {item}")
            print(f"Email capturado: {precio}")
            user = {
                "item": item,
                "precio": precio
            }
            db_insert_user(users, user)
            flag = True

    return render_template('index.html', flag=flag, name=name)


@app.route('/', methods=['GET', 'POST'])
def login():
    form = BuyForm(request.form)
    login_error = False
    if request.method == 'POST':
        item = form.item.data
        precio = form.precio.data
        if item != '' and precio != '':
            user = {
                "item": item,
                "precio": precio
            }
            db_insert_user(users, user)
            registro = db_find_all(users)
            flag = True
            return render_template('index.html', users = registro)
    return render_template('index.html', login_error=login_error, users= registro)


@app.errorhandler(404)
def no_encontrado(error=None):
    return render_template("404.html", url=request.url)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
