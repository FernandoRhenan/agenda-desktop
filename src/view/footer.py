import tkinter as tk
from tkinter import messagebox


def criar_footer(root, tree):

    frame = tk.Frame(root)
    frame.pack(pady=10)

    btn_excluir = tk.Button(frame, text="Excluir",
                            command=lambda: excluir_agendamento(tree))
    btn_excluir.pack(side=tk.LEFT, padx=5)

    btn_alterar = tk.Button(frame, text="Alterar",
                            command=lambda: alterar_agendamento(tree))
    btn_alterar.pack(side=tk.LEFT, padx=5)

    btn_novo = tk.Button(frame, text="Novo agendamento",
                         command=lambda: excluir_agendamento(tree))
    btn_novo.pack(side=tk.LEFT, padx=5)

    return frame


def excluir_agendamento(tree):
    selected_item = tree.selection()  # Seleciona o item
    if not selected_item:
        messagebox.showwarning(
            "Nenhuma seleção", "Selecione um agendamento para excluir")
        return
    tree.delete(selected_item)  # Deleta o item selecionado


def alterar_agendamento(tree):
    selected_item = tree.selection()  # Seleciona o item
    if not selected_item:
        messagebox.showwarning(
            "Nenhuma seleção", "Selecione um agendamento para alterar")
        return
    tree.item(selected_item, values=(
        'nova_data', 'novo_horario', 'novo_nome', 'lal'))
    print(selected_item)
