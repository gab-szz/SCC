from tkinter import *
from tkinter import ttk
from tkinter import tix
from tkinter import messagebox
import sqlite3
from tkcalendar import Calendar, DateEntry

conn = sqlite3.connect("BD_code.db")
cursor = conn.cursor()

# Funções

def tela_dois():
    tela_principal2 = Tk()
    tela_principal2.title = "SCC"
    tela_principal2.geometry("250x250+320+80")
    tela_principal2.configure(background='#0086b3')
    tela_principal2.resizable(width=True, height=True)
    tela_principal2.iconbitmap('@/home/gabs/Documentos/Projetos/Python/Aulas/main_icon.xbm')
    tela_principal2.transient(tela_principal)
    tela_principal2.focus_force()
    tela_principal2.grab_set()

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
    
def obter_cpf():
    t = en_cpf.get()
    tt = t.split(".")
    ttt = tt[2].split("-")
    full = tt[0] + tt[1] + ttt[0] + ttt[1]
    return full

def obter_telefone():
    t = en_telefone.get()
    tt = t.split("(")
    ttt = tt[1].split(")")
    full = ttt[0] + ttt[1]
    return full

def limpa_cliente():
    en_cpf.delete(0, "end")
    en_nome.delete(0, "end")
    en_telefone.delete(0, "end")
    en_cidade.delete(0, "end")
    
def adicionar_cliente():

    conn = sqlite3.connect("BD_code.db")
    cursor = conn.cursor()
    if en_nome.get() == "" or " ":
        msg = "Para cadastrar o novo cliente, é necessário\nque seja digitado ao menos um nome"
        messagebox.showinfo("Aviso", msg)
    else:
        cursor.execute("INSERT INTO clientes (cpf, nome, telefone, cidade, estado_civil) VALUES (?, ?, ?, ?, ?)", (en_cpf.get(), en_nome.get(), en_telefone.get(), en_cidade.get(), TipVar.get()))
        conn.commit()
        limpa_cliente()
        select_lista()
        conn.close()
    
def select_lista():
    tv.delete(*tv.get_children())
    conn = sqlite3.connect("BD_code.db")
    cursor = conn.cursor()
    lista = cursor.execute(""" SELECT cpf, nome, telefone, cidade, estado_civil FROM clientes
        ORDER BY nome ASC; """)
    for i in lista:
        tv.insert("", END, values=i)
    conn.close()
    
def OnDoubleClick(event):
    limpa_cliente()
    tv.selection
    
    for n in tv.selection():
        col1, col2, col3, col4 = tv.item(n, "values")
        en_cpf.insert(END, col1)
        en_nome.insert(END, col2)
        en_telefone.insert(END, col3)
        en_cidade.insert(END, col4)
        
def deleta_cliente():
    conn = sqlite3.connect("BD_code.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clientes WHERE cpf =?", (en_cpf.get(),))
    conn.commit()
    conn.close()
    select_lista()
    limpa_cliente()
    
def resolucao():
        if (bt_abrirf2["text"] == "Abrir lista"):
            tela_principal.geometry("800x600")
            frame_1.place(relx=0.02, rely=0.01, relwidth=0.96, relheight=0.46)
            frame_2.place(relx=0.02, rely=0.50, relwidth=0.96, relheight=0.48)
            bt_abrirf2["text"] = "Fechar lista"
            
        elif(bt_abrirf2["text"] == "Fechar lista"):
            tela_principal.geometry("800x300")
            frame_2.place_forget()
            frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.92)
            bt_abrirf2["text"] = "Abrir lista"
    
def OnDoubleClick(event):
    limpa_cliente()
    tv.selection()
    
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
            
def altera_cliente():
    conn = sqlite3.connect("BD_code.db")
    cursor = conn.cursor()
    cursor.execute(""" UPDATE clientes SET cpf =?, nome =?, telefone =?, cidade =?, estado_civil =? WHERE cpf =?""", (en_cpf.get(), en_nome.get(), en_telefone.get(), en_cidade.get(), TipVar.get(), en_cpf.get()))  
    conn.commit()
    conn.close()
    select_lista()
    limpa_cliente()
    
def busca_cliente():
    conn = sqlite3.connect("BD_code.db")
    cursor = conn.cursor()
    
    tv.delete(*tv.get_children())
    en_nome.insert(END, '%')
    cursor.execute(""" SELECT cpf, nome, telefone, cidade, estado_civil FROM clientes WHERE nome LIKE '%s' ORDER BY nome ASC""" % en_nome.get())
    buscanomeCli = cursor.fetchall()
    
    for i in (buscanomeCli):
        tv.insert("", END, values=i)
        
    limpa_cliente()
    conn.close()