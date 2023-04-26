from tkinter import *
from main_interface import *

# Definição de Variáveis

login_var = False

# Funções


def obter_valor():
    username = username_camp.get()
    password = password_camp.get()
    if ((username == "gab") and (password == "123")):
        login_window.destroy()
        open_main_window()
    elif ((username == "") and (password == "")):
        text_login.set("Digite o usuário e senha")
    elif ((username != "") and (password == "")):
        text_login.set("Digite a senha")
    elif ((username == "") and (password != "")):
        text_login.set("Digite o usuário")
    else:
        text_login.set("Usuário ou senha incorretos")


# Início do programa
login_window = Tk()
login_window.title("SCC")
login_window.iconbitmap("Media/main_icon.ico")
login_window.geometry("195x135+560+200")
login_window.resizable(False, False)
login_window['bg'] = "#99ddff"

# Declaração de variáveis

text_login = StringVar()

cabecalho = Label(login_window,
                  text="Sistema de Cadastro\nde Clientes",
                  background="#99ddff")
cabecalho.grid(row=0, columnspan=2, sticky='we', padx=25)

username_name = Label(login_window,
                      text="Usuario: ",
                      background="#99ddff")
username_camp = Entry(login_window, width=20)

password_name = Label(login_window,
                      text="Senha: ",
                      background="#99ddff")
password_camp = Entry(login_window, show="*")

login_error = Label(login_window,
                    textvariable=text_login,
                    background="#99ddff",)

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
