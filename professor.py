from bd_professor import Banco


class Professor():

    def __init__(self, idprofessor=0, nome="", cpf="", departamento=""):
        self.info = {}
        self.idprofessor = idprofessor
        self.nome = nome
        self.cpf = cpf
        self.departamento = departamento

    def insertProfessor(self):
        banco_professor = Banco()
        try:

            c = banco_professor.conexao.cursor()

            c.execute(
                "insert into professor (nome, cpf) values ('" + self.nome + "', '" + self.cpf + "', '" + self.departamento + "' )")

            banco_professor.conexao.commit()
            c.close()

            return "Professor cadastrado com sucesso!"
        except:
            return "Ocorreu um erro no cadastro do professor"

    def updateProfessor(self):
        banco_professor = Banco()
        try:

            c = banco_professor.conexao.cursor()

            c.execute(
                "update professor set nome = '" + self.nome + "', cpf = '" + self.cpf + "', departamento = '"
                + self.departamento + "' where idprofessor = " + self.idprofessor + " ")

            banco_professor.conexao.commit()
            c.close()

            return "Professor atualizado com sucesso!"
        except:
            return "Ocorreu um erro na alteração do professor"

    def deleteProfessor(self):

        banco_professor = Banco()
        try:
            c = banco_professor.conexao.cursor()

            c.execute("delete from professor where idprofessor = " + self.idprofessor + " ")

            banco_professor.conexao.commit()
            c.close()

            return "Professor excluído com sucesso!"
        except:
            return "Ocorreu um erro na exclusão do professor"

    def selectProfessor(self, idprofessor):
        banco_professor = Banco()
        try:
            c = banco_professor.conexao.cursor()

            c.execute("select * from professor where idprofessor = " + idprofessor + "  ")

            for linha in c:
                self.idprofessor = linha[0]
                self.nome = linha[1]
                self.cpf = linha[2]
                self.departamento = linha[3]

            c.close()

            return "Professor achado com sucesso!"

        except:
            return "Ocorreu um erro na busca do professor"

