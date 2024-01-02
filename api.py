from flask  import Flask, make_response ,request, jsonify
from function_db import *
from flask_cors import  CORS 

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)



@app.route('/produto', methods=['GET'])
def obterProduto():
    produtos = obterProdutos()
    return produtos


@app.route('/produto', methods=['POST'])
def inserirProduto():
    produto = request.json
    inserirNovoProduto(produto)
    
    return jsonify({"mensagem": "Produto adicionador com sucesso!"})

@app.route('/produto/<int:id>', methods=['PUT'])
def atualizarProduto(id):
    produto = request.json
    atualizarDadosDoProduto( produto, id)
    return jsonify({"mensagem":"Os dados do produto foram alterados com sucesso!"})


@app.route("/produto/<int:id>",methods=["DELETE"])
def removerProduto(id):
    excluirProduto(id)
    return jsonify({"mensagem":"O produto foi removido da lista!"})

#30m
app.run()