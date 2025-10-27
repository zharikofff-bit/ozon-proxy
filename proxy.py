from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Получаем ключи из переменных окружения (БЕЗ значений по умолчанию)
CLIENT_ID = os.environ.get('OZON_CLIENT_ID')
API_KEY = os.environ.get('OZON_API_KEY')

# Проверяем, что ключи заданы
if not CLIENT_ID or not API_KEY:
    raise ValueError("Не заданы OZON_CLIENT_ID или OZON_API_KEY в переменных окружения")

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
    return f"Прокси-сервер Ozon API работает! Client-ID: {CLIENT_ID}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
