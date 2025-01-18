from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import sqlite3 as sql
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
DATABASE = os.path.join(os.path.dirname(__file__), 'rumah_makan.db')

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'stikom123'

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_db_connection():
    conn = sql.connect(DATABASE)
    conn.row_factory = sql.Row
    return conn

@app.route('/')
@app.route('/index')
def index():
    kategori = request.args.get('kategori')
    sqliteConnection = sql.connect('rumah_makan.db')
    cursor = sqliteConnection.cursor()
    cursor.row_factory = sql.Row

    if kategori and kategori != 'all':
        cursor.execute("SELECT * FROM data_makanan WHERE kategori=?", (kategori,))
    else:
        cursor.execute("SELECT * FROM data_makanan")

    data = cursor.fetchall()
    return render_template("index.html", datas=data, selected_kategori=kategori)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin':
            flash('Login Berhasil!', 'success')
            return redirect(url_for('admin_menu'))
        else:
            flash('Kredensial salah, coba lagi.', 'danger')
            return redirect(url_for('login'))
    
    return render_template("login.html")


@app.route("/admin/menu")
def admin_menu():
    kategori = request.args.get('kategori')
    sqliteConnection = sql.connect('rumah_makan.db')
    cursor = sqliteConnection.cursor()
    cursor.row_factory = sql.Row

    if kategori and kategori != 'all':
        cursor.execute("SELECT * FROM data_makanan WHERE kategori=?", (kategori,))
    else:
        cursor.execute("SELECT * FROM data_makanan")

    data = cursor.fetchall()
    return render_template("admin/menu.html", datas=data, selected_kategori=kategori)


@app.route("/tambah-data", methods=['POST', 'GET'])
def tambah_data():
    if request.method == 'POST':
        nama = request.form['nama']
        harga = request.form['harga']
        kategori = request.form['kategori']
        deskripsi = request.form['deskripsi']

        file = request.files['gambar']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
        else:
            filename = None

        sqliteConnection = sql.connect('rumah_makan.db')
        cursor = sqliteConnection.cursor()
        cursor.execute("INSERT INTO data_makanan (nama, harga, kategori, deskripsi, gambar) VALUES (?, ?, ?, ?, ?)",
                       (nama, harga, kategori, deskripsi, filename))
        sqliteConnection.commit()
        flash('Data berhasil ditambahkan!', 'success')
        return redirect(url_for("admin_menu"))
    return render_template("admin/tambah_data.html")


@app.route("/edit-data/<int:id>", methods=['GET', 'POST'])
def edit_data(id):
    sqliteConnection = sql.connect('rumah_makan.db')
    cursor = sqliteConnection.cursor()
    cursor.row_factory = sql.Row

    if request.method == 'POST':
        nama = request.form['nama']
        harga = request.form['harga']
        kategori = request.form['kategori']
        deskripsi = request.form['deskripsi']
        file = request.files['gambar']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
        else:
            filename = request.form.get('old_image', None)

        cursor.execute(
            """UPDATE data_makanan
               SET nama=?, harga=?, kategori=?, deskripsi=?, gambar=?
               WHERE ID=?""",
            (nama, harga, kategori, deskripsi, filename, id)
        )
        sqliteConnection.commit()
        flash('Data berhasil diperbarui!', 'success')
        return redirect(url_for("admin_menu"))

    cursor.execute("SELECT * FROM data_makanan WHERE ID=?", (id,))
    data = cursor.fetchone()
    return render_template("admin/edit_data.html", datas=data)


@app.route("/delete-data/<int:id>", methods=['POST'])
def delete_data(id):
    """Endpoint untuk menghapus data menu"""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM data_makanan WHERE ID=?", (id,))
        conn.commit()
        conn.close()
        return {"message": "Data berhasil dihapus!"}, 200
    except sql.Error as e:
        return jsonify({'error': f"Database error: {e}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
