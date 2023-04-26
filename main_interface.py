# Importação das bibliotecas
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from classes import *
from tkinter.tix import *
import sqlite3

# Classes e funções


# Banco de dados
bd_scc = gerar_bd()
bd_scc.connect_bd("BD_SCC.db")
bd_scc.createtable_bd("clientes", "cod INTEGER PRIMARY KEY, nome_cliente CHAR(40) NOT NULL, tel_cliente INTEGER(20), cid_cliente CHAR(40)")

# Criando a telas
def open_main_window():
    class funcs():
        def limpar_func(self):
            codigoe.delete(0, END)
            nomee.delete(0, END)
            cidadee.delete(0, END)
            telefonee.delete(0, END)
    
    main_window = new_window()
    main_window.build_window('SCC', '700x500+320+80', '#004d00', False)

# Definição dos Widgets
# Frames
    frame1 = Frame(main_window, bd=4, bg='#ccffb3',
               highlightbackground='#339900', highlightthickness=3)
    frame2 = Frame(main_window, bd=4, bg='#ccffb3',
               highlightbackground='#339900', highlightthickness=3)

# Botões
    buscab = Button(main_window, text="Buscar", bg='#339900',
                bd=2, fg="white", font=('verdana', 8, 'bold'))
    limpab = Button(main_window, text="Limpar", bg='#339900',
                bd=2, fg="white", font=('verdana', 8, 'bold'), command=lambda: funcs().limpar_func())
    novob = Button(main_window, text="Novo", bg='#339900',
               bd=2, fg="white", font=('verdana', 8, 'bold'))
    alterarb = Button(main_window, text="Alterar", bg='#339900',
                  bd=2, fg="white", font=('verdana', 8, 'bold'))
    apagarb = Button(main_window, text="Apagar", bg='#339900',
                 bd=2, fg="white", font=('verdana', 8, 'bold'))

# Labels
    codigol = Label(main_window, text="Código", bg='#ccffb3',
                fg="#339900", font=('verdana', 8, 'bold'))
    nomel = Label(main_window, text="Nome", bg='#ccffb3',
              fg="#339900", font=('verdana', 8, 'bold'))
    telefonel = Label(main_window, text="Telefone", bg='#ccffb3',
                  fg="#339900", font=('verdana', 8, 'bold'))
    cidadel = Label(main_window, text="Cidade", bg='#ccffb3',
                fg="#339900", font=('verdana', 8, 'bold'))

# Entrys
    codigoe = Entry(main_window)
    nomee = Entry(main_window)
    telefonee = Entry(main_window)
    cidadee = Entry(main_window)

# Treeview
    tv = ttk.Treeview(frame2, height=3, column=("col1","col2", "col3", "col4"))
    tv.heading("#0", text="")
    tv.heading("#1", text="Codigo")
    tv.heading("#2", text="Nome")
    tv.heading("#3", text="Telefone")
    tv.heading("#4", text="Cidade")

    tv.column("#0", width=1)
    tv.column("#1", width=40)
    tv.column("#2", width=220)
    tv.column("#3", width=125)
    tv.column("#4", width=125)

# Scrollbar
    scrollista = Scrollbar(frame2, orient="vertical")
    tv.configure(yscroll=scrollista.set)

# Posicionamento dos Widgets
# Frames
    frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
    frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

# Botões
    buscab.place(relx=0.3, rely=0.06)
    limpab.place(relx=0.408, rely=0.06)
    novob.place(relx=0.649, rely=0.06)
    alterarb.place(relx=0.743, rely=0.06)
    apagarb.place(relx=0.853, rely=0.06)

# Labels
    codigol.place(relx=0.05, rely=0.04)
    nomel.place(relx=0.05, rely=0.14)
    telefonel.place(relx=0.05, rely=0.24)
    cidadel.place(relx=0.05, rely=0.34)

# Entrys
    codigoe.place(relx=0.05, rely=0.08, relwidth=0.076)
    nomee.place(relx=0.05, rely=0.18, relwidth=0.3)
    telefonee.place(relx=0.05, rely=0.28, relwidth=0.3)
    cidadee.place(relx=0.05, rely=0.38, relwidth=0.3)

# Treeview
    tv.place(relx=0.01, rely=0.01, relwidth=0.95, relheight=0.85)

# Scrollbar
    scrollista.place(relx=0.96, rely=0.01, relwidth=0.04, relheight=0.85)


# frame2.place_forget()

    bd_scc.disconnect_bd()
    main_window.mainloop()
