import tkinter as tk
from data_interface.schedule import post_data, get_data


def criar_menu(root):

    menubar = tk.Menu(root)

    menubar.add_command(label="Agenda", command=get_data)
    menubar.add_command(label="Novo agendamento", command=post_data)

    # Adicionar a barra de menus à janela principal
    root.config(menu=menubar)

    return menubar
