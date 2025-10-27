from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

CLIENT_ID = "1711413"
API_KEY = "eda4f687-acad-41b9-832c-e78ced0ecf47"

@app.route('/v3/posting/fbs/list', methods=['POST'])
def ozon_fbs_list():
    try:
        data = request.json
        
        response = requests.post(
            'https://api-seller.ozon.ru/v3/posting/fbs/list',
            json=data,
            headers={
                'Client-Id': CLIENT_ID,
                'Api-Key': API_KEY,
                'Content-Type': 'application/json'
            }
        )
        
        return jsonify(response.json())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def home():
    return "Прокси-сервер Ozon API работает!"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)