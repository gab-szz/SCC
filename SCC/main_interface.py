from tkinter import *
from tkinter.tix import *
from register_interface import open_client_window

# Creating main window


def printar():
    print("printou")


def open_main_window():
    main_window = Tk()
    main_window.title("SCC")
    main_window.iconbitmap("Media/main_icon.ico")
    main_window.geometry("214x120+500+150")
    main_window['bg'] = "#99ddff"
    main_window.resizable(False, False)

# Import the image using PhotoImage function

    user_icon = PhotoImage(file='Media/user_icon_250544.png')
    add_user_icon = PhotoImage(file="Media/add_user_icon_250499.png")
    rmv_user_icon = PhotoImage(file='Media/x_user_icon_250479.png')

# Add Buttons

    add_client_tip = Balloon(main_window)
    rmv_client_tip = Balloon(main_window)
    client_tip = Balloon(main_window)

    find_client = Button(main_window, image=user_icon)
    find_client.grid(row=0, column=0, padx=18, pady=15)

    new_client = Button(main_window, image=add_user_icon,
                        command=lambda: open_client_window())
    new_client.grid(row=0, column=1, padx=15)

    delete_client = Button(
        main_window, image=rmv_user_icon)
    delete_client.grid(row=0, column=2, padx=15)

# Add binds in buttons

    add_client_tip.bind_widget(new_client, balloonmsg="Adicionar cliente")
    rmv_client_tip.bind_widget(delete_client, balloonmsg="Remover cliente")
    client_tip.bind_widget(find_client, balloonmsg="Ver clientes")

    sistem_label = Label(main_window,
                         text="S.C.A.",
                         background="#99ddff",
                         font="Times 25")
    sistem_label.grid(row=1, columnspan=3, sticky='we')

    main_window.mainloop()
