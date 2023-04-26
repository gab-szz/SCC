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

    def execute_bd(self, text_bd2):
        self.cursor.execute("{}").format(text_bd2)
        self.cursor.commit()
        
    def select_bd(self, text_bd3):
        self.cursor.execute(f"""{text_bd3}""")
        
    def puxar_dado(self, text_bd3):
        self.cursor.execute(f"""{text_bd3}""")
        self.cursor.fetchall()
        
    def disconnect_bd(self):
        self.conn.close()
        