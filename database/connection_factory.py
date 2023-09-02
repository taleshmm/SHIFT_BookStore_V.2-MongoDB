import psycopg2 as pg

class ConnectionFactory:
  def get_connection(self):
   '''Função de Conexão ao Banco de Dados.

Esta função serve como um ponto de entrada para estabelecer uma conexão com o banco de dados. Certifique-se de substituir os placeholders pelos dados específicos do seu ambiente.

Parâmetros:
    - host (str): O endereço do servidor do banco de dados.
    - username (str): O nome de usuário para autenticação.
    - password (str): A senha do usuário para autenticação.
    - database (str): O nome do banco de dados que deseja acessar.
Retorno:
    - conn: A conexão estabelecida com o banco de dados.
    - cursor: O cursor para executar consultas SQL.

Exemplo de uso:
    conn, cursor = connect_to_database('seu_host', 'seu_usuario', 'sua_senha', 'seu_banco_de_dados')
    cursor.execute('SELECT * FROM tabela_exemplo')
    resultados = cursor.fetchall()
    conn.close()
'''
   return  pg.connect(host='Host', database='database', user='user', password='password')
  
  