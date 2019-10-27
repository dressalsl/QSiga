from turma import Turma

from tkinter import *


class Application:
    def __init__(self, master=None):
        self.fonte = ("Arial", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 50
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.tituloqsiga = Label(self.container1, text="╰☆╮ QSIGA 2.0 ╰☆╮")
        self.tituloqsiga["font"] = ("Calibri", "10", "bold")
        self.tituloqsiga.pack()

        self.titulo = Label(self.container1, text="CADASTRO - TURMA")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lblidturma = Label(self.container2, text="Código:", font=self.fonte, width=10)
        self.lblidturma.pack(side=LEFT)

        self.txtidturma = Entry(self.container2)
        self.txtidturma["width"] = 10
        self.txtidturma["font"] = self.fonte
        self.txtidturma.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarTurma
        self.btnBuscar.pack(side=RIGHT)

        self.lblcodigo_turma = Label(self.container3, text="Cód Turma:", font=self.fonte, width=10)
        self.lblcodigo_turma.pack(side=LEFT)

        self.txtcodigo_turma = Entry(self.container3)
        self.txtcodigo_turma["width"] = 25
        self.txtcodigo_turma["font"] = self.fonte
        self.txtcodigo_turma.pack(side=LEFT)

        self.lblperiodo = Label(self.container4, text="Período:", font=self.fonte, width=10)
        self.lblperiodo.pack(side=LEFT)

        self.txtperiodo = Entry(self.container4)
        self.txtperiodo["width"] = 25
        self.txtperiodo["font"] = self.fonte
        self.txtperiodo.pack(side=LEFT)

        self.lblcodigo_disciplina = Label(self.container5, text="Cód Disciplina:", font=self.fonte, width=10)
        self.lblcodigo_disciplina.pack(side=LEFT)

        self.txtcodigo_disciplina = Entry(self.container5)
        self.txtcodigo_disciplina["width"] = 20
        self.txtcodigo_disciplina["font"] = self.fonte
        self.txtcodigo_disciplina.pack(side=LEFT)

        self.lblcpf_professor = Label(self.container6, text="CPF Professor:", font=self.fonte, width=10)
        self.lblcpf_professor.pack(side=LEFT)

        self.txtcpf_professor = Entry(self.container6)
        self.txtcpf_professor["width"] = 20
        self.txtcpf_professor["font"] = self.fonte
        self.txtcpf_professor.pack(side=LEFT)

        self.lblcpf_aluno = Label(self.container7, text="CPF Aluno:", font=self.fonte, width=10)
        self.lblcpf_aluno.pack(side=LEFT)

        self.txtcpf_aluno = Entry(self.container7)
        self.txtcpf_aluno["width"] = 20
        self.txtcpf_aluno["font"] = self.fonte
        self.txtcpf_aluno.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirTurma
        self.bntInsert.pack(side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarTurma
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirTurma
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def inserirTurma(self):
        tur = Turma()

        tur.codigo_turma = self.txtcodigo_turma.get()
        tur.periodo = self.txtperiodo.get()
        tur.codigo_disciplina = self.txtcodigo_disciplina.get()
        tur.cpf_professor = self.txtcpf_professor.get()
        tur.cpf_aluno = self.txtcpf_aluno.get()

        self.lblmsg["text"] = tur.insertTurma()

        self.txtidturma.delete(0, END)
        self.txtcodigo_turma.delete(0, END)
        self.txtperiodo.delete(0, END)
        self.txtcodigo_disciplina.delete(0, END)
        self.txtcpf_professor.delete(0, END)
        self.txtcpf_aluno.delete(0, END)


    def alterarTurma(self):
        tur = Turma()

        tur.idturma = self.txtidturma.get()
        tur.codigo_turma = self.txtcodigo_turma.get()
        tur.periodo = self.txtperiodo.get()
        tur.codigo_disciplina = self.txtcodigo_disciplina.get()
        tur.cpf_professor = self.txtcpf_professor.get()
        tur.cpf_aluno = self.txtcpf_aluno.get()

        self.lblmsg["text"] = tur.insertTurma()

        self.txtidturma.delete(0, END)
        self.txtcodigo_turma.delete(0, END)
        self.txtperiodo.delete(0, END)
        self.txtcodigo_disciplina.delete(0, END)
        self.txtcpf_professor.delete(0, END)
        self.txtcpf_aluno.delete(0, END)

    def excluirTurma(self):
        tur = Turma()

        tur.idturma = self.txtidturma.get()

        self.lblmsg["text"] = tur.deleteTurma()

        self.txtidturma.delete(0, END)
        self.txtcodigo_turma.delete(0, END)
        self.txtperiodo.delete(0, END)
        self.txtcodigo_disciplina.delete(0, END)
        self.txtcpf_professor.delete(0, END)
        self.txtcpf_aluno.delete(0, END)

    def buscarTurma(self):
        tur = Turma()

        idturma = self.txtidturma.get()

        self.lblmsg["text"] = tur.selectTurma(idturma)

        self.txtidturma.delete(0, END)
        self.txtidturma.insert(INSERT, tur.idturma)

        self.txtcodigo_turma.delete(0, END)
        self.txtcodigo_turma.insert(INSERT, tur.codigo_turma)

        self.txtperiodo.delete(0, END)
        self.txtperiodo.insert(INSERT, tur.periodo)

        self.txtcodigo_disciplina.delete(0, END)
        self.txtcodigo_disciplina.insert(INSERT, tur.codigo_disciplina)

        self.txtcpf_professor.delete(0, END)
        self.txtcpf_professor.insert(INSERT, tur.cpf_professor)

        self.txtcpf_aluno.delete(0, END)
        self.txtcpf_aluno.insert(INSERT, tur.cpf_aluno)


root = Tk()
Application(root)
root.mainloop()
