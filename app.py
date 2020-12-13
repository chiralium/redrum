from flask import Flask, request, jsonify
import os, requests

import config

app = Flask(__name__)

@app.route( '/' )
def index():
  response = jsonify( {"message" : "Hello!" } )
  response.headers['Content-Type'] = 'application/json';
  return response

@app.route( '/deploy', methods=[ 'POST', 'GET' ] )
def deploy():
  request_data = request.get_json()
  if request_data is not None:
    if request_data.get('repository'):
      response = {
        'checkout' : os.system('cd /var/www/app/; git checkout .'),
        'fetch' : os.system('cd /var/www/app/; git fetch'),
        'pull' : os.system('cd /var/www/app/; git pull')
      }

      resp = jsonify( response )
      resp.status_code = 200

      return resp
  return "Undefined request!"

@app.route( '/api/pegas/', methods=[ 'GET' ])
def pegas_status():
  pegas_response = requests.get('https://pegas.bsu.edu.ru', verify=False)
  response = jsonify(
    {
      'status' : pegas_response.status_code
    }
  )

  response.headers['Content-Type'] = 'application/json'
  return response

app.run(debug=True, host=config.HOST)
