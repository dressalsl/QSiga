#importando módulo do SQlite
import sqlite3 


class Banco():

    def __init__(self):
        self.conexao = sqlite3.connect('aluno.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists aluno (
                     idaluno integer primary key autoincrement ,
                     nome text,
                     cpf text
                     )""")
        self.conexao.commit()
        c.close()