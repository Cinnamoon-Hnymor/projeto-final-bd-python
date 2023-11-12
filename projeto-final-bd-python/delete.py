#Para deletar algum dado
import psycopg2

conn = psycopg2.connect(database="postgres", name="postgres", password="qw789123",port="5432")
print("Sua conexão foi feita com êxito.")

comando = conn.cursor()
comando.execute(""" DELETE FROM AGENDA where codigo = 1 """)

conn.commit()

cont = comando.rowcount
print(cont, "-> O registro foi deletado.")

print("A exclusão foi concluída.")
conn.close()