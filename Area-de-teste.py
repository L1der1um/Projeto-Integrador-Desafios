import tkinter as tk
from tkinter import ttk
import math

# Função para calcular o ângulo de refração de acordo com a Lei de Snell
def calcular_angulo_refracao():
    try:
        # Obter valores inseridos pelo usuário
        indice_refracao1 = float(entry_indice_refracao1.get())
        indice_refracao2 = float(entry_indice_refracao2.get())
        angulo_incidencia = float(entry_angulo_incidencia.get())

        # Validar se o índice de refração 2 é zero
        if indice_refracao2 == 0:
            resultado.set("O índice de refração 2 não pode ser zero.")
            return

        # Converter o ângulo de incidência para radianos (se estiver em graus)
        angulo_incidencia_rad = math.radians(angulo_incidencia)

        # Calcular o ângulo de refração usando a Lei de Snell
        angulo_refracao_rad = math.asin((indice_refracao1 / indice_refracao2) * math.sin(angulo_incidencia_rad))
        angulo_refracao_deg = math.degrees(angulo_refracao_rad)

        # Exibir o resultado na label de resultado
        resultado.set(f"Ângulo de Refração: {angulo_refracao_deg:.2f} graus")

    except ValueError:
        resultado.set("Por favor, insira valores válidos.")

# Função para limpar os campos
def limpar_campos():
    entry_indice_refracao1.delete(0, tk.END)
    entry_indice_refracao2.delete(0, tk.END)
    entry_angulo_incidencia.delete(0, tk.END)
    resultado.set("")  # Resetar o campo de resultado

# Criar a janela principal
root = tk.Tk()
root.title("Calculadora da Lei de Snell")

# Criar um frame para o conteúdo
frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

# Labels e campos de entrada
label_indice_refracao1 = ttk.Label(frame, text="Índice de Refração 1:")
label_indice_refracao1.pack(fill="x", padx=5, pady=5)

entry_indice_refracao1 = ttk.Entry(frame)
entry_indice_refracao1.pack(fill="x", padx=5, pady=5)

label_indice_refracao2 = ttk.Label(frame, text="Índice de Refração 2:")
label_indice_refracao2.pack(fill="x", padx=5, pady=5)

entry_indice_refracao2 = ttk.Entry(frame)
entry_indice_refracao2.pack(fill="x", padx=5, pady=5)

label_angulo_incidencia = ttk.Label(frame, text="Ângulo de Incidência (graus):")
label_angulo_incidencia.pack(fill="x", padx=5, pady=5)

entry_angulo_incidencia = ttk.Entry(frame)
entry_angulo_incidencia.pack(fill="x", padx=5, pady=5)

# Botões Calcular e Limpar
btn_calcular = ttk.Button(frame, text="Calcular", command=calcular_angulo_refracao)
btn_calcular.pack(fill="x", padx=5, pady=10)

btn_limpar = ttk.Button(frame, text="Limpar", command=limpar_campos)
btn_limpar.pack(fill="x", padx=5, pady=5)

# Label para exibir o resultado
resultado = tk.StringVar()
label_resultado = ttk.Label(frame, textvariable=resultado)
label_resultado.pack(fill="x", padx=5, pady=10)

# Iniciar a interface gráfica
root.mainloop()
