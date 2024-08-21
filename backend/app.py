from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app) 

@app.route('/', methods=['GET'])
def get_data():
    return json.loads('{"message":"Hello World"}')

if __name__ == '__main__':
    app.run(debug=True)