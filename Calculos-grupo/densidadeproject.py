"""Trocar todas as variaveis tela18 por tela# da sua equação
    trocar os textos tanto no comentário quanto nos textos (text=)
    trocar as variaveis em label_ e entry_ (não podem se repetir no codigo principal)
    trocar as variaveis e formula da conta depois do comentário #FUNÇÃO QUE CALCULA...
    """
#CRIA A TELA 13 (Velocidade Média)
    def criar_tela18(self):

        self.tela18 = tk.Frame(self.root)
        self.tela18.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela18, text="Densidade" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=40)

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela18, text="Insira zero (0) dentro do dado que você deseja calcular")
        label6.pack(pady=20)

        #FUNÇÃO PARA REMOVER O TEXTO DO PLACEHOLDER
        def remover_placeholder(event):
            widget = event.widget
            if widget.get() == widget.placeholder:
                widget.delete(0, tk.END)
        
        #FUNÇÃO QUE VOLTA O TEXTO DO PLACEHOLDER
        def restaurar_placeholder(event):
            widget = event.widget
            if not widget.get():
                widget.insert(0, widget.placeholder)

        #TEXTO DENSIDADE DE ENTRADA
        label_densidade = tk.Label(self.tela18, text="Densidade (kg/m³): ")
        label_densidade.pack()

        entry_densidade = ttk.Entry(self.tela18)
        entry_densidade.placeholder = "Insira a Densidade (kg/m³):"
        entry_densidade.insert(0, entry_densidade.placeholder)
        entry_densidade.bind("<FocusIn>", remover_placeholder)
        entry_densidade.bind("<FocusOut>", restaurar_placeholder)
        entry_densidade.pack()

        #TEXTO MASSA DO CORPO
        label_massac = tk.Label(self.tela18, text="Massa (kg):")
        label_massac.pack()

        entry_massac = ttk.Entry(self.tela18)
        entry_massac.placeholder = "Insira a Massa do corpo (kg): "
        entry_massac.insert(0, entry_massac.placeholder)
        entry_massac.bind("<FocusIn>", remover_placeholder)
        entry_massac.bind("<FocusOut>", restaurar_placeholder)
        entry_massac.pack()

        #TEXTO VOLUME
        label_volumec = tk.Label(self.tela18, text="Volume (m³):")
        label_volumec.pack()

        entry_volumec = ttk.Entry(self.tela18)
        entry_volumec.placeholder = "Insira o volume (m³): "
        entry_volumec.insert(0, entry_volumec.placeholder)
        entry_volumec.bind("<FocusIn>", remover_placeholder)
        entry_volumec.bind("<FocusOut>", restaurar_placeholder)
        entry_volumec.pack()
        #FUNÇÃO QUE CALCULA A DENSIDADE
        def calcular():

            try:
                #PEGA OS DADOS INSERIDO PELO USUÁRIO
                densidade = float(entry_densidade.get())
                massac = float(entry_massac.get())
                volumec = float(entry_volumec.get())

                #CALCULA A FORÇA
                if densidade == 0:

                    densidade = (massac / volumec)
                    resultado.set(f"Velocidade média: {densidade} kg/m³")

                #CALCULA A DISTÂNCIA
                elif massac == 0:

                    massac = densidade * volumec
                    resultado.set(f"Distância: {massac} kg")

                #CALCULA O volumec
                elif volumec == 0:

                    volumec = massac / densidade
                    resultado.set(f"Deformação {volumec} m³")

                else:
                    #SOLICITA PARA O USUÁRIO INSERIR DOIS VALORES E UM ZERO O DADO QUE DESEJA CALCULAR
                    resultado.set("Preencha dois valores e deixe um campo com um zero (0) para calcular.")

            except ValueError:
                #INFORMA ERRO DE VALOR NÃO RECONHECIDO
                resultado.set("Insira valores numéricos válidos.")

        #FUNÇÃO LIMPAR OS CAMPOS
        def limpar_campos():
            entry_densidade.delete(0, tk.END)
            entry_massac.delete(0, tk.END)
            entry_volumec.delete(0, tk.END)
            resultado.set("")  # Limpa o resultado

        #CRIANDO O FRAME PARA BOTOES CALCULAR E LIMPAR FICAREM ALINHADOS
        frame1 = tk.Frame(self.tela18)
        frame1.pack()
        #CRIANDO BOTOES
        botao_calcular = tk.Button(frame1, text="Calcular", command=calcular)
        botao_limpar = tk.Button(frame1, text="Limpar", command=limpar_campos)
        botao_calcular.pack(side=tk.LEFT,padx=10, pady=10)
        botao_limpar.pack(side=tk.LEFT,padx=10, pady=10)

        #TEXTO PARA INFORMAR O RESULTADO DA OPERAÇÃO
        resultado = tk.StringVar()
        label_resultado = tk.Label(self.tela18, textvariable=resultado)
        label_resultado.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela18, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom', pady=20)