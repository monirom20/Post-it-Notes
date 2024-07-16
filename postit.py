from flask import Flask, render_template, request, redirect, url_for
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()



def connectBD():
    return mysql.connect()

def readBD(SQL_sentence):
    conn = connectBD()
    cursor = conn.cursor()
    cursor.execute(SQL_sentence)
    datos = cursor.fetchall()
    conn.close()
    return datos

@app.route("/")
def postit():
    return render_template('postit.html')

@app.route("/postit/list_notes")
def list_notes():
    datos = readBD("SELECT * from post_it")
    return render_template('list_notes.html', data=datos)

@app.route("/postit/add_notes")
def add_notes():
    datos = readBD("SELECT * from marca ORDER BY idmarca")
    return render_template('add_notes.html', data=datos)

@app.route('/postit/save_note', methods=['POST'])
def save_note():
    title = request.form["titulo"]
    description = request.form["descripcion"]
    date = request.form["fecha"]
    priority = request.form["prioridad"]
    mark = request.form["marca"]

    sentence = "INSERT INTO post_it(titulo, descripcion, fecha, prioridad, idmarca) \
                    VALUES (%s, %s, %s, %s, %s)"

    conn = connectBD()
    cursor = conn.cursor()
    cursor.execute(sentence, (title, description, date, priority, mark) )
    conn.commit()
    conn.close()

    return redirect(url_for('postit'))


@app.route("/postit/find_notes")
def search_notes():
    return render_template('find_notes.html')


@app.route("/postit/search_result", methods=['POST'])
def search_result():
    text = request.form["texto"]

    sentence = "SELECT * FROM post_it WHERE titulo LIKE '%" + text + "%' OR descripcion LIKE '%" + text + "%'"
    conn = connectBD()
    cursor = conn.cursor()
    cursor.execute(sentence)
    datos = cursor.fetchall()
    conn.close()

    return render_template('search_result.html', data=datos)


@app.route("/postit/delete_notes")
def delete_notes():
    datos = readBD("SELECT * from post_it")
    return render_template('delete_notes.html', data=datos)


@app.route("/postit/delete_row", methods=["POST"])
def delete_row():
    postit = request.form["button"]

    sentence = "DELETE FROM post_it WHERE idpost_it = %s"
    conn = connectBD()
    cursor = conn.cursor()
    cursor.execute(sentence, (postit, ) )
    conn.commit()
    conn.close()

    return redirect(url_for('delete_notes'))


if __name__ == "__main__":
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'postit'
    app.config['MYSQL_DATABASE_Host'] = 'localhost'

    mysql.init_app(app)
    app.run()
