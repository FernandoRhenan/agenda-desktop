import tkinter as tk


def criar_header_title(root, text):
    title = tk.Label(root, text=text, font=("Arial", 18), anchor="w")
    title.pack(fill='x', padx=10, pady=10)
