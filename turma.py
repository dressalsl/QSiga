from bd_turma import Banco


class Turma(object):

    def __init__(self, idturma=0, codigo_turma="", periodo="", codigo_disciplina="",cpf_professor="",cpf_aluno=""):
        self.info = {}
        self.idturma = idturma
        self.codigo_turma = codigo_turma
        self.periodo = periodo
        self.codigo_disciplina = codigo_disciplina
        self.cpf_professor = cpf_professor
        self.cpf_aluno = cpf_aluno

    def insertTurma(self):
        banco_turma = Banco()
        try:

            c = banco_turma.conexao.cursor()

            c.execute(
                "insert into turma (codigo_turma,periodo, codigo_disciplina, cpf_professor,cpf_aluno) "
                "values ('" + self.codigo_turma + "', '" + self.periodo + "', '" + self.codigo_disciplina +
                "', '" + self.cpf_professor + "', '" + self.cpf_aluno + "' )")

            banco_turma.conexao.commit()
            c.close()

            return "Turma cadastrada com sucesso!"
        except:
            return "Ocorreu um erro no cadastro da turma"

    @property
    def updateTurma(self):
        banco_turma = Banco()
        try:

            c = banco_turma.conexao.cursor()

            c.execute(
                "update turma set codigo_turma = '" + self.codigo_turma + "', periodo = '" + self.periodo +
                "', codigo_disciplina = '" + self.codigo_disciplina + "', cpf_professor = '" + self.cpf_professor +
                "', cpf_aluno = '" + self.cpf_aluno + "' where idturma = " + self.idturma + " ")

            banco_turma.conexao.commit()
            c.close()

            return "Turma atualizada com sucesso!"
        except:
            return "Ocorreu um erro na alteração da turma"

    def deleteTurma(self):

        banco_turma = Banco()
        try:
            c = banco_turma.conexao.cursor()

            c.execute("delete from turma where idturma = " + self.idturma + " ")

            banco_turma.conexao.commit()
            c.close()

            return "Turma excluída com sucesso!"
        except:
            return "Turma um erro na exclusão do professor"


    def selectProfessor(self, idturma):
        banco_turma = Banco()
        try:
            c = banco_turma.conexao.cursor()

            c.execute("select * from turma where idturma = " + idturma + "  ")

            for linha in c:
                self.idturma = linha[0]
                self.codigo_turma = linha[1]
                self.periodo = linha[2]
                self.codigo_disciplina = linha[3]
                self.cpf_professor = linha[4]
                self.cpf_aluno = linha[5]

            c.close()

            return "Turma achada com sucesso!"

        except:
            return "Ocorreu um erro na busca da turma"

