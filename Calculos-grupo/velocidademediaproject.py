"""Trocar todas as variaveis tela17 por tela# da sua equação
    trocar os textos tanto no comentário quanto nos textos (text=)
    trocar as variaveis em label_ e entry_ (não podem se repetir no codigo principal)
    trocar as variaveis e formula da conta depois do comentário #FUNÇÃO QUE CALCULA...
    """
#CRIA A TELA 13 (Velocidade Média)
    def criar_tela17(self):

        self.tela17 = tk.Frame(self.root)
        self.tela17.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela17, text="Velocidade Média" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=40)

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela17, text="Insira zero (0) dentro do dado que você deseja calcular")
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

        #TEXTO VELOCIDADE DE MÉDIA DE ENTRADA
        label_velomedia = tk.Label(self.tela17, text="Velocidade média (m/s):")
        label_velomedia.pack()

        entry_velomedia = ttk.Entry(self.tela17)
        entry_velomedia.placeholder = "Insira a velocidade média (m/s):"
        entry_velomedia.insert(0, entry_velomedia.placeholder)
        entry_velomedia.bind("<FocusIn>", remover_placeholder)
        entry_velomedia.bind("<FocusOut>", restaurar_placeholder)
        entry_velomedia.pack()

        #TEXTO DISTÂNCIA PERCORRIDA
        label_distanciap = tk.Label(self.tela17, text="Distância percorrida (m):")
        label_distanciap.pack()

        entry_distanciap = ttk.Entry(self.tela17)
        entry_distanciap.placeholder = "Insira a distância percorrida (m): "
        entry_distanciap.insert(0, entry_distanciap.placeholder)
        entry_distanciap.bind("<FocusIn>", remover_placeholder)
        entry_distanciap.bind("<FocusOut>", restaurar_placeholder)
        entry_distanciap.pack()

        #TEXTO TEMPO
        label_tempo = tk.Label(self.tela17, text="Tempo (s):")
        label_tempo.pack()

        entry_tempo = ttk.Entry(self.tela17)
        entry_tempo.placeholder = "Insira o tempo (s): "
        entry_tempo.insert(0, entry_tempo.placeholder)
        entry_tempo.bind("<FocusIn>", remover_placeholder)
        entry_tempo.bind("<FocusOut>", restaurar_placeholder)
        entry_tempo.pack()
        #FUNÇÃO QUE CALCULA A VELOCIDADE MÉDIA
        def calcular():

            try:
                #PEGA OS DADOS INSERIDO PELO USUÁRIO
                velomedia = float(entry_velomedia.get())
                distanciap = float(entry_distanciap.get())
                tempo = float(entry_tempo.get())

                #CALCULA A FORÇA
                if velomedia == 0:

                    velomedia = (distanciap / tempo)
                    resultado.set(f"Velocidade média: {velomedia} m/s")

                #CALCULA A DISTÂNCIA
                elif distanciap == 0:

                    distanciap = velomedia * tempo
                    resultado.set(f"Distância: {distanciap} m")

                #CALCULA O TEMPO
                elif tempo == 0:

                    tempo = distanciap / velomedia
                    resultado.set(f"Deformação {tempo} s")

                else:
                    #SOLICITA PARA O USUÁRIO INSERIR DOIS VALORES E UM ZERO O DADO QUE DESEJA CALCULAR
                    resultado.set("Preencha dois valores e deixe um campo com um zero (0) para calcular.")

            except ValueError:
                #INFORMA ERRO DE VALOR NÃO RECONHECIDO
                resultado.set("Insira valores numéricos válidos.")

        #FUNÇÃO LIMPAR OS CAMPOS
        def limpar_campos():
            entry_velomedia.delete(0, tk.END)
            entry_distanciap.delete(0, tk.END)
            entry_tempo.delete(0, tk.END)
            resultado.set("")  # Limpa o resultado

        #CRIANDO O FRAME PARA BOTOES CALCULAR E LIMPAR FICAREM ALINHADOS
        frame1 = tk.Frame(self.tela17)
        frame1.pack()
        #CRIANDO BOTOES
        botao_calcular = tk.Button(frame1, text="Calcular", command=calcular)
        botao_limpar = tk.Button(frame1, text="Limpar", command=limpar_campos)
        botao_calcular.pack(side=tk.LEFT,padx=10, pady=10)
        botao_limpar.pack(side=tk.LEFT,padx=10, pady=10)

        #TEXTO PARA INFORMAR O RESULTADO DA OPERAÇÃO
        resultado = tk.StringVar()
        label_resultado = tk.Label(self.tela17, textvariable=resultado)
        label_resultado.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela17, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom', pady=20)