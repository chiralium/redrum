from flask import Flask
app = Flask(__name__)

@app.route( '/' )
def index():
  return "Hello, Redrum"

app.run(debug=True, host='45.156.26.185')
