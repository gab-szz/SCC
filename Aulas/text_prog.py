from tkinter import *

OPTIONS = [
    "Selecione uma opção",
    "Contagem de caracteres",
    "Tornar maiusculo",
    "Tem a palavra no texto",
    "Esconder"
]


def function_exe():
    var = variable.get()
    result_label["text"] = " "
    result_label.grid(row=6, column=0)
    if (var == OPTIONS[0]):
        result_label["text"] = "Deu certo!"

    elif (var == OPTIONS[1]):
        var_1 = entry1.get()
        result_label["text"] = len(var_1)

    elif (var == OPTIONS[2]):
        var_1 = entry1.get()
        result_label["text"] = result_label.upper()

    elif (var == OPTIONS[3]):
        var_1 = entry1.get()
        var_2 = entry2.get()
        var_3 = var_2 in var_1
        if (var_3 == True):
            result_label["text"] = "A palavra digitada está\ncontida no texto"
        elif (var_3 == False):
            result_label["text"] = "A palavra digitada não\nestá contida no texto"
    # elif (var == OPTIONS[4]):

    elif (var == OPTIONS[4]):
        result_label.grid_remove()
        
    else:
        result_label["text"] = "Nenhuma opção foi selecionada"


main_window = Tk()
main_window.geometry("220x200+580+220")
main_window.title("Funções de Texto")

variable = StringVar(main_window)
variable.set(OPTIONS[0])

#   Criação de Widgets
# Labels
entry_label = Label(main_window, text="Digite um texto abaixo: ")
entry_label2 = Label(main_window, text="Caso necessário: ")
result_label = Label(main_window)
# Buttons
calc_option = OptionMenu(main_window, variable, *OPTIONS)
execute_btn = Button(main_window, text="Executar",
                     command=lambda: function_exe())
# Entrys
entry1 = Entry(main_window)
entry2 = Entry(main_window)

#   Grids
entry_label.grid(row=0, column=0)
entry1.grid(row=1, column=0)
entry_label2.grid(row=2, column=0)
entry2.grid(row=3, column=0)
calc_option.grid(row=4, column=0, padx=30)
execute_btn.grid(row=5, column=0)


main_window.mainloop()
