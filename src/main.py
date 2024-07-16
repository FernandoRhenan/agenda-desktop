import tkinter as tk
from view.menu import criar_menu
from view.tree import criar_tree
from view.header_title import criar_header_title
from infra.database import initDatabase

initDatabase()

# Configuração da janela principal
root = tk.Tk()
root.title("Agenda")
root.state('zoomed')
root.geometry('900x450')

criar_menu(root)
criar_header_title(root, "Agendamentos")
criar_tree(root)

# Loop principal da aplicação
root.mainloop()
