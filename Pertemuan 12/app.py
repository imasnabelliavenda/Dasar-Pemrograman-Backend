from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

#tentukan folder untuk menyimpan file yang diupload
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#tentukan ekstensi file yang diizinkan
ALLOWES_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf', 'bmp', 'doc', 'txt'}

#function untuk memeriksa ektensi file yang diupload
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWES_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        #periksa apakah file ada dalam request
        if 'file' not in request.files:
            return 'Tidak ada file'
        file = request.files['file']

        #jika tidak ada file yang dipilih
        if file.filename == '':
            return 'Tidak ada file yang dipilih'
        
        if file and allowed_file(file.filename):
            #menyimpan file di folder uploads
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            return f'{filename} berhasil diupload'
        else:
            return 'Type file tidak sesuai(png, jpg, jpeg, gif, pdf, bmp, doc, txt)'
        
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)