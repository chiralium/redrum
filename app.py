from flask import Flask, request, jsonify
import os

import config

app = Flask(__name__)
print( config.HOST )

@app.route( '/' )
def index():
  return "<p align='center' style='color: cyan'><b>Hello, Redrum!</b></span>"

@app.route( '/deploy', methods=[ 'POST', 'GET' ] )
def deploy():
  request_data = request.get_json()
  if request_data is not None:
    if request_data.get('repository'):
      response = {
        'checkout' : os.popen('git checkout .').read(),
        'fetch' : os.popen('git fetch').read(),
        'pull' : os.popen('git pull').read()
      }

      resp = jsonify( response )
      resp.status_code = 200

      return resp
  return "Undefined request!"

app.run(debug=True, host=config.HOST)
