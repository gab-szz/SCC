# Programa para cadastro de clientes e fornecedores

# Importing libraries
from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter import messagebox
import os
import sqlite3
import pandas as pd

# Variables
v = "clientes"

conn = sqlite3.connect("BD_code.db")
cursor = conn.cursor()

# Functions

#  Creating a new screen
def tela_dois():
    tela_principal2 = Tk()
    tela_principal2.title = "SCC"
    tela_principal2.geometry("250x250+320+80")
    tela_principal2.configure(background='#0086b3')
    tela_principal2.resizable(width=True, height=True)
    tela_principal2.transient(tela_principal)
    tela_principal2.focus_force()
    tela_principal2.grab_set()

#  Import the DB datas and insert them to the TreeView
def select_lista(nome_aba):
    global v
    if nome_aba == "clientes": v = "clientes"
    if nome_aba == "fornecedores": v = "fornecedores"
    tv.delete(*tv.get_children())
    conn = sqlite3.connect("BD_code.db")
    cursor = conn.cursor()
    lista = cursor.execute(f""" SELECT cpf, nome, telefone, cidade, estado_civil FROM {nome_aba}
        ORDER BY nome ASC; """)
    for i in lista:
        tv.insert("", END, values=i)
    conn.close()

#  Format the CPF camp
def formatar_cpf(event = None):
    
    text = en_cpf.get().replace(".", "").replace("-", "")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace": return
    
    for index in range(len(text)):
        
        if not text[index] in "0123456789": continue
        if index in [2, 5]: new_text += text[index] + "."
        elif index == 8: new_text += text[index] + "-"
        else: new_text += text[index]

    en_cpf.delete(0, "end")
    en_cpf.insert(0, new_text)
    
    text2 = en_cpf2.get().replace(".", "").replace("-", "")[:11]
    new_text2 = ""

    if event.keysym.lower() == "backspace": return
    
    for index2 in range(len(text2)):
        
        if not text2[index2] in "0123456789": continue
        if index2 in [2, 5]: new_text2 += text2[index2] + "."
        elif index2 == 8: new_text2 += text2[index2] + "-"
        else: new_text2 += text2[index2]

    en_cpf2.delete(0, "end")
    en_cpf2.insert(0, new_text2)

#  Format the phone number camp
def formatar_telefone(event = None):
    
    text = en_telefone.get().replace("(", "").replace(")","")[:11]
    new_text = ""

    if event.keysym.lower() == "backspace": return
    
    for index in range(len(text)):
        
        if not text[index] in "0123456789": continue
        if index == 0: new_text +=  "(" + text[index] 
        elif index == 1: new_text += text[index] + ")"
        else: new_text += text[index]

    en_telefone.delete(0, "end")
    en_telefone.insert(0, new_text)

    
    text2 = en_telefone2.get().replace("(", "").replace(")","")[:11]
    new_text2 = ""

    if event.keysym.lower() == "backspace": return
    
    for index in range(len(text2)):
        
        if not text2[index] in "0123456789": continue
        if index == 0: new_text2 +=  "(" + text2[index] 
        elif index == 1: new_text2 += text2[index] + ")"
        else: new_text2 += text2[index]

    en_telefone2.delete(0, "end")
    en_telefone2.insert(0, new_text2)
    
#  Get the text in the cpf camp
def obter_cpf(nome_aba):
    if nome_aba == "clientes": t = en_cpf.get()
    elif nome_aba == "fornecedores": t = en_cpf2.get()
    tt = t.split(".")
    ttt = tt[2].split("-")
    full = tt[0] + tt[1] + ttt[0] + ttt[1]
    return full

#  Get the phone number in the cpf camp
def obter_telefone(nome_aba):
    if nome_aba == "clientes": t = en_telefone.get()
    elif nome_aba == "fornecedores": t = en_telefone2.get()
    tt = t.split("(")
    ttt = tt[1].split(")")
    full = ttt[0] + ttt[1]
    return full

#  Clear the texts of all camps
def limpa_pessoa(nome_aba):
    if nome_aba == "clientes":
        en_cpf.delete(0, "end")
        en_nome.delete(0, "end")
        en_telefone.delete(0, "end")
        en_cidade.delete(0, "end")
    elif nome_aba == "fornecedores":
        en_cpf2.delete(0, "end")
        en_nome2.delete(0, "end")
        en_telefone2.delete(0, "end")
        en_cidade2.delete(0, "end")
    
#  Add a new person
def adicionar_pessoa(nome_aba):
    conn = sqlite3.connect("BD_code.db")
    cursor = conn.cursor()
    if nome_aba == "clientes":
        if en_nome.get() == "":
            msg = "Para cadastrar o novo cliente, é necessário\nque seja digitado ao menos um nome"
            messagebox.showinfo("Aviso", msg)
        elif en_nome.get() == " ":
            msg = "Para cadastrar o novo cliente, é necessário\nque seja digitado ao menos um nome"
            messagebox.showinfo("Aviso", msg)
        else:
            cursor.execute("INSERT INTO clientes (cpf, nome, telefone, cidade, estado_civil) VALUES (?, ?, ?, ?, ?)", (en_cpf.get(), en_nome.get(), en_telefone.get(), en_cidade.get(), TipVar.get()))
            conn.commit()
            limpa_pessoa("clientes")
            select_lista("clientes")
    elif nome_aba == "fornecedores":
        if en_nome2.get() == "":
            msg = "Para cadastrar o novo fornecedor, é necessário\nque seja digitado ao menos um nome"
            messagebox.showinfo("Aviso", msg)
        elif en_nome2.get() == " ":
            msg = "Para cadastrar o novo fornecedor, é necessário\nque seja digitado ao menos um nome"
            messagebox.showinfo("Aviso", msg)
        else:
            cursor.execute("INSERT INTO fornecedores (cpf, nome, telefone, cidade, estado_civil) VALUES (?, ?, ?, ?, ?)", (en_cpf2.get(), en_nome2.get(), en_telefone2.get(), en_cidade2.get(), TipVar2.get()))
            conn.commit()
            limpa_pessoa("fornecedores")
            select_lista("fornecedores")
    conn.close()
        
#  Remove an person
def deleta_pessoa(nome_aba):
    conn = sqlite3.connect("BD_code.db")
    cursor = conn.cursor()
    if nome_aba == "clientes": cursor.execute("""DELETE FROM clientes WHERE cpf =?""", (en_cpf.get(),))
    elif nome_aba == "fornecedores": cursor.execute("""DELETE FROM fornecedores WHERE cpf =?""", (en_cpf.get(),))
    conn.commit()
    conn.close()
    select_lista(nome_aba)
    limpa_pessoa(nome_aba)
    
#  Adjust the window resolution
def resolucao():
    if (bt_abrirf2["text"] == "Abrir lista"):
            tela_principal.geometry("800x600")
            frame_1.place(relx=0.02, rely=0.01, relwidth=0.96, relheight=0.46)
            frame_2.place(relx=0.02, rely=0.50, relwidth=0.96, relheight=0.48)
            bt_abrirf2["text"] = "Fechar lista"
            bt_abrirf3["text"] = "Fechar lista"
            
    elif(bt_abrirf2["text"] == "Fechar lista"):
            tela_principal.geometry("800x300")
            frame_2.place_forget()
            frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.92)
            bt_abrirf2["text"] = "Abrir lista"
            bt_abrirf3["text"] = "Abrir lista"
    
#  Carry data on double click
def OnDoubleClick(event):
    
    tv.selection()
    global v
    if v == "clientes":
        limpa_pessoa("clientes")
        for n in tv.selection():
            col1, col2, col3, col4, col5 = tv.item(n, 'values')
            en_cpf.insert(END, col1)
            en_nome.insert(END, col2)
            en_telefone.insert(END, col3)
            en_cidade.insert(END, col4)
            
            if (col5 == "Solteiro(a)"):
                TipVar.set(TipV[0])
            elif (col5 == "Casado(a)"):
                TipVar.set(TipV[1])
            elif (col5 == "Divorciado(a)"):
                TipVar.set(TipV[2])
            elif (col5 == "Viúvo(a)"):
                TipVar.set(TipV[3])
    elif v == "fornecedores": 
        limpa_pessoa("fornecedores")
        for n in tv.selection():
            col1, col2, col3, col4, col5 = tv.item(n, 'values')
            en_cpf2.insert(END, col1)
            en_nome2.insert(END, col2)
            en_telefone2.insert(END, col3)
            en_cidade2.insert(END, col4)
            
            if (col5 == "Solteiro(a)"):
                TipVar.set(TipV[0])
            elif (col5 == "Casado(a)"):
                TipVar.set(TipV[1])
            elif (col5 == "Divorciado(a)"):
                TipVar.set(TipV[2])
            elif (col5 == "Viúvo(a)"):
                TipVar.set(TipV[3])
            
def altera_pessoa(nome_aba):
    conn = sqlite3.connect("BD_code.db")
    cursor = conn.cursor()
    if nome_aba == "clientes": cursor.execute(""" UPDATE clientes SET cpf =?, nome =?, telefone =?, cidade =?, estado_civil =? WHERE cpf =?""", (en_cpf.get(), en_nome.get(), en_telefone.get(), en_cidade.get(), TipVar.get(), en_cpf.get())) 
    elif nome_aba == "fornecedores": cursor.execute(""" UPDATE fornecedores SET cpf =?, nome =?, telefone =?, cidade =?, estado_civil =? WHERE cpf =?""", (en_cpf2.get(), en_nome2.get(), en_telefone2.get(), en_cidade2.get(), TipVar2.get(), en_cpf2.get()))
    conn.commit()
    conn.close()
    select_lista(nome_aba)
    limpa_pessoa(nome_aba)
    
def busca_pessoa(nome_aba):
    conn = sqlite3.connect("BD_code.db")
    cursor = conn.cursor()
    
    tv.delete(*tv.get_children())
    en_nome.insert(END, '%')
    if nome_aba == "clientes": cursor.execute(""" SELECT cpf, nome, telefone, cidade, estado_civil FROM clientes WHERE nome LIKE '%s' ORDER BY nome ASC""" % en_nome.get())
    elif nome_aba == "fornecedores": cursor.execute(""" SELECT cpf, nome, telefone, cidade, estado_civil FROM fornecedores WHERE nome LIKE '%s' ORDER BY nome ASC""" % en_nome2.get())
    buscanomeCli = cursor.fetchall()
    
    for i in (buscanomeCli):
        tv.insert("", END, values=i)
        
    limpa_pessoa(nome_aba)
    conn.close()
    
def atualiza_lista(event):
    var = "none"
    global v
    numTab = str(abas.index(abas.select()))
    print(numTab)
    if numTab == "0": var = "clientes"; v = "clientes"; print(v)
    if numTab == "1": var = "fornecedores"; v = "fornecedores"; print(v)
    tv.delete(*tv.get_children())
    conn = sqlite3.connect("BD_code.db")
    cursor = conn.cursor()
    lista = cursor.execute(f""" SELECT cpf, nome, telefone, cidade, estado_civil FROM {var}
        ORDER BY nome ASC; """)
    for i in lista:
        tv.insert("", END, values=i)
    conn.close()
    
def gerar_tabela():
    conn = sqlite3.connect("BD_code.db")
    cursor = conn.cursor()
    
    dirname = "relatorios"
    if os.path.isdir(dirname) == False:
        os.mkdir(dirname)
        print("The directory is created.")
    else:
        print("The directory already exists.")
    
    cursor.execute(''' SELECT * FROM clientes ''')
    bd_dados = pd.DataFrame(cursor.fetchall())
    bd_dados.to_excel('relatorios/clientes.xlsx')
    bd_dados = pd.read_sql_query ('''
                               SELECT
                               *
                               FROM fornecedores
                               ''', conn)
    bd_dados.to_excel('relatorios/fornecedores.xlsx')
    

# Execução do Aplicativo\
#  - Inicia o a tela principal
tela_principal = tix.Tk()
tela_principal.title = "Sistema de Cadastro de Clientes"
tela_principal.geometry("800x300+270+20")
tela_principal.configure(background='#0086b3')
tela_principal.resizable(width=True, height=True)

# Barra de Menu

menubar = Menu(tela_principal)
tela_principal.config(menu=menubar)
filemenu = Menu(menubar)

menubar.add_cascade(label="Opções", menu=filemenu)
filemenu.add_command(label="Gerar relatorio", command=gerar_tabela)
filemenu.add_command(label="Sair", command=tela_principal.destroy)


# Criação e Posicionamento dos Frames
#  - Primeiro Frame
frame_1 = Frame(tela_principal, width=300, height=300, bg='#b3d9ff', highlightthickness=2)
frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.92)
        
#  - Segundo Frame
frame_2 = Frame(tela_principal, width=300, height=300, bg='#b3d9ff', highlightthickness=2)

# Posicionando os Widgets
# - Widgets do Primeiro Frame

# - Abas
abas = ttk.Notebook(frame_1)

aba_clientes = Frame(abas)
aba_fornecedores = Frame(abas)
aba_clientes.configure(background='lightgray')

abas.add(aba_clientes, text='Clientes')
abas.add(aba_fornecedores, text='Fornecedores')
abas.place(relx=0.00, rely=0.00, relwidth=1, relheight=1)

# Aba clientes
# Labels

lb_cpf = Label(aba_clientes, text="CPF", bg='lightgray', fg="#004080", font=('verdana', 10, 'bold'))
lb_cpf.place(relx= 0.025, rely= 0.05)

lb_nome = Label(aba_clientes, text="Nome", bg='lightgray', fg="#004080", font=('verdana', 10, 'bold'))
lb_nome.place(relx=0.025, rely=0.35)

lb_telefone = Label(aba_clientes, text="Telefone", bg='lightgray', fg="#004080", font=('verdana', 10, 'bold'))
lb_telefone.place(relx=0.025, rely=0.6)

lb_cidade = Label(aba_clientes, text="Cidade", bg='lightgray', fg="#004080", font=('verdana', 10, 'bold'))
lb_cidade.place(relx=0.22, rely=0.6)

lb_estadoCivil = Label(aba_clientes, text="Estado\nCivil:", bg='lightgray', fg="#004080", font=('verdana', 10, 'bold'))
lb_estadoCivil.place(relx=0.060, rely=0.815)
        
# Entrys

en_cpf = Entry(aba_clientes)
en_cpf.bind("<KeyRelease>", formatar_cpf)
en_cpf.place(relx= 0.025, rely= 0.15, relwidth= 0.162)

en_nome = Entry(aba_clientes)
en_nome.place(relx=0.025, rely=0.45, relwidth=0.48)

en_telefone = Entry(aba_clientes)
en_telefone.bind("<KeyRelease>", formatar_telefone)
en_telefone.place(relx=0.025, rely=0.7, relwidth=0.162)

en_cidade = Entry(aba_clientes)
en_cidade.place(relx=0.22, rely=0.7, relwidth=0.285)

#en_data = Entry(aba_clientes)
#en_data.place(relx=0.52, rely=0.45, relwidth=0.15)

# Drop Down Button

TipVar = StringVar(aba_clientes)
TipV = ("Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viúvo(a)")
TipVar.set(TipV[0])
popupMenu = OptionMenu(aba_clientes,TipVar, *TipV)
popupMenu.place(relx=0.15, rely=0.825, relwidth=0.20)

# Criando os botões e balões

bt_limpa = Button(aba_clientes, text="Limpar", bg='#004080', bd=2, fg="white", font=('verdana', 8, 'bold'), command=lambda: limpa_pessoa("clientes"))
bt_limpa.place(relx= 0.25, rely=0.1, relwidth=0.1, relheight= 0.15)

bl_limpa = tix.Balloon(aba_clientes)
bl_limpa.subwidget('label')['image'] = BitmapImage()
bl_limpa.bind_widget(bt_limpa, balloonmsg="Limpa todos os campos")

bt_busca = Button(aba_clientes, text="Buscar", bg='#004080', bd=2, fg="white", font=('verdana', 8, 'bold'), command=lambda: busca_pessoa("clientes"))
bt_busca.place(relx=0.35, rely=0.1, relwidth=0.1, relheight=0.15)

bt_novo = Button(aba_clientes, text="Novo", bg='#004080', bd=2, fg="white", font=('verdana', 8, 'bold'), command=lambda: adicionar_pessoa("clientes"))
bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
bt_alterar = Button(aba_clientes, text="Alterar", bg='#004080', bd=2, fg="white", font=('verdana', 8, 'bold'), command=lambda: altera_pessoa("clientes"))
bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

bt_apagar = Button(aba_clientes, text="Deletar", bg='#004080', bd=2, fg="white", font=('verdana', 8, 'bold'), command=lambda: deleta_pessoa("clientes"))
bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

bt_abrirf2 = Button(aba_clientes, text="Abrir lista", bg='#004080', bd=2, fg="white", font=('verdana', 8, 'bold'), command=lambda: resolucao())
bt_abrirf2.place(relx=0.86, rely=0.84, relwidth=0.14, relheight=0.15)


# Aba Fornecedores
# Labels

lb_cpf2 = Label(aba_fornecedores, text="CPF", bg='lightgray', fg="#004080", font=('verdana', 10, 'bold'))
lb_cpf2.place(relx= 0.025, rely= 0.05)

lb_nome2 = Label(aba_fornecedores, text="Nome", bg='lightgray', fg="#004080", font=('verdana', 10, 'bold'))
lb_nome2.place(relx=0.025, rely=0.35)

lb_telefone2 = Label(aba_fornecedores, text="Telefone", bg='lightgray', fg="#004080", font=('verdana', 10, 'bold'))
lb_telefone2.place(relx=0.025, rely=0.6)

lb_cidade2 = Label(aba_fornecedores, text="Cidade", bg='lightgray', fg="#004080", font=('verdana', 10, 'bold'))
lb_cidade2.place(relx=0.22, rely=0.6)

lb_estadoCivil2 = Label(aba_fornecedores, text="Estado\nCivil:", bg='lightgray', fg="#004080", font=('verdana', 10, 'bold'))
lb_estadoCivil2.place(relx=0.060, rely=0.815)
        
# Entrys

en_cpf2 = Entry(aba_fornecedores)
en_cpf2.bind("<KeyRelease>", formatar_cpf)
en_cpf2.place(relx= 0.025, rely= 0.15, relwidth= 0.162)

en_nome2 = Entry(aba_fornecedores)
en_nome2.place(relx=0.025, rely=0.45, relwidth=0.48)

en_telefone2 = Entry(aba_fornecedores)
en_telefone2.bind("<KeyRelease>", formatar_telefone)
en_telefone2.place(relx=0.025, rely=0.7, relwidth=0.162)

en_cidade2 = Entry(aba_fornecedores)
en_cidade2.place(relx=0.22, rely=0.7, relwidth=0.285)

#en_data2 = Entry(aba_fornecedores)
#en_data2.place(relx=0.52, rely=0.45, relwidth=0.15)

# Drop Down Button

TipVar2 = StringVar(aba_fornecedores)
TipV2 = ("Solteiro(a)", "Casado(a)", "Divorciado(a)", "Viúvo(a)")
TipVar2.set(TipV2[0])
popupMenu2 = OptionMenu(aba_fornecedores,TipVar, *TipV)
popupMenu2.place(relx=0.15, rely=0.825, relwidth=0.20)

# Criando os botões e balões

bt_limpa2 = Button(aba_fornecedores, text="Limpar", bg='#004080', bd=2, fg="white", font=('verdana', 8, 'bold'), command=lambda: limpa_pessoa("fornecedores"))
bt_limpa2.place(relx= 0.25, rely=0.1, relwidth=0.1, relheight= 0.15)

bl_limpa2 = tix.Balloon(aba_fornecedores)
bl_limpa2.subwidget('label')['image'] = BitmapImage()
bl_limpa2.bind_widget(bt_limpa, balloonmsg="Limpa todos os campos")

bt_busca2 = Button(aba_fornecedores, text="Buscar", bg='#004080', bd=2, fg="white", font=('verdana', 8, 'bold'), command=lambda: busca_pessoa("fornecedores"))
bt_busca2.place(relx=0.35, rely=0.1, relwidth=0.1, relheight=0.15)

bt_novo2 = Button(aba_fornecedores, text="Novo", bg='#004080', bd=2, fg="white", font=('verdana', 8, 'bold'), command=lambda: adicionar_pessoa("fornecedores"))
bt_novo2.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
bt_alterar2 = Button(aba_fornecedores, text="Alterar", bg='#004080', bd=2, fg="white", font=('verdana', 8, 'bold'), command=lambda: altera_pessoa("fornecedores"))
bt_alterar2.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)

bt_apagar2 = Button(aba_fornecedores, text="Deletar", bg='#004080', bd=2, fg="white", font=('verdana', 8, 'bold'), command=lambda: deleta_pessoa("fornecedores"))
bt_apagar2.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)

bt_abrirf3 = Button(aba_fornecedores, text="Abrir lista", bg='#004080', bd=2, fg="white", font=('verdana', 8, 'bold'), command=lambda: resolucao())
bt_abrirf3.place(relx=0.86, rely=0.84, relwidth=0.14, relheight=0.15)

# - Widgets do Segundo Frame
# - Treeview
tv = ttk.Treeview(frame_2, height=2, column=("col1", "col2", "col3", "col4", "col5"))

# - Textos das colunas
tv.heading("#0", text="")
tv.heading("#1", text="CPF")
tv.heading("#2", text="Nome")
tv.heading("#3", text="Telefone")
tv.heading("#4", text="Cidade")
tv.heading("#5", text="Estado Civil")

# - Tamanho das colunas
tv.column("#0", width=1)
tv.column("#1", width=100)
tv.column("#2", width=200)
tv.column("#3", width=120)
tv.column("#4", width=100)
tv.column("#5", width=125)
tv.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)
#Chamando o evento de puxar os dados ao clicar na linha
tv.bind('<Double-1>', OnDoubleClick)
abas.bind('<<NotebookTabChanged>>', atualiza_lista)

# - Scrollbar
scroolLista = Scrollbar(frame_2, orient="vertical")
tv.configure(yscroll=scroolLista.set)
scroolLista.place(relx=0.96, rely=0.1, relwidth=0.025, relheight=0.89)

select_lista("clientes")

tela_principal.mainloop()