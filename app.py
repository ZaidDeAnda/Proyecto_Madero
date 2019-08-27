from dbutils import MONGO_URI
from dbutils import db_connect
from dbutils import db_insert_user
from dbutils import db_find_all
<<<<<<< HEAD
from dbutils import db_delete_temp
from form import BuyForm
=======
from form import EmailForm
>>>>>>> parent of 9fcc560... Cambios en la interfaz de compras
from form import LoginForm
from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)
users = db_connect(MONGO_URI, 'mi_app', 'users')


@app.route('/', methods=['GET', 'POST'])
def index():
    form = EmailForm(request.form)
    flag = False
    name = None

    if len(form.errors):
        print(form.errors)
    if request.method == 'POST':
        email = form.email.data
        name = form.name.data
        if email != '' and name != '':
            print(f"Nombre capturado: {name}")
            print(f"Email capturado: {email}")
            user = {
                "name": name,
                "email": email
            }
            db_insert_user(users, user)
            flag = True

    return render_template('index.html', flag=flag, name=name)


@app.route('/admin', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    login_error = False
<<<<<<< HEAD
    list_temporal= []
    if request.method == 'POST':
        item = form.item.data
        precio = form.precio.data
        if item != '' and precio != '':
            list_temporal.append([item, precio])
            flag = True
            return render_template('index.html', list_temporal = list_temporal)
    return render_template('index.html', login_error=login_error)
=======

    if len(form.errors):
        print(form.errors)
    if request.method == 'POST':
        if form.username.data == 'admin' and form.password.data == 'admin':
            registered = db_find_all(users)
            return render_template('tables.html', users=registered)
        else:
            login_error = True
    return render_template('admin.html', login_error=login_error)
>>>>>>> parent of 9fcc560... Cambios en la interfaz de compras


@app.errorhandler(404)
def no_encontrado(error=None):
    return render_template("404.html", url=request.url)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
