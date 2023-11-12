import tkinter as tk
import psycopg2

class AppBD:
    def __init__(self):
        print("Método construtor")

    def abrirConexao(self):
        try:
            self.connection = psycopg2.connect(user="postgres", password="qw789123", host="127.0.0.1", port="5432",database="postgres")
        except(Exception, psycopg2.Error) as error:
            if (self.connection):
                print("Houve um problema ao se conectar ao BD.", error)
#A seguir, a função para inserção de dados dentro do BD
    def inserirDados(self, codigo, nome, preco):
        try:

            self.abrirConexao()
            novoPreco = float(preco) * 1.1
            cursor = self.connection.cursor()
            postgresInsertQ = """INSERT INTO public."products"
            ("codigo", "nome", "preco") VALUES (%s,%s,%s)"""
            record_to_insert = (codigo, nome, novoPreco)
            cursor.execute(postgresInsertQ, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Seu registo foi inserido na tabela products")
        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print("Houve um erro ao inserir o registro na tab. products", error)
        finally:
            if self.connection:
                if 'cursor' in locals() and cursor is not None:
                    cursor.close()
                    self.connection.close()
                    print("A conexão com o PostgreSQL foi encerrada.")

#A seguir, a função para fazer a atualização dos dados dentro do banco de dados.
    def atualizarDados(self, codigo, nome, preco):
        try:
            novoPreco = float(preco) * 1.1
            self.abrirConexao()
            cursor = self.connection.cursor()
            sqlUpdateQ = """Update public."products" set "nome" = %s,
            "preco" = %s where "codigo" = %s"""
            cursor.execute(sqlUpdateQ, (nome, novoPreco, codigo))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Seu registro foi atualizado! ")
            print("Seu registro após atualização: ")
            sqlSelectQ = """select * from public."products"
            where "codigo" = %s"""
            cursor.execute(sqlSelectQ, (codigo,))
            record = cursor.fetchone()
            print(record)
        except (Exception, psycopg2.Error) as error:
            print("Houve um erro na ação de update", error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o postgreSQL foi encerrada...")
#A seguir, a função para exclusão de dados do BD
    def excluirDados(self, codigo):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            sqlDeleteQ = """Delete from public."products"
            where "codigo" = %s"""
            cursor.execute(sqlDeleteQ, (codigo,))
            self.connection.commit()
            count = cursor.rowcount
            print(count, "O registro foi eliminado. ")
        except (Exception, psycopg2.Error) as error:
            print("Houve um erro na Exclusão do registro.", error)
        finally:
            if (self.connection):
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi fechada.")

#Criar a GUI principal da aplicação
class PrincipalBD:
    def __init__(self, win):
        self.objBD = AppBD()

        self.lbTitulo = tk.Label(win, text='Registradora de produtos!')
        self.lbCodigo = tk.Label(win, text='Codigo do produto:')
        self.lblNome = tk.Label(win, text='Nome do produto:')
        self.lblPreco = tk.Label(win, text='Preço do produto:')

        self.txtCodigo = tk.Entry(bd=4)
        self.txtNome = tk.Entry(bd=4)
        self.txtPreco = tk.Entry(bd=4)

        self.btnCadastrar = tk.Button(win, text='Cadastrar', command=self.fCadastrarproducts)
        self.btnExcluir = tk.Button(win, text="Exluir", command=self.fExcluirProduto)
        self.btnLimpar = tk.Button(win, text="Limpar", command=self.fLimparTela)
        self.btnAtualizar = tk.Button(win, text='Atualizar', command=self.fAtualizarProduto)

        self.lblNovoPreco = tk.Label(win, text='Preco acrescentado de 10% : ')
        self.lblNovoPreco.place(x=100, y=300)

        self.lbTitulo.place(x=250, y=25)

        self.lbCodigo.place(x=100, y=100)

        self.txtCodigo.place(x=250, y=100)

        self.lblNome.place(x=100, y=150)
        self.txtNome.place(x=250, y=150)

        self.lblPreco.place(x=100, y=200)
        self.txtPreco.place(x=250, y=200)

        self.btnCadastrar.place(x=100, y=250, width=80)
        self.btnExcluir.place(x=300, y=250, width=80)
        self.btnLimpar.place(x=400, y=250, width=80)
        self.btnAtualizar.place(x=200, y=250, width=80)
#A seguir, a função de cadastro de produtos e do cálculo de 10% em acréscimo do valor o qual foi inserido.        
    def fCadastrarproducts(self):
        try:
            codigo, nome, preco = self.fLerCampos
            novoPreco = float(preco) * 1.1
            self.objBD.inserirDados(codigo, nome, preco)
            self.lblNovoPreco.config(text=f'Preco acrescentado 10% : {novoPreco}')
            self.fLimparTela()
            print('O cadastro do produto foi realizado com êxito.')

        except:
            print('Não foi possível fazer o cadastro.')
        return codigo, nome, preco


    @property
    def fLerCampos(self):
        codigo = self.txtCodigo.get()
        nome = self.txtNome.get()
        preco = self.txtPreco.get()
        return codigo, nome, preco

    def fLimparTela(self):
        try:
            self.txtCodigo.delete(0, tk.END)
            self.txtNome.delete(0, tk.END)
            self.txtPreco.delete(0, tk.END)
            print('Campos Limpos!')
        except:
            print('Não foi possível limpar os campos.')

    def fAtualizarProduto(self):
        try:
            codigo, nome, preco = self.fLerCampos
            self.objBD.atualizarDados(codigo, nome, preco)
            self.fLimparTela()
            print('Produto Atualizado com Sucesso!')
        except:
            print('Não foi possível fazer a atualização.')


    def fExcluirProduto(self):
        try:
            codigo, nome, preco = self.fLerCampos
            self.objBD.excluirDados(codigo)
            self.fLimparTela()
            print('O produto foi deletado corretamente.')
        except:
            print('Houve algum imprevisto na exclusão do item.')


    def inserirDados(self, codigo, nome, preco):
        try:
            self.abrirConexao()
            cursor = self.connection.cursor()
            postgresInsertQ = """INSERT INTO public."PRODUTO"
            ("CODIGO", "NOME", "PRECO") VALUES (%s,%s,%s)"""
            record_to_insert = (codigo, nome, preco)
            cursor.execute(postgresInsertQ, record_to_insert)
            self.connection.commit()
            count = cursor.rowcount
            print(count, "Registro inserido com sucesso na tabela PRODUTO")
        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print("Falha ao inserir registro na tabela PRODUTO", error)
        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print("A conexão com o PostgreSQL foi encerrada.")


janela = tk.Tk()
principal = PrincipalBD(janela)
janela.configure(background='#00BFFF')
janela.title('Registro de products')
janela.geometry("600x400")
janela.mainloop()