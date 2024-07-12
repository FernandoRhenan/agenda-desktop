import tkinter as tk

def abrir_arquivo():
    print("Abrir arquivo")

def salvar_arquivo():
    print("Salvar arquivo")

def criar_menu(root):
    menubar = tk.Menu(root)

    # Menu Arquivo
    menu_arquivo = tk.Menu(menubar, tearoff=0)
    menu_arquivo.add_command(label="Abrir", command=abrir_arquivo)
    menu_arquivo.add_command(label="Salvar", command=salvar_arquivo)
    menu_arquivo.add_separator()
    menu_arquivo.add_command(label="Sair", command=root.quit)

    menubar.add_cascade(label="Arquivo", menu=menu_arquivo)

    # Adicionar a barra de menus à janela principal
    root.config(menu=menubar)