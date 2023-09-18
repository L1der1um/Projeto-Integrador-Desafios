import tkinter as tk

# Função para calcular a força
def calcular_forca():
    try:
        # Obter valores inseridos pelo usuário
        massa1 = float(entry_massa1.get())
        massa2 = float(entry_massa2.get())
        distancia = float(entry_distancia.get())

        # Calcular a força usando a fórmula da gravitação universal de Newton
        constante_gravitacional = 6.67430e-11
        forca = constante_gravitacional * (massa1 * massa2) / (distancia ** 2)

        # Exibir o resultado na label de resultado
        resultado.config(text=f"Força: {forca:.4e} N")

    except ValueError:
        resultado.config(text="Por favor, insira valores válidos.")

# Criar a janela tkinter
janela = tk.Tk()
janela.title("Calculadora de Força Gravitacional")

# Massa 1
label_massa1 = tk.Label(janela, text="Massa 1 (kg):")
label_massa1.pack()

entry_massa1 = tk.Entry(janela)
entry_massa1.pack()

# Massa 2
label_massa2 = tk.Label(janela, text="Massa 2 (kg):")
label_massa2.pack()

entry_massa2 = tk.Entry(janela)
entry_massa2.pack()

# Distância
label_distancia = tk.Label(janela, text="Distância (m):")
label_distancia.pack()

entry_distancia = tk.Entry(janela)
entry_distancia.pack()

# Botão para calcular a força
calcular_button = tk.Button(janela, text="Calcular Força", command=calcular_forca)
calcular_button.pack()

# Label para exibir o resultado
resultado = tk.Label(janela, text="", padx=10, pady=10)
resultado.pack()

# Iniciar a interface gráfica
janela.mainloop()
