"""Trocar todas as variaveis tela8 por tela# da sua equação
    trocar os textos tanto no comentário quanto nos textos (text=)
    trocar as variaveis em label_ e entry_ (não podem se repetir no codigo principal)
    trocar as variaveis e formula da conta depois do comentário #FUNÇÃO QUE CALCULA...
    """
#CRIA A TELA 8 (Lei da gravitação universal de Newton)
    def criar_tela9(self):

        self.tela8 = tk.Frame(self.root)
        self.tela8.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela8, text="Lei da gravitação unversal de Newton" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=40)

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela8, text="Insira zero (0) dentro do dado que você deseja calcular")
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

        #TEXTO FORÇA GRAVITACIONAL (F)
        label_forcagravitacional = tk.Label(self.tela8, text="Força Gravitacional (N):")
        label_forcagravitacional.pack()

        entry_forcagravitacional = ttk.Entry(self.tela8)
        entry_forcagravitacional.placeholder = "Insira a força gravitacional"
        entry_forcagravitacional.insert(0,entry_forcagravitacional.placeholder)
        entry_forcagravitacional.bind("<FocusIn>", remover_placeholder)
        entry_forcagravitacional.bind("<FocusOut>", restaurar_placeholder)
        entry_forcagravitacional.pack()

        #TEXTO Massa 1 (m1)
        label_m1 = tk.Label(self.tela8, text="massa 1 (kg):")
        label_m1.pack()

        entry_m1 = ttk.Entry(self.tela8)
        entry_m1.placeholder = "Insira a massa do primeiro corpo: "
        entry_m1.insert(0,entry_m1.placeholder)
        entry_m1.bind("<FocusIn>", remover_placeholder)
        entry_m1.bind("<FocusOut>", restaurar_placeholder)
        entry_m1.pack()

        #TEXTO Massa 2 (m2)
        label_m2 = tk.Label(self.tela8, text="massa 2 (kg):")
        label_m2.pack()

        entry_m2 = ttk.Entry(self.tela8)
        entry_m2.placeholder = "Insira a massa do segundo corpo: "
        entry_m2.insert(0,entry_m2.placeholder)
        entry_m2.bind("<FocusIn>", remover_placeholder)
        entry_m2.bind("<FocusOut>", restaurar_placeholder)
        entry_m2.pack()

        #TEXTO Distância (r) 
        label_distraio = tk.Label(self.tela8, text="Distância r (m):")
        label_distraio.pack()

        entry_distraio = ttk.Entry(self.tela8)
        entry_distraio.placeholder = "Insira a distância entre os centros dos dois corpos: "
        entry_distraio.insert(0,entry_distraio.placeholder)
        entry_distraio.bind("<FocusIn>", remover_placeholder)
        entry_distraio.bind("<FocusOut>", restaurar_placeholder)
        entry_distraio.pack()

        #TEXTO Constante Gravitacional (G)

        label_gconstante = tk.Label(self.tela8, text="Constante gravitacional: 6.67430 x 10^(-11)")
        label_gconstante.pack()

        constanteg = 6.67430e-11

                #entry_m2 = ttk.Entry(self.tela8)
               # entry_m2.placeholder = "Insira a massa do segundo corpo: "
               # entry_m2.insert(0,entry_m2.placeholder)
                #entry_m2.bind("<FocusIn>", remover_placeholder)
                #entry_m2.bind("<FocusOut>", restaurar_placeholder)
               # entry_m2.pack()

        #FUNÇÃO QUE CALCULA A LEI GRAVITACIONAL DE NEWTON

        import math 

        def calcular():

            try:
                #PEGA OS DADOS INSERIDO PELO USUÁRIO
                forcagravitacional = float(entry_forcagravitacional.get())
                m1 = float(entry_m2.get())
                m2 = float(entry_m2.get())
                distraio = float(entry_distraio.get())

                #CALCULA A FORÇA
                if forcagravitacional == 0:

                    forcagravitacional = (constanteg*m1*m2*)/(distraio ** 2)
                    resultado.set(f"Força Gravitacional: {forcagravitacional} N")

                #CALCULA A MASSA 1
                elif m1 == 0:

                    m1 = (forcagravitacional*(dstraio**2)/(constanteg*m2))

                    resultado.set(f"Massa 1: {m1} kg")

                #CALCULA A MASSA 2 
                elif m2 == 0:

                    m2 = (forcagravitacional*(dstraio**2)/(constanteg*m1))

                    resultado.set(f"Massa 2: {m2} kg")

                #CALCULA A MASSA 2 

                elif m2 == 0:

                    distraio = math.sqrt((constanteg * m1 * m2) / forcagravitacional)

                    resultado.set(f"Distância r: {distraio} m")


                else:
                    #SOLICITA PARA O USUÁRIO INSERIR TRÊS VALORES E UM ZERO O DADO QUE DESEJA CALCULAR
                    resultado.set("Preencha três valores e deixe um campo com um zero (0) para calcular.")

            except ValueError:
                #INFORMA ERRO DE VALOR NÃO RECONHECIDO
                resultado.set("Insira valores numéricos válidos.")

        #FUNÇÃO LIMPAR OS CAMPOS
        def limpar_campos():
           entry_forcagravitacional.delete(0, tk.END)
           entry_m1.delete(0, tk.END)
           entry_m2.delete(0, tk.END)
            resultado.set("")  # Limpa o resultado

        #CRIANDO O FRAME PARA BOTOES CALCULAR E LIMPAR FICAREM ALINHADOS
        frame1 = tk.Frame(self.tela8)
        frame1.pack()
        #CRIANDO BOTOES
        botao_calcular = tk.Button(frame1, text="Calcular", command=calcular)
        botao_limpar = tk.Button(frame1, text="Limpar", command=limpar_campos)
        botao_calcular.pack(side=tk.LEFT,padx=10, pady=10)
        botao_limpar.pack(side=tk.LEFT,padx=10, pady=10)

        #TEXTO PARA INFORMAR O RESULTADO DA OPERAÇÃO
        resultado = tk.StringVar()
        label_resultado = tk.Label(self.tela8, textvariable=resultado)
        label_resultado.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela8, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom', pady=20)