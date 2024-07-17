import tkinter as tk
from data_interface.schedule import post_data, get_data


def criar_menu(root):

    menubar = tk.Menu(root)
    menubar.add_command(label="Sair", command=root.destroy)

    # Adicionar a barra de menus à janela principal
    root.config(menu=menubar)

    return menubar
