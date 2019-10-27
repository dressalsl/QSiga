from bd_disciplina import Banco


class Disciplina(object):

    def __init__(self, iddisciplina=0, nome=""):
        self.info = {}
        self.iddisciplina = iddisciplina
        self.nome = nome

    def insertDisciplina(self):
        banco_disciplina = Banco()
        try:

            c = banco_disciplina.conexao.cursor()

            c.execute(
                "insert into disciplina (nome) values ('" + self.nome + "' )")

            banco_disciplina.conexao.commit()
            c.close()

            return "Disciplina cadastrada com sucesso!"
        except:
            return "Ocorreu um erro no cadastro da Disciplina"

    def updateDisciplina(self):
        banco_disciplina = Banco()
        try:

            c = banco_disciplina.conexao.cursor()

            c.execute(
                "update disciplina set nome = '" + self.nome + "' where iddisciplina = " + self.iddisciplina + " ")

            banco_disciplina.conexao.commit()
            c.close()

            return "Disciplina atualizada com sucesso!"
        except:
            return "Ocorreu um erro na alteração da disciplina"

    def deleteDisciplina(self):

        banco_disciplina = Banco()
        try:
            c = banco_disciplina.conexao.cursor()

            c.execute("delete from disciplina where iddisciplina = " + self.iddisciplina + " ")

            banco_disciplina.conexao.commit()
            c.close()

            return "Disciplina excluída com sucesso!"
        except:
            return "Ocorreu um erro na exclusão da Disciplina"


    def selectDisciplina(self, iddisciplina):
        banco_disciplina = Banco()
        try:
            c = banco_disciplina.conexao.cursor()

            c.execute("select * from disciplina where iddisciplina = " + iddisciplina + "  ")

            for linha in c:
                self.iddisciplina = linha[0]
                self.nome = linha[1]

            c.close()

            return "Disciplina achada com sucesso!"

        except:
            return "Ocorreu um erro na busca da Disciplina"

