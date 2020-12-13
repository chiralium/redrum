from flask import Flask, request, jsonify
import subprocess

import config

app = Flask(__name__)
print( config.HOST )

@app.route( '/' )
def index():
  return "<p align='center' style='color: gainsboro; font-size: 32pt'><b>Hello, Redrum...</b></span>"

@app.route( '/deploy', methods=[ 'POST', 'GET' ] )
def deploy():
  request_data = request.get_json()
  if request_data is not None:
    if request_data.get('repository'):
      checkout = subprocess.Popen( 'git checkout .', stdout=subprocess.PIPE, shell=True ).stdout
      fetch = subprocess.Popen( 'git fetch', stdout=subprocess.PIPE, shell=True ).stdout
      pull = subprocess.Popen( 'git pull', stdout=subprocess.PIPE, shell=True ).stdout

      response = {
        'checkout' : checkout.read(),
        'fetch' : fetch.read(),
        'pull' : pull.read()
      }

      resp = jsonify( response )
      resp.status_code = 200

      return resp
  return "Undefined request!"

app.run(debug=True, host=config.HOST)
