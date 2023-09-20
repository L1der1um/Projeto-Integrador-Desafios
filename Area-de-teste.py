import tkinter as tk
from tkinter import ttk

def calcular():
    try:
        # Obtenha os valores inseridos pelo usuário
        S0 = float(entry_S0.get())
        v = float(entry_v.get())
        t = float(entry_t.get())

        # Calcule a posição final S(t)
        St = S0 + v * t

        # Atualize as variáveis de resultado
        resultado.set(f"Posição Final (S(t)): {St:.2f} unidades")

    except ValueError:
        resultado.set("Insira valores válidos em todas as entradas")

# Cria a janela principal
root = tk.Tk()
root.title("Calculadora MRU")

# Cria um frame para as entradas e botão
frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# Labels e entradas para S0, v e t
label_S0 = tk.Label(frame, text="Posição Inicial (S0):")
label_S0.pack()

entry_S0 = ttk.Entry(frame)
entry_S0.pack()

label_v = tk.Label(frame, text="Velocidade (v):")
label_v.pack()

entry_v = ttk.Entry(frame)
entry_v.pack()

label_t = tk.Label(frame, text="Tempo (t):")
label_t.pack()

entry_t = ttk.Entry(frame)
entry_t.pack()

# Botão de calcular
btn_calcular = ttk.Button(frame, text="Calcular", command=calcular)
btn_calcular.pack()

# Variável de resultado
resultado = tk.StringVar()
resultado.set("")  # Inicialmente vazio

# Label para exibir o resultado
label_resultado = tk.Label(root, textvariable=resultado, padx=20, pady=10)
label_resultado.pack()

root.mainloop()
