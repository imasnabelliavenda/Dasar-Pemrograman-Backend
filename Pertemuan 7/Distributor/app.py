from flask import Flask, render_template, request, redirect, url_for
import pymysql
import pymysql.cursors, os

application = Flask(__name__)

conn = cursor = None

#fungsi koneksi database
def openDb():
    global conn, cursor
    conn = pymysql.connect(host="localhost", user="root", passwd="imas", database="stok")
    cursor = conn.cursor()

#fungsi untuk menutup koneksi
def closeDb():
    global conn, cursor
    cursor.close()
    conn.close()

#fungsi view index() untuk menampilkan data dari database
@application.route('/')
def index():
    openDb()
    container = []
    sql = "SELECT * FROM barang"
    cursor.execute(sql)
    results = cursor.fetchall()
    for data in results:
        container.append(data)
    closeDb()
    return render_template('index.html', container=container,)

#form tambah
@application.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        kode = request.form['kode']
        nama = request.form['nama']
        harga = request.form['harga']
        jumlah = request.form['jumlah']
        openDb()
        sql = "INSERT INTO barang (kodebrg, namabrg, harga, jumlah) VALUES (%s, %s, %s, %s)"
        val = (kode, nama, harga, jumlah)
        cursor.execute(sql, val)
        conn.commit()
        closeDb()
        return redirect(url_for('index'))
    
    else:
        return render_template('tambah.html')
    
#fungsi view edit() untuk form edit
@application.route('/edit/<id_barang>', methods=['GET', 'POST'])
def edit(id_barang):
    openDb()
    cursor.execute('SELECT * FROM barang WHERE id_barang=%s', (id_barang))
    data = cursor.fetchone()
    if request.method == 'POST':
        id_barang = request.form['id_barang']
        kode = request.form['kode']
        nama = request.form['nama']
        harga = request.form['harga']
        jumlah = request.form['jumlah']
        sql = "UPDATE barang SET kodebrg=%s, namabrg=%s, harga=%s, jumlah=%s WHERE id_barang=%s"
        val = (kode, nama, harga, jumlah, id_barang)
        cursor.execute(sql, val)
        conn.commit()
        closeDb()
        return redirect(url_for('index'))
    else:
        closeDb()
        return render_template('edit.html', data=data)

#fungsi untuk menghapus data
@application.route('/hapus/<id_barang>', methods=['GET', 'POST'])
def hapus(id_barang):
    openDb()
    cursor.execute('DELETE FROM barang WHERE id_barang=%s', (id_barang,))
    conn.commit()
    closeDb()
    return redirect(url_for('index'))

if __name__ == '__main__':
    application.run(debug=True)