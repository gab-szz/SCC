from tkinter import *
from tkinter import ttk
from classes import *
import sqlite3

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image
import webbrowser


# Criando o objeto que será a tela
main_window = new_window()

# Classe para relatorios em pdf
class Relatorios():
    # Função para abrir o relatório em pdf no browser padrão
    def printCliente(self):
        webbrowser.open("cliente.pdf") 
        
    # Função para gerar o relatório em pdf
    def geraRelatCliente(self):
        self.c = canvas.Canvas("cliente.pdf")
        self.codigoRel = self.en_codigo.get()
        self.nomeRel = self.en_nome.get()
        self.telefoneRel = self.en_telefone.get()
        self.cidadeRel = self.en_cidade.get()
        
        self.c.setFont("Helvetica-Bold", 24)
        self.c.drawString(220, 750, "Ficha do Cliente") # Titulo
        
        self.c.rect(20, 620, 550, 3, fill=True, stroke=False) # Faz uma linha
        
        self.c.setFont("Helvetica-Bold", 18)
        self.c.drawString(50, 700, "Codigo:" + self.codigoRel) 
        self.c.drawString(50, 680, "Nome:" + self.nomeRel) 
        self.c.drawString(50, 660, "Telefone:" + self.telefoneRel) 
        self.c.drawString(50, 640, "Cidade:" + self.cidadeRel) 
        
        self.c.rect(20, 620, 550, 3, fill=True, stroke=False) # Faz uma linha
        
        
        self.c.showPage()
        self.c.save()
        self.printCliente()
        
        



# Classe da funções que serão executadas
class Funcs():
    # Função para limpar as entradas
    def limpa_cliente(self):
        self.en_codigo.delete(0, END)
        self.en_cidade.delete(0, END)
        self.en_telefone.delete(0, END)
        self.en_nome.delete(0, END)
    
    # Função para conectar ao banco de dados
    def conecta_bd(self):
        self.conn = sqlite3.connect("BD_SCC.db")
        self.cursor = self.conn.cursor(); print("Conectando ao banco de dados")
        
    # Função para desconectar do banco de dados
    def desconecta_bd(self):
        self.conn.close(); print("Desconectando ao banco de dados")
        
    # Função para montar a tabela
    def montaTabelas(self):
        self.conecta_bd()
        ### Criar tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)               
            );
        """)
        self.conn.commit(); print("Banco de dados criado")
        self.desconecta_bd()
        
    # Função para adicionar um cliente
    def add_cliente(self):
        self.codigo = self.en_codigo.get()
        self.nome =  self.en_nome.get()
        self.fone = self.en_telefone.get()
        self.cidade = self.en_cidade.get()
        self.conecta_bd()

        self.cursor.execute(""" INSERT INTO clientes (nome_cliente, telefone, cidade)
            VALUES (?, ?, ?)""", (self.nome, self.fone, self.cidade))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_cliente()
        
    # Função para atualizar a tabela e a treeview
    def select_lista(self):
        self.tv.delete(*self.tv.get_children())
        self.conecta_bd()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
            ORDER BY cod ASC; """)
        for i in lista:
            print(i)
            self.tv.insert("", END, values=i)
        self.desconecta_bd()
        
    # Função do duplo clique no cliente na treeview puxar os dados para as entrys
    def OnDoubleClick(self, event):
        self.limpa_cliente()
        self.tv.selection()
        
        for n in self.tv.selection():
            col1, col2, col3, col4 = self.tv.item(n, 'values')
            self.en_codigo.insert(END, col1)
            self.en_nome.insert(END, col2)
            self.en_telefone.insert(END, col3)
            self.en_cidade.insert(END, col4)
            
    
    # Função para deletar os clientes da tabela
    def deleta_cliente(self):
        self.codigo = self.en_codigo.get()
        self.conecta_bd()
        self.cursor.execute(""" DELETE FROM clientes WHERE cod =?""", (self.codigo,))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_cliente()
        
    # Função para ocultar e mostrar o segundo frame
    def resolucao(self):
        if (self.bt_abrirf2["text"] == "Abrir lista"):
            main_window.geometry("700x500+320+80")
            self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
            self.frame2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
            self.bt_abrirf2["text"] = "Fechar lista"
            
        elif(self.bt_abrirf2["text"] == "Fechar lista"):
            self.frame2.place_forget()
            self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.94)
            main_window.geometry("700x250+320+80")
            self.bt_abrirf2["text"] = "Abrir lista"

    # Função para alterar dados de um cliente
    def alterar_cliente(self):
        self.codigo = self.en_codigo.get()
        self.nome =  self.en_nome.get()
        self.fone = self.en_telefone.get()
        self.cidade = self.en_cidade.get()
        self.conecta_bd()

        self.cursor.execute(""" UPDATE clientes SET nome_cliente =?, telefone =?, cidade =?
            WHERE cod =?""", (self.nome, self.fone, self.cidade, self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.limpa_cliente()

    # Função do botão buscar
    def busca_cliente(self):
        self.conecta_bd()
        self.tv.delete(*self.tv.get_children())
        
        self.en_nome.insert(END, '%')
        nome = self.en_nome.get()
        print(nome)
        self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
            WHERE nome_cliente LIKE '%s' ORDER BY cod ASC"""  % nome)
        buscanomeCli = self.cursor.fetchall()
        print(buscanomeCli)
        for i in buscanomeCli:
            self.tv.insert("", END, values=i)

        self.limpa_cliente()
        self.desconecta_bd()

# Classe com a aplicaçãos
class Application(Funcs, Relatorios):
    #def open_main_window():
    # Iniciando a tela
    def __init__(self):
        self.main_window = main_window
        self.tela_principal()
        self.frames_da_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        self.menu()
        
        
        main_window.mainloop()
    
    # Criando a tela principal
    def tela_principal(self):
        main_window.build_window('SCC', '700x250+320+80', '#004d00', False)
        
    # Criando os frames
    def frames_da_tela(self):
        # Criando os frames
        self.frame1 = Frame(main_window, bd=4, bg='#ccffb3',
               highlightbackground='#339900', highlightthickness=3)
        self.frame2 = Frame(main_window, bd=4, bg='#ccffb3',
               highlightbackground='#339900', highlightthickness=3)
        
        # Posicionando os frames
        self.frame1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.94)
        
    # Criando os widgets no frame1
    def widgets_frame1(self):
        # Criando os botões
        self.bt_busca = Button(self.frame1, text="Buscar", bg='#339900',
                        bd=2, fg="white", font=('verdana', 8, 'bold'), command=lambda: self.busca_cliente())
        self.bt_limpa = Button(self.frame1, text="Limpar", bg='#339900',
                        bd=2, fg="white", font=('verdana', 8, 'bold'), command=lambda: self.limpa_cliente())
        self.bt_novo = Button(self.frame1, text="Novo", bg='#339900',
                        bd=2, fg="white", font=('verdana', 8, 'bold'), command=lambda: self.add_cliente())
        self.bt_alterar = Button(self.frame1, text="Alterar", bg='#339900',
                        bd=2, fg="white", font=('verdana', 8, 'bold'), command=lambda: self.alterar_cliente())
        self.bt_apagar = Button(self.frame1, text="Apagar", bg='#339900',
                        bd=2, fg="white", font=('verdana', 8, 'bold'), command=lambda: self.deleta_cliente())
        self.bt_abrirf2 = Button(self.frame1, text="Abrir lista", bg='#339900',
                        bd=2, fg="white", font=('verdana', 8, 'bold'), command=lambda: self.resolucao())
        
        # Posicionando os botões
        self.bt_busca.place(relx=0.3, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_limpa.place(relx= 0.2, rely=0.1, relwidth=0.1, relheight= 0.15)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_alterar.place(relx=0.7, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_apagar.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.15)
        self.bt_abrirf2.place(relx=0.86, rely=0.85, relwidth=0.14, relheight=0.15)
        
        
        # Criando as labels
        self.lb_codigo = Label(self.frame1, text="Código", bg='#ccffb3',
                            fg="#339900", font=('verdana', 8, 'bold'))
        self.lb_nome = Label(self.frame1, text="Nome", bg='#ccffb3',
                            fg="#339900", font=('verdana', 8, 'bold'))
        self.lb_telefone = Label(self.frame1, text="Telefone", bg='#ccffb3',
                            fg="#339900", font=('verdana', 8, 'bold'))
        self.lb_cidade = Label(self.frame1, text="Cidade", bg='#ccffb3',
                            fg="#339900", font=('verdana', 8, 'bold'))
        
        # Posicionando as labels
        self.lb_codigo.place(relx= 0.05, rely= 0.05)
        self.lb_nome.place(relx=0.05, rely=0.35)
        self.lb_telefone.place(relx=0.05, rely=0.6)
        self.lb_cidade.place(relx=0.5, rely=0.6)
        
        # Criando as entrys
        self.en_codigo = Entry(self.frame1)
        self.en_nome = Entry(self.frame1)
        self.en_telefone = Entry(self.frame1)
        self.en_cidade = Entry(self.frame1)
        
        # Posicionando as entrys
        self.en_codigo.place(relx= 0.05, rely= 0.15, relwidth= 0.08)
        self.en_nome.place(relx=0.05, rely=0.45, relwidth=0.8)
        self.en_telefone.place(relx=0.05, rely=0.7, relwidth=0.4)
        self.en_cidade.place(relx=0.5, rely=0.7, relwidth=0.4)
    
    # Criando os widgets no frame2
    def lista_frame2(self):
        self.tv = ttk.Treeview(self.frame2, height=3,
                                     column=("col1", "col2", "col3", "col4"))
        self.tv.heading("#0", text="")
        self.tv.heading("#1", text="Codigo")
        self.tv.heading("#2", text="Nome")
        self.tv.heading("#3", text="Telefone")
        self.tv.heading("#4", text="Cidade")
        
        self.tv.column("#0", width=1)
        self.tv.column("#1", width=50)
        self.tv.column("#2", width=200)
        self.tv.column("#3", width=125)
        self.tv.column("#4", width=125)
        self.tv.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        # Criando a scrollbar
        self.scroolLista = Scrollbar(self.frame2, orient='vertical')
        self.tv.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)
        
        # Chamando o evento de ao clicar puxar os dados
        self.tv.bind('<Double-1>', self.OnDoubleClick)
    
    def menu(self):
        menubar = Menu(main_window)
        main_window.config(menu=menubar)
        filemenu = Menu(menubar, tearoff=0)
        #filemenu2 = Menu(menubar, tearoff=0)
        
        def Quit(): main_window.destroy()
        
        menubar.add_cascade(label="Opções", menu=filemenu)
        #menubar.add_cascade(label="Sobre", menu=filemenu2)
        filemenu.add_command(label="Gerar relatório", command=self.geraRelatCliente)
        filemenu.add_command(label="Sair", command=Quit)
        
Application()