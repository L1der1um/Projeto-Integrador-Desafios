import tkinter as tk
from tkinter import ttk

# Função para calcular a energia cinética
def calcular_energia_cinetica():
    try:
        # Obter valores inseridos pelo usuário
        massa = float(entry_massa.get())
        velocidade = float(entry_velocidade.get())

        # Calcular a energia cinética
        energia_cinetica = 0.5 * massa * (velocidade ** 2)

        # Exibir o resultado na label de resultado
        resultado.set(f"Energia Cinética: {energia_cinetica:.2f} Joules")

    except ValueError:
        resultado.set("Por favor, insira valores válidos.")

# Função para limpar os campos
def limpar_campos():
    entry_massa.delete(0, tk.END)
    entry_velocidade.delete(0, tk.END)
    resultado.set("")  # Resetar o campo de resultado

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora de Energia Cinética")

# Criar um frame para o conteúdo
frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

# Labels e campos de entrada
label_massa = ttk.Label(frame, text="Massa (kg):")
label_massa.pack(fill="x", padx=5, pady=5)

entry_massa = ttk.Entry(frame)
entry_massa.pack(fill="x", padx=5, pady=5)

label_velocidade = ttk.Label(frame, text="Velocidade (m/s):")
label_velocidade.pack(fill="x", padx=5, pady=5)

entry_velocidade = ttk.Entry(frame)
entry_velocidade.pack(fill="x", padx=5, pady=5)

# Botões Calcular e Limpar
btn_calcular = ttk.Button(frame, text="Calcular", command=calcular_energia_cinetica)
btn_calcular.pack(fill="x", padx=5, pady=10)

btn_limpar = ttk.Button(frame, text="Limpar", command=limpar_campos)
btn_limpar.pack(fill="x", padx=5, pady=5)

# Label para exibir o resultado
resultado = tk.StringVar()
label_resultado = ttk.Label(frame, textvariable=resultado)
label_resultado.pack(fill="x", padx=5, pady=10)

# Iniciar a interface gráfica
root.mainloop()
