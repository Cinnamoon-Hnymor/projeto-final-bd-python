#Crud
import psycopg2

class AppBD:
    def __init__(self):
        print("Método construtor")
    def abrirConexao(self):
        try:
            self.connection = psycopg2.connect(user="postgres", password="qw789123",host="127.0.0.1", port="5432",database="postgres")
        except(Exception, psycopg2.Error) as error:
            if (self.connection):
                print("Ops, parece que houve uma falha ao conectar com o BD!", error)