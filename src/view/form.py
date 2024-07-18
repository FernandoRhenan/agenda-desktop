import tkinter as tk
from tkinter import messagebox


def criar_form(root, tree, footer):
    form_frame = tk.Frame(root, padx=10, pady=10)
    form_frame.pack(fill=tk.BOTH, expand=True)

    tk.Label(form_frame, text="Data:").grid(
        row=0, column=0, sticky="e", pady=5)
    data_entry = tk.Entry(form_frame)
    data_entry.grid(row=0, column=1, pady=5)

    tk.Label(form_frame, text="Hora:").grid(
        row=1, column=0, sticky="e", pady=5)
    hora_entry = tk.Entry(form_frame)
    hora_entry.grid(row=1, column=1, pady=5)

    tk.Label(form_frame, text="Nome:").grid(
        row=2, column=0, sticky="e", pady=5)
    nome_entry = tk.Entry(form_frame)
    nome_entry.grid(row=2, column=1, pady=5)

    tk.Label(form_frame, text="Procedimento:").grid(
        row=3, column=0, sticky="e", pady=5)
    procedimento_entry = tk.Entry(form_frame)
    procedimento_entry.grid(row=3, column=1, pady=5)

    # Botões de Submeter e Cancelar
    buttons_frame = tk.Frame(form_frame)
    buttons_frame.grid(row=4, columnspan=2, pady=10)

    submeter_btn = tk.Button(buttons_frame, text="Agendar", command=lambda: submeter(
        data_entry, hora_entry, nome_entry, procedimento_entry))
    submeter_btn.pack(side="left", padx=5)

    cancelar_btn = tk.Button(
        buttons_frame, text="Cancelar", command=lambda: cancelar(form_frame, tree, footer))
    cancelar_btn.pack(side="left", padx=5)

    return form_frame


def submeter(data_entry, hora_entry, nome_entry, procedimento_entry):
    data = data_entry.get()
    hora = hora_entry.get()
    nome = nome_entry.get()
    procedimento = procedimento_entry.get()

    if data and hora and nome and procedimento:
        # Aqui você pode adicionar o código para salvar os dados
        print(f"Agendamento: {data}, {hora}, {nome}, {procedimento}")
        messagebox.showinfo("Sucesso", "Agendamento submetido com sucesso!")
    else:
        messagebox.showwarning("Campos obrigatórios",
                               "Todos os campos devem ser preenchidos.")


def cancelar(form, tree, footer):
    form.pack_forget()
    tree.pack(fill=tk.BOTH, expand=True)
    footer.pack(pady=10)
