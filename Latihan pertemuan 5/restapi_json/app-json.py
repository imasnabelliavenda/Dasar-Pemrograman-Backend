from flask import Flask, jsonify, request, make_response
import json

app = Flask(__name__)
app.config["DEBUG"] = True

#buka file json
file_json = open("restapi_json/mahasiswa.json")

#parsing data json
data = json.loads(file_json.read())

#cetak isi data json
@app.route('/', methods=['GET'])
def index():
    for dtmhs in data['mahasiswa']:
        print(f"Nama: {dtmhs['nama']}")
        print("Alamat: ")
        print(f"- Kecamatan: {dtmhs['alamat'] ['kec']}")
        print(f"- Kabupaten: {dtmhs['alamat'] ['kab']}")
        print(f"Nomor telp: {dtmhs['no_telp']}")
        print("Sosial Media:")
        print(f"- Facebook: {dtmhs['social_media']['facebook']}")
        print(f"- Twitter: {dtmhs['social_media']['twitter']}")
        print(f"- Instagram: {dtmhs['social_media']['instagram']}")

        return make_response(jsonify({'Biodata' : data}), 200)

app.run()