import tkinter as tk
from tkinter import ttk

# Função para calcular a conservação da energia mecânica
def calcular_conservacao_energia_mecanica():
    try:
        # Obter valores inseridos pelo usuário
        energia_cinetica_inicial = float(entry_energia_cinetica_inicial.get())
        energia_potencial_inicial = float(entry_energia_potencial_inicial.get())
        energia_cinetica_final = float(entry_energia_cinetica_final.get())
        energia_potencial_final = float(entry_energia_potencial_final.get())

        # Verificar se a conservação da energia mecânica é válida
        energia_mecanica_inicial = energia_cinetica_inicial + energia_potencial_inicial
        energia_mecanica_final = energia_cinetica_final + energia_potencial_final

        if energia_mecanica_inicial == energia_mecanica_final:
            resultado.set("Conservação da Energia Mecânica é válida.")
        else:
            resultado.set("Conservação da Energia Mecânica não é válida.")

    except ValueError:
        resultado.set("Por favor, insira valores válidos.")

# Função para limpar os campos
def limpar_campos():
    entry_energia_cinetica_inicial.delete(0, tk.END)
    entry_energia_potencial_inicial.delete(0, tk.END)
    entry_energia_cinetica_final.delete(0, tk.END)
    entry_energia_potencial_final.delete(0, tk.END)
    resultado.set("")  # Resetar o campo de resultado

# Criar a janela principal
root = tk.Tk()
root.title("Verificador de Conservação da Energia Mecânica")

# Criar um frame para o conteúdo
frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

# Labels e campos de entrada
label_energia_cinetica_inicial = ttk.Label(frame, text="Energia Cinética Inicial (Joules):")
label_energia_cinetica_inicial.pack(fill="x", padx=5, pady=5)

entry_energia_cinetica_inicial = ttk.Entry(frame)
entry_energia_cinetica_inicial.pack(fill="x", padx=5, pady=5)

label_energia_potencial_inicial = ttk.Label(frame, text="Energia Potencial Inicial (Joules):")
label_energia_potencial_inicial.pack(fill="x", padx=5, pady=5)

entry_energia_potencial_inicial = ttk.Entry(frame)
entry_energia_potencial_inicial.pack(fill="x", padx=5, pady=5)

label_energia_cinetica_final = ttk.Label(frame, text="Energia Cinética Final (Joules):")
label_energia_cinetica_final.pack(fill="x", padx=5, pady=5)

entry_energia_cinetica_final = ttk.Entry(frame)
entry_energia_cinetica_final.pack(fill="x", padx=5, pady=5)

label_energia_potencial_final = ttk.Label(frame, text="Energia Potencial Final (Joules):")
label_energia_potencial_final.pack(fill="x", padx=5, pady=5)

entry_energia_potencial_final = ttk.Entry(frame)
entry_energia_potencial_final.pack(fill="x", padx=5, pady=5)

# Botões Calcular e Limpar
btn_calcular = ttk.Button(frame, text="Verificar", command=calcular_conservacao_energia_mecanica)
btn_calcular.pack(fill="x", padx=5, pady=10)

btn_limpar = ttk.Button(frame, text="Limpar", command=limpar_campos)
btn_limpar.pack(fill="x", padx=5, pady=5)

# Label para exibir o resultado
resultado = tk.StringVar()
label_resultado = ttk.Label(frame, textvariable=resultado)
label_resultado.pack(fill="x", padx=5, pady=10)

# Iniciar a interface gráfica
root.mainloop()
