from flask import Flask, request
from flask_cors import CORS
import json
import firebase
import keywords_parser
import search_ranking

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_data():
    return json.loads('{"message":"Hello World"}')

@app.route('/createResource', methods=['POST'])
def create_resource():
    frontend_request = request.get_json()
    campus_code = frontend_request['campus']
    resource_name = frontend_request['name']
    resource_data = keywords_parser.process_description(frontend_request['data'])

    firebase.add_resource(campus_code, resource_name, resource_data)
    return json.loads('{"message":"success"}')

@app.route('/searchResources', methods=['POST'])
def search_resource():
    frontend_request = request.get_json()
    
    campus_code = frontend_request['campus']
    target_keywords = keywords_parser.process_situation(campus_code, frontend_request['query'])
    amount_of_results = frontend_request['amount']

    results = search_ranking.rank_resources( campus_code, target_keywords, amount_of_results )

    response = {
        'message':'success',
        'results': results
    }
    
    return json.dumps(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)