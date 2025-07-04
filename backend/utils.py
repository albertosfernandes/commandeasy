from flask import Flask, request, jsonify
import boto3
import uuid
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)
#Configuraçao para Dynamodb
dynamodb = boto3.resource(
    'dynamodb',
    regiona_namev='us-east-1',
    endpoint_url='http://localhost:8000',
    aws_access_key_id = 'fake'
    aws_secret_access_key = 'fake'
)

#Nome da Tabela
TABELA_NOME = 'CommandTable'
tabela = dynamodb.Table(TABELA_NOME)

@app.route('/comandos', methods=['GET'])
def listar_comandos():
    try:
        response = tabela.scan()
        return jsonify(response
        ['Itens']), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500


@app.route('/comandos', methods=['POST'])
def adicionar_comandos():
    try:
        data = request.json
        comando = {
            'id' : str(uuid.uuid4()),
            'descricao' : data.get('descricao'),
            'comando' : data.get('comando'),
            'tags': data.get('tags',[]),
            'referencia' : data.get('referencia'),
            'created_at' : datetime.utcnow().isoformat()
        }
        tabela.put_item(Item=comando)
        return jsonify({'msg': 'Comando adicionado com sucesso', 'comando': comando}), 201
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 