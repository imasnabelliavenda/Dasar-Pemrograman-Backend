import sqlite3

try:
    sqliteConnection = sqlite3.connect('rumah_makan.db')
    cursor = sqliteConnection.cursor()
    print("Database berhasil terkoneksi")
    
    sqlite_create_table_query = '''CREATE TABLE data_makanan(
                                id INTEGER PRIMARY KEY,
                                nama TEXT NOT NULL,
                                harga INTEGER NOT NULL,
                                kategori TEXT NOT NULL,
                                deskripsi TEXT NOT NULL,
                                gambar TEXT);'''
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print('Tabel berhasil dibuat')
    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Error gagal terkoneksi ke database!", error)

finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("Koneksi database selesai")