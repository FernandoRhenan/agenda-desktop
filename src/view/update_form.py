import tkinter as tk
from tkinter import messagebox
from data_interface.schedule import update_data
from view.tree import fill_data


def update_form(root, tree, footer, items):
    form_frame = tk.Frame(root, padx=10, pady=10)
    form_frame.pack(fill=tk.BOTH, expand=True)

    tk.Label(form_frame, text="Data:").grid(
        row=0, column=0, sticky="e", pady=5)
    data_entry = tk.Entry(form_frame)
    data_entry.grid(row=0, column=1, pady=5)
    data_entry.insert(0, items[0])

    tk.Label(form_frame, text="Hora:").grid(
        row=1, column=0, sticky="e", pady=5)
    hora_entry = tk.Entry(form_frame)
    hora_entry.grid(row=1, column=1, pady=5)
    hora_entry.insert(0, items[1])

    tk.Label(form_frame, text="Nome:").grid(
        row=2, column=0, sticky="e", pady=5)
    nome_entry = tk.Entry(form_frame)
    nome_entry.grid(row=2, column=1, pady=5)
    nome_entry.insert(0, items[2])

    tk.Label(form_frame, text="Procedimento:").grid(
        row=3, column=0, sticky="e", pady=5)
    procedimento_entry = tk.Entry(form_frame)
    procedimento_entry.grid(row=3, column=1, pady=5)
    procedimento_entry.insert(0, items[3])

    # Botões de Submeter e Cancelar
    buttons_frame = tk.Frame(form_frame)
    buttons_frame.grid(row=4, columnspan=2, pady=10)

    submeter_btn = tk.Button(buttons_frame, text="Atualizar", command=lambda: submeter(
        data_entry, hora_entry, nome_entry, procedimento_entry, form_frame, tree, footer, items[0], items[1]))
    submeter_btn.pack(side="left", padx=5)

    cancelar_btn = tk.Button(
        buttons_frame, text="Cancelar", command=lambda: cancelar(form_frame, tree, footer))
    cancelar_btn.pack(side="left", padx=5)

    return form_frame


def submeter(data_entry, hora_entry, nome_entry, procedimento_entry, form_frame, tree, footer, dataKey, timeKey):
    data = data_entry.get()
    time = hora_entry.get()
    name = nome_entry.get()
    service = procedimento_entry.get()

    if data and time and name and service:
        # Aqui você pode adicionar o código para salvar os dados

        update_data(name, service, data, time, dataKey, timeKey)

        fill_data(tree)

        messagebox.showinfo("Sucesso", "Agendamento atualizado com sucesso!")

        form_frame.pack_forget()
        tree.pack(fill=tk.BOTH, expand=True)
        footer.pack(pady=10)

    else:
        messagebox.showwarning("Campos obrigatórios",
                               "Todos os campos devem ser preenchidos.")


def cancelar(form, tree, footer):
    form.pack_forget()
    tree.pack(fill=tk.BOTH, expand=True)
    footer.pack(pady=10)
