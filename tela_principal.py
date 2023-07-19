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
# connect to database
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
def selecionar_lista(nome_aba):
    # Calling the global variable v
    global v
    if nome_aba == "clientes": v = "clientes"
    if nome_aba == "fornecedores": v = "fornecedores"
    # Clear all items of TreeView
    tv.delete(*tv.get_children())
    # connect to database
    conn = sqlite3.connect("BD_code.db")
    cursor = conn.cursor()
    lista = cursor.execute(f""" SELECT cpf, nome, telefone, cidade, estado_civil FROM {nome_aba}
        ORDER BY nome ASC; """)
    # Insert the datas in the TreeView
    for i in lista:
        tv.insert("", END, values=i)
    # disconnect from database
    conn.close()

#  Format the CPF camp
def formatar_cpf(event = None):
    # Format the CPF camp in "clientes"
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
    # Format the CPF camp in "fornecedores"
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
    #  Format the phone in "clientes"
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

    # Format the phone in "fornecedores"
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
    # remove the punctuation of the text and return it
    tt = t.split(".")
    ttt = tt[2].split("-")
    full = tt[0] + tt[1] + ttt[0] + ttt[1]
    return full

#  Get the phone number in the cpf camp
def obter_telefone(nome_aba):
    if nome_aba == "clientes": t = en_telefone.get()
    elif nome_aba == "fornecedores": t = en_telefone2.get()
    # remove the punctuation of the text and return it
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
    # connect to database
    conn = sqlite3.connect("BD_code.db")
    cursor = conn.cursor()

    if nome_aba == "clientes":
        # If it has one or more empty fields
        if en_nome.get() == "" or en_cpf.get() == "" or en_cidade.get() == "" or en_telefone.get() == "":
            msg = "Há um ou mais campos vazios!"
            messagebox.showinfo("Aviso", msg)
        elif en_nome.get() == " " or en_cpf.get() == " " or en_cidade.get() == " " or en_telefone.get() == " ":
            msg = "Há um ou mais campos vazios!"
            messagebox.showinfo("Aviso", msg)
        # If it has no one empty field
        else:
            cursor.execute("INSERT INTO clientes (cpf, nome, telefone, cidade, estado_civil) VALUES (?, ?, ?, ?, ?)", (en_cpf.get(), en_nome.get(), en_telefone.get(), en_cidade.get(), TipVar.get()))
            conn.commit()
            limpa_pessoa("clientes")
            selecionar_lista("clientes")

    elif nome_aba == "fornecedores":
        # If it has one or more empty fields
        if en_nome2.get() == "" or en_cpf2.get() == "" or en_cidade2.get() == "" or en_telefone2.get() == "":
            msg = "Para cadastrar o novo fornecedor, é necessário\nque seja digitado ao menos um nome"
            messagebox.showinfo("Aviso", msg)
        # If it has no one empty field
        elif en_nome2.get() == " " or en_cpf2.get() == " " or en_cidade2.get() == " " or en_telefone2.get() == " ":
            msg = "Para cadastrar o novo fornecedor, é necessário\nque seja digitado ao menos um nome"
            messagebox.showinfo("Aviso", msg)
        else:
            cursor.execute("INSERT INTO fornecedores (cpf, nome, telefone, cidade, estado_civil) VALUES (?, ?, ?, ?, ?)", (en_cpf2.get(), en_nome2.get(), en_telefone2.get(), en_cidade2.get(), TipVar2.get()))
            conn.commit()
            limpa_pessoa("fornecedores")
            selecionar_lista("fornecedores")
    conn.close()  # Disconnect from database
        
#  Remove an person
def deleta_pessoa(nome_aba):
    # Connect to database
    conn = sqlite3.connect("BD_code.db")
    cursor = conn.cursor()

    if nome_aba == "clientes": cursor.execute("""DELETE FROM clientes WHERE cpf =?""", (en_cpf.get(),))
    elif nome_aba == "fornecedores": cursor.execute("""DELETE FROM fornecedores WHERE cpf =?""", (en_cpf2.get(),))
    
    conn.commit() # Save changes on database
    conn.close() # Disconnect from database
    selecionar_lista(nome_aba)
    limpa_pessoa(nome_aba)
    
#  Adjust the window resolution
def resolucao():
    # Increase the window height and show the frame_2
    if (bt_abrirf2["text"] == "Abrir lista"):
            tela_principal.geometry("800x600")
            frame_1.place(relx=0.02, rely=0.01, relwidth=0.96, relheight=0.46)
            frame_2.place(relx=0.02, rely=0.50, relwidth=0.96, relheight=0.48)
            bt_abrirf2["text"] = "Fechar lista"
            bt_abrirf3["text"] = "Fechar lista"
            bl_limpa.bind_widget(bt_abrirf2, balloonmsg="Fechar lista com os dados dos clientes")
            bl_limpa.bind_widget(bt_abrirf3, balloonmsg="Fechar lista com os dados dos clientes")
    # Decreases the window height and hide the frame_2        
    elif(bt_abrirf2["text"] == "Fechar lista"):
            tela_principal.geometry("800x300")
            frame_2.place_forget()
            frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.92)
            bt_abrirf2["text"] = "Abrir lista"
            bt_abrirf3["text"] = "Abrir lista"
            bl_limpa.bind_widget(bt_abrirf2, balloonmsg="Abrir lista com os dados dos clientes")
            bl_limpa.bind_widget(bt_abrirf3, balloonmsg="Abrir lista com os dados dos clientes")
    
#  Carry data on double click
def OnDoubleClick(event):
    tv.selection() # Return the tuple of selected items
    
    global v # Import the global variable "v" to use it in the function
    if v == "clientes":
        limpa_pessoa("clientes")
        
        # Read all items in TreeView and insert into the text boxes
        for n in tv.selection(): # "n" is the ID of the selected item
            col1, col2, col3, col4, col5 = tv.item(n, 'values') # "values" is a tuple with the values of the selected item
            en_cpf.insert(END, col1)
            en_nome.insert(END, col2)
            en_telefone.insert(END, col3)
            en_cidade.insert(END, col4)
            TipVar.set(col5)
    
    elif v == "fornecedores": 
        limpa_pessoa("fornecedores")
        
        # Read all items in TreeView and insert into the text boxes
        for n in tv.selection(): # "n" is the ID of the selected item
            col1, col2, col3, col4, col5 = tv.item(n, 'values') # "values" is a tuple with the values of the selected item
            en_cpf2.insert(END, col1)
            en_nome2.insert(END, col2)
            en_telefone2.insert(END, col3)
            en_cidade2.insert(END, col4)
            TipVar2.set(col5)
            
#  Change a data in the database
def altera_pessoa(nome_aba):
    # Connect to database
    conn = sqlite3.connect("BD_code.db")
    cursor = conn.cursor()
    # Update data in database
    if nome_aba == "clientes": cursor.execute(""" UPDATE clientes SET cpf =?, nome =?, telefone =?, cidade =?, estado_civil =? WHERE cpf =?""", (en_cpf.get(), en_nome.get(), en_telefone.get(), en_cidade.get(), TipVar.get(), en_cpf.get())) 
    elif nome_aba == "fornecedores": cursor.execute(""" UPDATE fornecedores SET cpf =?, nome =?, telefone =?, cidade =?, estado_civil =? WHERE cpf =?""", (en_cpf2.get(), en_nome2.get(), en_telefone2.get(), en_cidade2.get(), TipVar2.get(), en_cpf2.get()))
    conn.commit() # Save changes on database
    conn.close() # Disconnect from database
    selecionar_lista(nome_aba)
    limpa_pessoa(nome_aba)
    
#  Find a person in the database by name
def busca_pessoa(nome_aba):
    # Connect to database
    conn = sqlite3.connect("BD_code.db")
    cursor = conn.cursor()
    # Clear all items in TreeView
    tv.delete(*tv.get_children())
    # If have no text in the entry, show all items in the database
    en_nome.insert(END, '%')
    
    # Execute the query
    if nome_aba == "clientes": cursor.execute(""" SELECT cpf, nome, telefone, cidade, estado_civil FROM clientes WHERE nome LIKE '%s' ORDER BY nome ASC""" % en_nome.get())
    elif nome_aba == "fornecedores": cursor.execute(""" SELECT cpf, nome, telefone, cidade, estado_civil FROM fornecedores WHERE nome LIKE '%s' ORDER BY nome ASC""" % en_nome2.get())
    buscanomeCli = cursor.fetchall()
    
    for i in (buscanomeCli):
        tv.insert("", END, values=i)
        
    limpa_pessoa(nome_aba)
    conn.close() # Disconnect from database
    
def atualiza_lista(event):
    global v
    # Fet the number of the tab
    numTab = str(abas.index(abas.select()))
    if numTab == "0": v = "clientes"
    if numTab == "1": v = "fornecedores"
    tv.delete(*tv.get_children())
    conn = sqlite3.connect("BD_code.db")
    cursor = conn.cursor()
    lista = cursor.execute(f""" SELECT cpf, nome, telefone, cidade, estado_civil FROM {v}
        ORDER BY nome ASC; """)
    for i in lista:
        tv.insert("", END, values=i)
    conn.close()
    

def gerar_tabela():
    conn = sqlite3.connect("BD_code.db")
    cursor = conn.cursor()
    
    #  Check if the directory exists
    dirname = "relatorios"
    if os.path.isdir(dirname) == False:
        os.mkdir(dirname) # Create a new directory
        print("The directory is created.")
    else:
        print("The directory already exists.")
    
    #  Create the worksheet with data
    i = 0
    while i<2:
        table_bd = "table" # Var to store the table name
        if i == 0: table_bd = "clientes"
        elif i == 1: table_bd = "fornecedores"
        # Read data from sql database
        bd_dados = pd.read_sql_query (f''' SELECT * FROM {table_bd}''', conn)
        # Save the data in a excel file
        writer = pd.ExcelWriter(f'relatorios/{table_bd}.xlsx') 
        bd_dados.to_excel(writer, sheet_name='sheetName', index=False, na_rep='NaN')
        print(bd_dados)

        # Adjust the columns width
        for column in bd_dados.columns:
            column_length = max(bd_dados[column].astype(str).map(len).max(), len(column))
            col_idx = bd_dados.columns.get_loc(column)
            writer.sheets['sheetName'].set_column(col_idx, col_idx, column_length)
        
        writer.close() # Close and save the excel file
        i = i + 1

# Execução do Aplicativo\
#  - Inicia o a tela principal
tela_principal = tix.Tk()
tela_principal.title = "Sistema de Cadastro de Clientes"
tela_principal.geometry("800x300+270+20")
tela_principal.configure(background='#0086b3')
tela_principal.resizable(width=True, height=True)

#  Menu Bar
# Create the menu
menubar = Menu(tela_principal)
tela_principal.config(menu=menubar)

# Option cascade menu
filemenu = Menu(menubar)
menubar.add_cascade(label="Opções", menu=filemenu)
filemenu.add_command(label="Sair", command=tela_principal.destroy)

# Report cascade menu
reportmenu = Menu(menubar)
menubar.add_cascade(label="Relatórios", menu=reportmenu)
reportmenu.add_command(label="Gerar relatorio", command=gerar_tabela)

#  Criação ef Posicionamento dos Frames
# First rame
frame_1 = Frame(tela_principal, width=300, height=300, bg='#b3d9ff', highlightthickness=2)
frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.92)
        
# Second Frame
frame_2 = Frame(tela_principal, width=300, height=300, bg='#b3d9ff', highlightthickness=2)

# Create the baloon
bl_limpa = tix.Balloon(tela_principal)
bl_limpa.subwidget('label')['image'] = BitmapImage()

# First Frame widgets
# Tabs
abas = ttk.Notebook(frame_1) # Create the tab

aba_clientes = Frame(abas) # Create the frame of the first tab
aba_clientes.configure(background='lightgray')

aba_fornecedores = Frame(abas) # Create the frame of the second tab
aba_fornecedores.configure(background='lightgray')

abas.add(aba_clientes, text='Clientes') # Add an tab
abas.add(aba_fornecedores, text='Fornecedores') # Add an tab
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

#  Creating the buttons
bt_limpa = Button(aba_clientes, text="Limpar", bg='#004080', bd=2.5, fg="white", font=('verdana', 8, 'bold'), command=lambda: limpa_pessoa("clientes"))
bt_limpa.place(relx= 0.25, rely=0.1, relwidth=0.1, relheight= 0.15)
bl_limpa.bind_widget(bt_limpa, balloonmsg="Limpar todos os campos")

bt_busca = Button(aba_clientes, text="Buscar", bg='#004080', bd=2.5, fg="white", font=('verdana', 8, 'bold'), command=lambda: busca_pessoa("clientes"))
bt_busca.place(relx=0.35, rely=0.1, relwidth=0.1, relheight=0.15)
bl_limpa.bind_widget(bt_busca, balloonmsg="Buscar um cliente pelo nome")

bt_novo = Button(aba_clientes, text="Novo", bg='#004080', bd=2.5, fg="white", font=('verdana', 8, 'bold'), command=lambda: adicionar_pessoa("clientes"))
bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
bl_limpa.bind_widget(bt_novo, balloonmsg="Adicionar um cliente")

bt_alterar = Button(aba_clientes, text="Alterar", bg='#004080', bd=2.5, fg="white", font=('verdana', 8, 'bold'), command=lambda: altera_pessoa("clientes"))
bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
bl_limpa.bind_widget(bt_alterar, balloonmsg="Alterar dados de um cliente")

bt_apagar = Button(aba_clientes, text="Deletar", bg='#004080', bd=2.5, fg="white", font=('verdana', 8, 'bold'), command=lambda: deleta_pessoa("clientes"))
bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)
bl_limpa.bind_widget(bt_apagar, balloonmsg="Apagar dados de um cliente")

bt_abrirf2 = Button(aba_clientes, text="Abrir lista", bg='#004080', bd=2.5, fg="white", font=('verdana', 8, 'bold'), command=lambda: resolucao())
bt_abrirf2.place(relx=0.86, rely=0.84, relwidth=0.14, relheight=0.15)
bl_limpa.bind_widget(bt_abrirf2, balloonmsg="Abrir lista com os dados dos clientes")


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
TipVar2.set(TipV[0])
popupMenu2 = OptionMenu(aba_fornecedores,TipVar2, *TipV)
popupMenu2.place(relx=0.15, rely=0.825, relwidth=0.20)

# Criando os botões e balões

bt_limpa2 = Button(aba_fornecedores, text="Limpar", bg='#004080', bd=2.5, fg="white", font=('verdana', 8, 'bold'), command=lambda: limpa_pessoa("fornecedores"))
bt_limpa2.place(relx= 0.25, rely=0.1, relwidth=0.1, relheight= 0.15)
bl_limpa.bind_widget(bt_limpa2, balloonmsg="Limpar todos os campos")

bt_busca2 = Button(aba_fornecedores, text="Buscar", bg='#004080', bd=2.5, fg="white", font=('verdana', 8, 'bold'), command=lambda: busca_pessoa("fornecedores"))
bt_busca2.place(relx=0.35, rely=0.1, relwidth=0.1, relheight=0.15)
bl_limpa.bind_widget(bt_busca2, balloonmsg="Buscar um cliente pelo nome")

bt_novo2 = Button(aba_fornecedores, text="Novo", bg='#004080', bd=2.5, fg="white", font=('verdana', 8, 'bold'), command=lambda: adicionar_pessoa("fornecedores"))
bt_novo2.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
bl_limpa.bind_widget(bt_novo2, balloonmsg="Adicionar um cliente")

bt_alterar2 = Button(aba_fornecedores, text="Alterar", bg='#004080', bd=2.5, fg="white", font=('verdana', 8, 'bold'), command=lambda: altera_pessoa("fornecedores"))
bt_alterar2.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
bl_limpa.bind_widget(bt_alterar2, balloonmsg="Alterar dados de um cliente")

bt_apagar2 = Button(aba_fornecedores, text="Deletar", bg='#004080', bd=2.5, fg="white", font=('verdana', 8, 'bold'), command=lambda: deleta_pessoa("fornecedores"))
bt_apagar2.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)
bl_limpa.bind_widget(bt_apagar2, balloonmsg="Apagar dados de um cliente")

bt_abrirf3 = Button(aba_fornecedores, text="Abrir lista", bg='#004080', bd=2.5, fg="white", font=('verdana', 8, 'bold'), command=lambda: resolucao())
bt_abrirf3.place(relx=0.86, rely=0.84, relwidth=0.14, relheight=0.15)
bl_limpa.bind_widget(bt_abrirf3, balloonmsg="Abrir lista com os dados dos clientes")

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

selecionar_lista("clientes")

tela_principal.mainloop()