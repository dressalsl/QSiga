from bd_aluno import Banco


class Aluno(object):

    def __init__(self, idaluno=0, nome="", cpf=""):
        self.info = {}
        self.idaluno = idaluno
        self.nome = nome
        self.cpf = cpf

    def insertAluno(self):

        banco_aluno = Banco()
        try:

            c = banco_aluno.conexao.cursor()

            c.execute(
                "insert into aluno (nome, cpf) values ('" + self.nome + "', '" + self.cpf + "' )")

            banco_aluno.conexao.commit()
            c.close()

            return "Aluno cadastrado com sucesso!"
        except:
            return "Ocorreu um erro na inserção do aluno"

    def updateAluno(self):

        banco_aluno = Banco()
        try:

            c = banco_aluno.conexao.cursor()

            c.execute(
                "update aluno set nome = '" + self.nome + "', cpf = '" + self.cpf + "' where idaluno = " + self.idaluno + " ")

            banco_aluno.conexao.commit()
            c.close()

            return "Aluno atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do aluno"

    def deleteAluno(self):

        banco_aluno = Banco()
        try:

            c = banco_aluno.conexao.cursor()

            c.execute("delete from aluno where idaluno = " + self.idaluno + " ")

            banco_aluno.conexao.commit()
            c.close()

            return "Aluno excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do aluno"

    def selectAluno(self, idaluno):
        banco_aluno = Banco()
        try:

            c = banco_aluno.conexao.cursor()

            c.execute("select * from aluno where idaluno = " + idaluno + "  ")

            for linha in c:
                self.idaluno = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]

            c.close()

            return "Busca feita com sucesso!"
        except:
            return "Ocorreu um erro na busca do aluno"