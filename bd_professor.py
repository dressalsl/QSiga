#importando módulo do SQlite
import sqlite3


class Banco():

    def __init__(self):
        self.conexao = sqlite3.connect('banco_professor.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists professor (
                     idprofessor integer primary key autoincrement ,
                     nome text,
                     cpf text,
                     departamento text)""")
        self.conexao.commit()
        c.close()