from flask import Flask, request
from flask_cors import CORS
import json
import firebase
import keywords_parser

app = Flask(__name__)
CORS(app)

# @app.route('/', methods=['GET'])
# def get_data():
#     return json.loads('{"message":"Hello World"}')

@app.route('/createResource', methods=['POST'])
def create_resource():
    frontend_request = request.get_json()
#     print(frontend_request)
    campus_code = frontend_request['campus']
    resource_name = frontend_request['name']
    resource_data = keywords_parser.process_description(frontend_request['data'])

    firebase.add_resource(campus_code, resource_name, resource_data)
    return json.loads('{"message":"success"}')

if __name__ == '__main__':
    app.run(debug=True)