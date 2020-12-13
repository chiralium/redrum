from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import os, requests

import config

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route( '/' )
@cross_origin()
def index():
  response = jsonify( {"message" : "Hello!" } )
  response.headers['Content-Type'] = 'application/json'
  return response

@app.route( '/deploy', methods=[ 'POST', 'GET' ] )
@cross_origin()
def deploy():
  request_data = request.get_json()
  if request_data is not None:
    if request_data.get('repository'):
      response = {
        'checkout' : os.system('cd /var/www/app/; git checkout .'),
        'fetch' : os.system('cd /var/www/app/; git fetch'),
        'pull' : os.system('cd /var/www/app/; git pull'),
        'build' : os.system('cd /var/www/app/; npm run-script build')
      }

      resp = jsonify( response )
      resp.status_code = 200

      return resp
  return "Undefined request!"

@app.route( '/api/pegas/', methods=[ 'GET' ])
def pegas_status():
  pegas_response = requests.get('http://pegas.bsu.edu.ru', verify=False)
  response = jsonify(
    {
      'status' : pegas_response.status_code
    }
  )

  response.headers['Content-Type'] = 'application/json'
  return response

app.run(debug=True, host=config.HOST)
