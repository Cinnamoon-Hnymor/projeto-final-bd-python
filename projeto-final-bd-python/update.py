#Para fazer a atualização de dados
import psycopg2

conn = psycopg2.connect(database="postgres", name="postgres", password="qw789123",port="5432")
print("Conexão realizada com sucesso!")

comando = conn.cursor()
comando.execute(""" SELECT * FROM AGENDA where id = 1 """)

registro = comando.fetchone()
print('dados encontrados: ', registro)
comando.execute(""" UPDATE AGENDA set telefone = 988680000 where id = 1 """)

conn.commit()

print("Registro atualizado com sucessso")
comando = conn.cursor()

print("-------Consulta após a atualização feita:-------")
comando.execute(""" SELECT * FROM AGENDA where id  = 1 """)
registro = comando.fetchone()
print("Dados atualizados: ", registro)

conn.commit()
conn.close()