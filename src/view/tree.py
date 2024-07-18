import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


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

    # Inserindo dados de exemplo
    dados = [
        ("01/01/2024", "10:00", "Cliente A", "manutenção"),
        ("02/01/2024", "11:00", "Cliente B", "manutenção"),
        ("03/01/2024", "12:00", "Cliente C", "manutenção"),
        ("04/01/2024", "13:00", "Cliente D", "manutenção"),
        ("05/01/2024", "14:00", "Cliente E", "manutenção")
    ]

    for index, dado in enumerate(dados):
        if index % 2 == 0:
            tree.insert("", tk.END, values=dado, tags=('evenrow'))
        else:
            tree.insert("", tk.END, values=dado, tags=('oddrow'))

    return tree


def remover_tree(tree):
    tree.pack_forget()


# Fazer tree e footer sumir quando clicar em Novo agendamento para aparecer os inputs.
