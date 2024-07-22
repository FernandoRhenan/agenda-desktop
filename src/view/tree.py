import tkinter as tk
from tkinter import ttk
from data_interface.schedule import get_data


def criar_tree(root):

    tree = ttk.Treeview(root, columns=(
        "data", "hora", "nome", "procedimento"), show="headings")
    tree.heading("data", text="Data")
    tree.heading("hora", text="Horário")
    tree.heading("nome", text="Cliente")
    tree.heading("procedimento", text="Procedimento")

    tree.column("data", width=75, stretch=False, anchor="center")
    tree.column("hora", width=60, stretch=False, anchor="center")
    tree.column("nome", width=150, stretch=False)
    tree.column("procedimento", width=100, stretch=False)

    tree.pack(fill=tk.BOTH, expand=True)

    tree.tag_configure('oddrow', background='white')
    tree.tag_configure('evenrow', background='#eee')

    fill_data(tree)

    return tree


def fill_data(tree):

    for item in tree.get_children():
        tree.delete(item)

    dados = get_data()
    for index, dado in enumerate(dados):
        if index % 2 == 0:
            tree.insert("", tk.END, values=(
                dado[2], dado[3], dado[0], dado[1]), tags=('evenrow'))
        else:
            tree.insert("", tk.END, values=(
                dado[2], dado[3], dado[0], dado[1]), tags=('oddrow'))


def remover_tree(tree):
    tree.pack_forget()
