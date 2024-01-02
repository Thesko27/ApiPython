import psycopg2
from flask import jsonify, make_response



#Função que retorna a conexão com db

def obterConexao():
   conn = psycopg2.connect(
    host="localhost",
    database="sistema_python",
    user="postgres",
    password="151707",
    port= "5432"

    )
   return conn

# Função que obtem todos os registros da tabela

def obterProdutos():
   connect = obterConexao()
   cursor = connect.cursor()
   cursor.execute("SELECT * FROM produtos")
   produtos = cursor.fetchall()

   myProdutos = list()
   for produto in produtos:
        myProdutos.append({
             'id':produto[0],
             'descricao':produto[1],
             'estoque':produto[2]
        })

   connect.close()
   return make_response (
         myProdutos)


# Função que obtem produtos pelo id

def obterProdutoPeloId(id):
   connect =obterConexao()
   cursor =connect.cursor()
   cursor.execute("SELECT * FROM produtos WHERE Id=%s",[id])
   produto =  cursor.fetchall()
   connect.close()

   return produto

#Função que insere novo produto

def inserirNovoProduto(produto):
   connect = obterConexao()
   cursor = connect.cursor()
   sql = "INSERT INTO produtos (descricao, estoque) VALUES (%s, %s)"
   cursor.execute(sql, [ produto['descricao'], produto['estoque']])
   connect.commit()
   connect.close()
   


# Função Atualizar Produtos
   
def  atualizarDadosDoProduto( produto, id):
      connect = obterConexao()
      cursor = connect.cursor()
      sql = "UPDATE produtos SET descricao = %s, estoque = %s WHERE Id = %s"
      cursor.execute(sql, [produto['descricao'], produto['estoque'], id])
      connect.commit()
      connect.close()


      
# Função Excluir Produtos
      
def excluirProduto(id):
         connect= obterConexao()
         cursor = connect.cursor()
         sql= "DELETE FROM produtos WHERE Id = %s"
         cursor.execute(sql, [id])
         connect.commit()
         connect.close()





excluirProduto(4)
   