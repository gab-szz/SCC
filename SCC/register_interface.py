from tkinter import *

def open_client_window():
    register_window = Tk()
    register_window.title("SCA")
    register_window.iconbitmap("Media/main_icon.ico")
    register_window.geometry("420x350+500+150")
    register_window['bg'] = "#99ddff"
    register_window.resizable(False, False)

# Funções

    def format_cpf(event=None):

        text = entry.get().replace(".", "").replace("-", "")[:11]
        new_text = ""

        if event.keysym.lower() == "backspace":
            return

        for index in range(len(text)):

            if not text[index] in "0123456789":
                continue
            if index in [2, 5]:
                new_text += text[index] + "."
            elif index == 8:
                new_text += text[index] + "-"
            else:
                new_text += text[index]

        entry.delete(0, "end")
        entry.insert(0, new_text)

    nome_label = Label(register_window, text="Nome: ",
                       background="#99ddff", font="Arial 12", pady=15)
    nome_entry = Entry(register_window)
    cpf_label = Label(register_window, text="CPF: ",
                      background="#99ddff", width=10)
    entry = Entry(register_window, font=("Arial", 12))
    sex_entry = Label(register_window, text="Sexo: ",
                      background="#99ddff", pady=15)
    sex_mb = Menubutton(
        register_window, text="selecione o sexo", relief=RAISED)

    entry.bind("<KeyRelease>", format_cpf)

    nome_label.grid(row=0, column=0)
    nome_entry.grid(row=0, column=1)
    cpf_label.grid(row=1, column=0)
    entry.grid(row=1, column=1)
    sex_entry.grid(row=2, column=0)
    sex_mb.grid(row=2, column=1)

    sex_mb.menu = Menu(sex_mb, tearoff=0)
    sex_mb["menu"] = sex_mb.menu

    mayoVar = IntVar()
    ketchVar = IntVar()

    sex_mb.menu.add_checkbutton(label="Masculino",
                                variable=mayoVar)
    sex_mb.menu.add_checkbutton(label="Feminino",
                                variable=ketchVar)

    register_window.mainloop()
