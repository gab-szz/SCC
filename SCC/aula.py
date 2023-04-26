from tkinter import *

window = Tk()

# adicionar titulo
window.title("Sistema de Cadastro de Alunos")

# adicionar icone
window.iconbitmap("Media/main_icon.ico")

# mudar cor de fundo ['bg' = background]
window['bg'] = "white"

# larguraxaltura e local de inicio <+^
window.geometry("550x500+430+100")  # inicia no centro

# tamanho minimo (largura, altura)
window.minsize(450, 400)

# tamanho maximo
# window.maxsize(550, 500)

# impede a mudança de tamanho da janela (largura, altura) (Boolean)
window.resizable(True, True)

# Define o inicio ("zoomed = tela cheia, iconic = pequena")
# window.state("iconic")

# função do botão

count_color = 1


def click_color():
    global count_color
    if (count_color == 1):
        window['bg'] = "green"
        count_color = 2
    elif (count_color == 2):
        window['bg'] = "blue"
        count_color = 3
    elif (count_color == 3):
        window['bg'] = "white"
        count_color = 1

# Função de disparar mensagem


def message_click(mensagem):
    print(mensagem)


# botão para mudar cor
btn_color = Button(window, text="Mudar Cor",
                   command=click_color,
                   width=20,  # Define a largura
                   height=2)  # Define a altura

# o pack é o que coloca o widget criado no layout
btn_color.pack()

# botão para disparar mensagem
btn_message = Button(window, text="Disparar mensagem",
                     command=lambda: message_click("Mensagem"),
                     bg="#b3d9ff",  # muda a cor de fundo
                     fg="#000000",  # muda a cor da fonte
                     font="Times 16")  # muda a fonte e o tamanho
btn_message.pack()

# label
label_1 = Label(window,
                text="Frase1\nFrase2",
                padx=10,
                pady=10,
                justify=LEFT,
                anchor=W,
                bd=1,  # Começamos aqui a adicionar uma borda, sâo 6 tipos:
                relief="solid")  # groove #solid #sunken #raised #ridge #flat
# label_1.pack()

# outro modo de modificar objetos
label_2 = Label(window)
label_2['text'] = "Segundo Label"
label_2['bd'] = 3
label_2['relief'] = "solid"
# label_2.pack()
label_1.grid(row=0, column=0)
label_2.grid(row=1, column=0)

window.mainloop()
