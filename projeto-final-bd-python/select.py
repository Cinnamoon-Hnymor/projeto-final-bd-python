#Para fazer a seleção 
import psycopg2

conn = psycopg2.connect(database="postgres", name="postgres", password="qw789123",port="5432")
print("Conexão realizada com êxito.")

comando = conn.cursor()
comando.execute("""SELECT * FROM AGENDA where id = 2""")

registro = comando.fetchone()
print("Dados requisitados:", registro)

conn.commit()

print("A seleção foi feita com êxito!")
conn.close()