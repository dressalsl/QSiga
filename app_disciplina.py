from disciplina import Disciplina

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
        self.container5["padx"] = 20
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

        self.titulo = Label(self.container1, text="CADASTRO - DISCIPLINA")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lbliddisciplina = Label(self.container2, text="Código:", font=self.fonte, width=10)
        self.lbliddisciplina.pack(side=LEFT)

        self.txtiddisciplina = Entry(self.container2)
        self.txtiddisciplina["width"] = 10
        self.txtiddisciplina["font"] = self.fonte
        self.txtiddisciplina.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarDisciplina
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Nome:", font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirDisciplina
        self.bntInsert.pack(side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarDisciplina
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirDisciplina
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def inserirDisciplina(self):
        disc = Disciplina()

        disc.nome = self.txtnome.get()

        self.lblmsg["text"] = disc.insertDisciplina()

        self.txtiddisciplina.delete(0, END)
        self.txtnome.delete(0, END)

    def alterarDisciplina(self):
        disc = Disciplina()

        disc.iddisciplina = self.txtiddisciplina.get()
        disc.nome = self.txtnome.get()

        self.lblmsg["text"] = disc.updateDisciplina()

        self.txtiddisciplina.delete(0, END)
        self.txtnome.delete(0, END)

    def excluirDisciplina(self):
        disc = Disciplina()

        disc.iddisciplina = self.txtiddisciplina.get()

        self.lblmsg["text"] = disc.deleteDisciplina()

        self.txtiddisciplina.delete(0, END)
        self.txtnome.delete(0, END)

    def buscarDisciplina(self):
        disc = Disciplina()

        iddisciplina = self.txtiddisciplina.get()

        self.lblmsg["text"] = disc.selectDisciplina(iddisciplina)

        self.txtiddisciplina.delete(0, END)
        self.txtiddisciplina.insert(INSERT, disc.iddisciplina)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, disc.nome)


root = Tk()
Application(root)
root.mainloop()