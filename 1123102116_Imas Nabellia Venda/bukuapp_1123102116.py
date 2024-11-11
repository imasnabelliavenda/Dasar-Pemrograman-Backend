from flask import Flask, render_template, request, redirect, url_for
import pymysql
import pymysql.cursors

app = Flask(__name__)

conn = cursor = None

def openDb():
    global conn, cursor
    conn = pymysql.connect(host="localhost", user="root", passwd="imas", database="perpus_1123102116")
    cursor = conn.cursor()

def closeDb():
    global conn, cursor
    cursor.close()
    conn.close()

@app.route('/')
def index():
    openDb()
    container = []
    sql = "SELECT * FROM buku_1123102116"
    cursor.execute(sql)
    results = cursor.fetchall()
    for data in results:
        container.append(data)
    closeDb()
    return render_template('index_1123102116.html', container=container)

@app.route('/tambah', methods=['GET', 'POST'])
def tambah():
    if request.method == 'POST':
        kode = request.form['kode']
        nama = request.form['nama']
        penerbit = request.form['penerbit']
        pengarang = request.form['pengarang']
        jumlah = request.form['jumlah']
        openDb()
        
        sql = "INSERT INTO buku_1123102116 (kode_buku, nama_buku, penerbit, pengarang, jumlah_buku) VALUES (%s, %s, %s, %s, %s)"
        val = (kode, nama, penerbit, pengarang, jumlah)
        cursor.execute(sql, val)
        conn.commit()
        closeDb()
        return redirect(url_for('index'))
    else:
        return render_template('tambah_1123102116.html')

@app.route('/edit/<kode_buku>', methods=['GET', 'POST'])
def edit(kode_buku):
    openDb()
    cursor.execute('SELECT * FROM buku_1123102116 WHERE kode_buku=%s', (kode_buku,))
    data = cursor.fetchone()
    if request.method == 'POST':
        kode = request.form['kode']
        nama = request.form['nama']
        penerbit = request.form['penerbit']
        pengarang = request.form['pengarang']
        jumlah = request.form['jumlah']
        sql = "UPDATE buku_1123102116 SET kode_buku=%s, nama_buku=%s, penerbit=%s, pengarang=%s, jumlah_buku=%s WHERE kode_buku=%s"
        val = (kode, nama, penerbit, pengarang, jumlah, kode_buku)
        cursor.execute(sql, val)
        conn.commit()
        closeDb()
        return redirect(url_for('index'))
    else:
        closeDb()
        return render_template('edit_1123102116.html', data=data)

@app.route('/hapus/<kode_buku>', methods=['GET', 'POST'])
def hapus(kode_buku):
    openDb()
    cursor.execute('DELETE FROM buku_1123102116 WHERE kode_buku=%s', (kode_buku,))
    conn.commit()
    closeDb()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
