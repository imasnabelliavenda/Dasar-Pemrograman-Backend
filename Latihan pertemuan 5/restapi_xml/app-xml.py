from flask import Flask
import xml.dom.minidom as minidom

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def main():
    #gunakan parse untuk me-load xml ke memori dan di parse
    doc = minidom.parse("restapi_xml/mahasiswa.xml")

    print(doc.nodeName)
    print(doc.firstChild.tagName)

    nama = doc.getElementsByTagName("nama")[1].firstChild.data
    alamat = doc.getElementsByTagName("alamat")[1].firstChild.data
    jurusan = doc.getElementsByTagName("jurusan")[1].firstChild.data
    list_hobi = doc.getElementsByTagName("hobi")

    print("Nama: {}\n Alamat: {}\n Jurusan: {}\n".format(nama, alamat, jurusan))

    print("Memiliki {} hobi:".format(len(list_hobi)))

    for hobi in list_hobi:
        print("-", hobi.getAttribute("name"))

if __name__ == "__main__":
    main()