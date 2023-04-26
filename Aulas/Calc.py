from tkinter import *


# Variáveis


OPTIONS = [

    "Operações",

    "Soma",

    "Subtração",

    "Divisão",

    "Multiplicação"

]  # etc


# Interface


main_window = Tk()

main_window.title("Calc")

main_window.geometry("163x190+600+225")


# Funções


variable = StringVar(main_window)

variable.set(OPTIONS[0])



def conta():

    var = variable.get()

    if (var == OPTIONS[0]):

        text2["text"] = "Selecione uma\noperação"

    elif (var == OPTIONS[1]):

        valor1 = float(input1.get())

        valor2 = float(input2.get())

        resultado = valor1 + valor2

        text2["text"] = "Resultado: {}".format(resultado)

    elif (var == OPTIONS[2]):

        valor1 = float(input1.get())

        valor2 = float(input2.get())

        resultado = valor1 - valor2

        text2["text"] = "{}".format(resultado)

    elif (var == OPTIONS[3]):
        #print(*OPTIONS)

        valor1 = float(input1.get())

        valor2 = float(input2.get())

        resultado = valor1 / valor2

        text2["text"] = "{}".format(resultado)

    elif (var == OPTIONS[4]):
        #print(*OPTIONS)

        valor1 = float(input1.get())

        valor2 = float(input2.get())

        resultado = valor1 * valor2

        text2["text"] = "{}".format(resultado)


# Operações de comparação:

#   a < b

#   a <= b

#   a > b

#   a >= b

#   a == b

#   a != b

#   a is b

#   a is not b


# Widgets



text1 = Label(main_window, text="Digite dois valores: ")

input1 = Entry(main_window, bd=5)

input2 = Entry(main_window, bd=5)

text2 = Label(main_window, text=" ", font="Arial 13")

calc_option = OptionMenu(main_window, variable, *OPTIONS)

calc_button = Button(main_window, text="Calcular",

                     command=lambda: conta(), bd=3)


# Posicionamento na Interface


text1.grid(columnspan=2, row=0, padx=15)

input1.grid(column=1, row=1, padx=15)

input2.grid(column=1, row=2, padx=15)

calc_option.grid(columnspan=2, row=4, pady=8, padx=15)

calc_button.grid(columnspan=2, row=5, padx=15)

text2.grid(columnspan=2, row=6, padx=15)



main_window.mainloop()

