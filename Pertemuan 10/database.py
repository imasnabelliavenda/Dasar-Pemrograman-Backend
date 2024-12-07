import sqlite3

try:
    sqliteConnection = sqlite3.connect('database_siswa.db')
    cursor = sqliteConnection.cursor()
    print("Database berhasil terkoneksi")
    #membuat tabel pada database
    sqlite_create_table_query = '''CREATE TABLE data_siswa(
                                id INTEGER PRIMARY KEY,
                                nama TEXT NOT NULL,
                                email TEXT NOT NULL UNIQUE);'''
    #eksekusi perintah sql
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