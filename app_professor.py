from professor import Professor

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

        self.titulo = Label(self.container1, text="CADASTRO - PROFESSOR")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lblidprofessor = Label(self.container2, text="Código:", font=self.fonte, width=10)
        self.lblidprofessor.pack(side=LEFT)

        self.txtidprofessor = Entry(self.container2)
        self.txtidprofessor["width"] = 10
        self.txtidprofessor["font"] = self.fonte
        self.txtidprofessor.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarProfessor
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lblcpf = Label(self.container4, text="CPF:", font=self.fonte, width=10)
        self.lblcpf.pack(side=LEFT)

        self.txtcpf = Entry(self.container4)
        self.txtcpf["width"] = 25
        self.txtcpf["font"] = self.fonte
        self.txtcpf.pack(side=LEFT)

        self.lbldepartamento = Label(self.container5, text="Departamento:", font=self.fonte, width=10)
        self.lbldepartamento.pack(side=LEFT)

        self.txtdepartamento = Entry(self.container5)
        self.txtdepartamento["width"] = 20
        self.txtdepartamento["font"] = self.fonte
        self.txtdepartamento.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirProfessor
        self.bntInsert.pack(side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarProfessor
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirProfessor
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def inserirProfessor(self):
        prof = Professor()

        prof.nome = self.txtnome.get()
        prof.cpf = self.txtcpf.get()
        prof.departamento = self.txtdepartamento.get()

        self.lblmsg["text"] = prof.insertProfessor()

        self.txtidprofessor.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcpf.delete(0, END)
        self.txtdepartamento.delete(0, END)

    def alterarProfessor(self):
        prof = Professor()

        prof.idprofessor = self.txtidprofessor.get()
        prof.nome = self.txtnome.get()
        prof.cpf = self.txtcpf.get()
        prof.departamento = self.txtdepartamento.get()

        self.lblmsg["text"] = prof.updateProfessor

        self.txtidprofessor.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcpf.delete(0, END)
        self.txtdepartamento.delete(0, END)

    def excluirProfessor(self):
        prof = Professor()

        prof.idprofessor = self.txtidprofessor.get()

        self.lblmsg["text"] = prof.deleteProfessor()

        self.txtidprofessor.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcpf.delete(0, END)
        self.txtdepartamento.delete(0, END)

    def buscarProfessor(self):
        prof = Professor()

        idprofessor = self.txtidprofessor.get()

        self.lblmsg["text"] = prof.selectProfessor(idprofessor)

        self.txtidprofessor.delete(0, END)
        self.txtidprofessor.insert(INSERT, prof.idprofessor)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, prof.nome)

        self.txtcpf.delete(0, END)
        self.txtcpf.insert(INSERT, prof.cpf)

        self.txtdepartamento.delete(0, END)
        self.txtdepartamento.insert(INSERT, prof.departamento)


root = Tk()
Application(root)
root.mainloop()