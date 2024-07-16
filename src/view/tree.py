import tkinter as tk
from tkinter import ttk


def criar_tree(root):

    tree = ttk.Treeview(root, columns=(
        "data", "hora", "nome"), show="headings")
    tree.heading("data", text="Data")
    tree.heading("hora", text="Horário")
    tree.heading("nome", text="Cliente")

    tree.pack(fill=tk.BOTH, expand=True)

    return tree
