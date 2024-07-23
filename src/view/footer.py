import tkinter as tk
from tkinter import messagebox
from view.tree import remover_tree
from view.form import criar_form
from view.update_form import update_form
from data_interface.schedule import delete_data


def criar_footer(root, tree):

    footer = tk.Frame(root)
    footer.pack(pady=10)

    btn_excluir = tk.Button(footer, text="Excluir",
                            command=lambda: excluir_agendamento(tree))
    btn_excluir.pack(side=tk.LEFT, padx=5)

    btn_alterar = tk.Button(footer, text="Alterar",
                            command=lambda: alterar_agendamento(tree, footer, root))
    btn_alterar.pack(side=tk.LEFT, padx=5)

    btn_novo = tk.Button(footer, text="Novo agendamento",
                         command=lambda: novo_agendamento(tree, footer, root))
    btn_novo.pack(side=tk.LEFT, padx=5)

    return footer


def excluir_agendamento(tree):
    selected_item = tree.selection()  # Seleciona o item
    if not selected_item:
        messagebox.showwarning(
            "Nenhuma seleção", "Selecione um agendamento para excluir")
        return
    items = tree.item(selected_item[0], "values")
    delete_data(items[0], items[1])

    tree.delete(selected_item)  # Deleta o item selecionado


def alterar_agendamento(tree, footer, root):
    selected_item = tree.selection()  # Seleciona o item
    if not selected_item:
        messagebox.showwarning(
            "Nenhuma seleção", "Selecione um agendamento para alterar")
        return

    items = tree.item(selected_item[0], "values")

    remover_tree(tree)
    footer.pack_forget()
    update_form(root, tree, footer, items)


def novo_agendamento(tree, footer, root):
    remover_tree(tree)
    footer.pack_forget()
    criar_form(root, tree, footer)
