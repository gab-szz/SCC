from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from classes import *
from tkinter.tix import *
from sqlite3 import *
from main_interface import *

# Conectando ao banco de dados
bd_scc = gerar_bd()
bd_scc.connect_bd("BD_SCC.db")
conn = sqlite3.connect("BD_SCC.db")
cursor = conn.cursor()


# Criando tabela "user"
bd_scc.createtable_bd("user", 
                    "id_user INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome_user TEXT NOT NULL, senha_user VARCHAR(18) NOT NULL")

# Adicionando senha ao banco de dados
cursor.execute(""" 
INSERT INTO user (nome_user, senha_user) VALUES ('gab', '123')
""")
conn.commit()

cursor.execute("""SELECT nome_user FROM user WHERE id_user = 1""")
nome_user = cursor.fetchall()
cursor.execute("""SELECT senha_user FROM user WHERE id_user = 1""")
senha_user = cursor.fetchall()

# Função para fazer login

def obter_valor():
    app = Application()
    print("executado")
    username = username_camp.get()
    password = password_camp.get()
    if (username == "".join(nome_user[0])) and (password == "".join(senha_user[0])):
        login_window.destroy()
        app.open_main_window()
    elif ((username == "") and (password == "")):
        text_login.set("Digite o usuário e senha")
        login_window.destroy()
        app.open_main_window()
    elif ((username != "") and (password == "")):
        text_login.set("Digite a senha")
        login_window.destroy()
        app.open_main_window()
    elif ((username == "") and (password != "")):
        text_login.set("Digite o usuário")
        login_window.destroy()
        app.open_main_window()
    else:
        text_login.set("Usuário ou senha incorretos")
        login_window.destroy()
        app.open_main_window()

# Inicio do Programa


login_window = new_window()


login_window.build_window('SCC', '245x150+515+200', '#004d00', False)

text_login = StringVar()

# Criação dos widgets

cabecalho = Label(login_window,
                  text="Sistema de Cadastro\nde Clientes",
                  background="#004d00",
                  fg="#ffffff")
username_name = Label(login_window,
                      text="Usuario: ",
                      background="#004d00",
                      fg="#ffffff")
username_camp = Entry(login_window, width=20)
password_name = Label(login_window,
                      text="Senha: ",
                      background="#004d00",
                      fg="#ffffff")
password_camp = Entry(login_window, show="*")
login_error = Label(login_window,
                    textvariable=text_login,
                    background="#004d00",
                    fg="#ffffff")

# Organização dos widgets
cabecalho.grid(row=0, columnspan=2, sticky='we', padx=25)
username_name.grid(row=1, column=0, padx=5)
username_camp.grid(row=1, column=1)

password_name.grid(row=2, column=0)
password_camp.grid(row=2, column=1)

login_error.grid(row=3, columnspan=2)

login_button = Button(login_window, text="Login",
                      command=obter_valor).grid(row=4,
                                                columnspan=2,
                                                sticky='we',
                                                padx=15)

username_camp.focus()  # Deixa pronto para digitar no campo

login_window.mainloop()
