from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Получаем ключи из переменных окружения (безопаснее)
CLIENT_ID = os.environ.get('OZON_CLIENT_ID', '1711413')  # Замените на ваш реальный Client-ID
API_KEY = os.environ.get('OZON_API_KEY', 'eda4f687-acad-41b9-832c-e78ced0ecf47')  # Замените на ваш реальный Api-Key

@app.route('/v3/posting/fbs/list', methods=['POST'])
def ozon_fbs_list():
    try:
        data = request.json
        
        # Логируем для отладки
        print(f"Using Client-ID: {CLIENT_ID}")
        print(f"Request data: {data}")
        
        response = requests.post(
            'https://api-seller.ozon.ru/v3/posting/fbs/list',
            json=data,
            headers={
                'Client-Id': CLIENT_ID,
                'Api-Key': API_KEY,
                'Content-Type': 'application/json'
            }
        )
        
        print(f"Ozon API response status: {response.status_code}")
        
        return jsonify(response.json())
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

@app.route('/')
def home():
    return f"Прокси-сервер Ozon API работает! Client-ID: {CLIENT_ID}"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
