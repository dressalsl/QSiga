#importando módulo do SQlite
import sqlite3


class Banco():

    def __init__(self):
        self.conexao = sqlite3.connect('banco_turma.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists turma (
                     idturma integer primary key autoincrement ,
                     codigo_turma text,
                     periodo text,
                     departamento text
                     codigo_disciplina text,
                     cpf_professor text,
                     cpf_aluno text)""")
        self.conexao.commit()
        c.close()