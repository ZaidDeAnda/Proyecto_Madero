from dbutils import MONGO_URI
from dbutils import db_connect
from dbutils import db_insert_user
from dbutils import db_find_all
from dbutils import db_drop
from form import BuyForm
from form import LoginForm
from flask import Flask
from flask import request
from flask import render_template


app = Flask(__name__)
users = db_connect(MONGO_URI, 'Proyecto_Madero', 'users')

@app.route('/', methods=['GET', 'POST'])
def login():
    form = BuyForm(request.form)
    form2 = LoginForm(request.form)
    login_error = False
    registro={}
    if request.method == 'POST':
        item = form.item.data
        precio = form.precio.data
        if item != '' and precio != '' and item != 'borrar':
            user = {
                "item": item,
                "precio": precio
            }
            db_insert_user(users, user)
            registro = db_find_all(users)
            flag = True
            return render_template('index.html', users = registro)
        if item == 'borrar' and precio == '5':
            db_drop(users)
            registro = db_find_all(users)
            return render_template('index.html', users=registro)
    return render_template('index.html', login_error=login_error)


@app.errorhandler(404)
def no_encontrado(error=None):
    return render_template("404.html", url=request.url)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
