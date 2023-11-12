#Para criar a tabela no banco de dados
import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="qw789123", port="5432")
print("Conexão com o Banco de dados feita com êxito.")

comando = conn.cursor()
comando.execute(""" CREATE TABLE products
(nome TEXT NOT NULL,
codigo int NOT NULL,
preco float NOT NULL)
""")

conn.commit()

print("Tabela criada com sucesso!")
conn.close()
