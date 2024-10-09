from flask import Flask, jsonify, request, make_response

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def hello():
    data = [{
        'nama': 'Galih',
        'pekerjaan': 'Web Engineer',
        'pesan': 'Hello World'
    }]
    return make_response(jsonify({'data': data}), 200)

@app.route('/karyawan', methods=['GET', 'POST', 'PUT', 'DELETE'])
def karyawan():
    try:
        if request.method == 'GET':
            data = [{
                'nama' : 'Galih GET',
                'pekerjaan' : 'Web Engineer',
                'usia' : '27',
            }]
        elif request.method == 'POST':
            data = [{
                'nama' : 'Galih POST',
                'pekerjaan' : 'Web Engineer',
                'usia' : '27',
            }]
        elif request.method == 'PUT':
            data = [{
                'nama' : 'Galih PUT',
                'pekerjaan' : 'Web Engineer',
                'usia' : '27',
            }]
        else:
            data = [{
                'nama' : 'Galih DELETE',
                'pekerjaan' : 'Web Engineer',
                'usia' : '27',
            }]
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 400)
    return make_response(jsonify({'data': data}), 200)

app.run()    