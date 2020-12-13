from flask import Flask, request, jsonify

import config

app = Flask(__name__)
print( config.HOST )

@app.route( '/' )
def index():
  return "<span style='color: red'>Hello, Redrum!</span>"

@app.route( '/deploy', methods=[ 'POST', 'GET' ] )
def deploy():
  request_data = request.get_json()
  if request_data is not None:
    if request_data.get('repository'):
      response = {
        'fetch' : os.popen('git fetch').read(),
        'pull' : os.popen('git pull').read()
      }

      resp = jsonify( response )
      resp.status_code = 200

      return resp
  return "Undefined request!"

app.run(debug=True, host=config.HOST)
