import tkinter as tk

# Criando a janela
window = tk.Tk()
window.geometry("300x150")
window.title("Gerencia Frases")

# Adicionando um Frame para organizar os elementos
frame = tk.Frame(window)
frame.pack(padx=10, pady=10, fill='both', expand=True)  # fill='both' para melhor adaptação

# Adicionando um Label
label = tk.Label(frame, text="Olá, mundo!", font=("Arial", 12, "bold"))  # Melhorando a legibilidade
label.pack(fill='x', expand=True, pady=5)

# Adicionando um Label para o input
frase_lab = tk.Label(frame, text="Frase:", font=("Arial", 10))
frase_lab.pack(fill='x', expand=True)

# Adicionando o input de texto
frase_inp = tk.Entry(frame)
frase_inp.pack(fill='x', expand=True, pady=5)

# 5 
def click():
    label.config(text=frase_inp.get())


# 6 
button = tk.Button(frame, text="Enviar", command=click)
button.pack()

# Iniciando o loop da interface gráfica
window.mainloop()