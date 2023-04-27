from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import sqlite3

class new_window(tk.Tk):
    def __init__(self):
        super().__init__()

    def build_window(self, wtitle, wgeo, wbg, wrez):
        # configure the root window
        self.title(f'{wtitle}')
        self.geometry(f'{wgeo}')
        self["bg"] = f'{wbg}'
        # self.iconbitmap(fs"{wico}")
        if (wrez == True):
            self.resizable(True, True)
        else:
            self.resizable(False, False)



class gerar_bd ():

    def connect_bd(self, nome_arquivo):
        # Conectando ao banco de dados
        self.conn = sqlite3.connect(f'{nome_arquivo}')
        # Um cursor é uma ponte entre o BD e o código:
        self.cursor = self.conn.cursor()

    def createtable_bd(self, name_table, datas_table):
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS {name_table} ({datas_table});""")
        
        
    def insert_bd(self, text_bd):
        self.cursor.execute(f"""INSERT INTO {text_bd}""")
        self.cursor.commit()

    def execute_bd(self, text_bd):
        self.cursor.execute("{}").format(text_bd)
        self.cursor.commit()
        
    def select_bd(self, text_bd):
        self.cursor.execute(f"""{text_bd}""")
        
    def puxar_dado(self, text_bd):
        self.cursor.execute(f"""{text_bd}""")
        self.cursor.fetchall()
        
    def select_lista(self, text_bd, text_bd2):
        self.listaCli.delete(*self.listaCli.get_children())
        self.connect_bd(text_bd)
        lista = self.cursor.execute(f"""{text_bd2}""")
        for i in lista:
            self.listaCli.insert('', 'end', values=(i))
        self.disconnect_bd()
        
    def disconnect_bd(self):
        self.conn.close()
        