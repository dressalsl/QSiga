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


        #nome dos botoes, tipo de fonte

        self.tituloqsiga = Label(self.container1, text="╰☆╮ QSIGA 2.0 ╰☆╮")
        self.tituloqsiga["font"] = ("Calibri", "10", "bold")
        self.tituloqsiga.pack()

        self.titulo = Label(self.container1, text="MENU")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.btnprofessor = Button(self.container2, text="Professor", font=self.fonte, width=10)
        self.btnprofessor.pack(side=LEFT)

        self.btndisciplina = Button(self.container3, text="Disciplina", font=self.fonte, width=10)
        self.btndisciplina.pack(side=LEFT)

        self.btnaluno = Button(self.container4, text="Aluno", font=self.fonte, width=10)
        self.btnaluno.pack(side=LEFT)

        self.btnturma = Button(self.container5, text="Turma", font=self.fonte, width=10)
        self.btnturma.pack(side=LEFT)

        self.btnsair = Button(self.container7, text="Sair", font=self.fonte, width=10)
        self.btnsair.pack(side=RIGHT)






root = Tk()
Application(root)
root.mainloop()