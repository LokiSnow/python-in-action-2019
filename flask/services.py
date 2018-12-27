from flask import *
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello World"


@app.route('/request', methods=['GET'])
def req():
    data_url = request.args['dataUrl']
    header = request.args['headers']
    param = request.args.to_dict()
    del param['dataUrl']
    del param['headers']
    print('===>' + str(param))
    r = requests.get(data_url, params=param, headers=header)
    return jsonify(r.json())


@app.route('/download', methods=['GET'])
def download():
    data_url = request.args['dataUrl']
    file_name = request.args['fileId']
    header = request.args['headers']
    param = {'fileId': file_name}
    r = requests.get(data_url, params=param, headers=header)
    if r.ok:
        with open('../../data/' + file_name, 'wb') as file:
            file.write(r.content)
        return "Success"
    else:
        return '%d : %s' % (r.status_code, r.text)


if __name__ == '__main__':
    app.run(debug=True)
