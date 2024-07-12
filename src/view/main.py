import tkinter as tk
from menu import criar_menu

# Criação da janela principal
root = tk.Tk()
root.title("Agenda")
root.geometry("300x200")
root.state('zoomed')

# Criar o menu
criar_menu(root)

# Início do loop principal do Tkinter
root.mainloop()
