import tkinter as tk

# Função para calcular a densidade
def calcular_densidade():
    try:
        # Obtém os valores inseridos pelo usuário
        massa = float(entry_massa.get())
        volume = float(entry_volume.get())

        #Validar se o índice de refração 2 é zero
        if volume == 0:
            resultado.set("O volume não pode ser zero (0).")
            return

        # Calcula a densidade
        densidade = massa / volume

        # Atualiza o valor da StringVar
        resultado.set(f"Densidade: {densidade:.2f} kg/m³")

    except ValueError:
        resultado.set("Por favor, insira valores válidos / Preencha todos os campos.")

# Cria a janela principal
root = tk.Tk()
root.title("Calculadora de Densidade")

# Variável StringVar para o resultado
resultado = tk.StringVar()

# Rótulo e campo de entrada para a massa
label_massa = tk.Label(root, text="Massa (kg):")
label_massa.pack()
entry_massa = tk.Entry(root)
entry_massa.pack()

# Rótulo e campo de entrada para o volume
label_volume = tk.Label(root, text="Volume (m³):")
label_volume.pack()
entry_volume = tk.Entry(root)
entry_volume.pack()

# Botão para calcular a densidade
btn_calcular = tk.Button(root, text="Calcular Densidade", command=calcular_densidade)
btn_calcular.pack()

# Rótulo para exibir o resultado
resultado_label = tk.Label(root, textvariable=resultado)
resultado_label.pack()

# Inicia o loop principal da interface gráfica
root.mainloop()
