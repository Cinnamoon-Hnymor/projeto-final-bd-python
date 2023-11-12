#Para fazer a inserção
import psycopg2

conn = psycopg2.connect(database="postgres", user="postgres", password="qw789123", port="5432")
print("Sua conexão foi feita com êxito.")

comando = conn.cursor()
comando.execute("""INSERT INTO products (codigo, nome, preco))""")

conn.commit()

print("A inserção foi concluída com sucesso.")
conn.close()