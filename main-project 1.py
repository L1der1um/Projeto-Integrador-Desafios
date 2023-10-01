#IMPORTANDO A BIBLIOTECA TKINTER
import tkinter as tk
from tkinter import Text
from tkinter import ttk
#IMPORTANTO BIBLIOTECA WEBBROWSER PARA O LINK DO GITHUB
import webbrowser
#IMPORTANTO BIBLIOTECA MATH PARA CALCULAR RESULTADOS COM SEN E COS
import math
#IMPORTANDO BIBLITOECA QRCODE PARA GERAR O QRCODE DO GITHUB
import qrcode
##IMPORTANDO BIBLIOTECA PIL PARA AUXILAR NA ABERTURA DO QRCODE NA TELA
from PIL import ImageTk

#CRIANDO A CLASSE SOFTWARE
class Software:

#################################################### CONFIGURAÇÃO TKINTER ##########################################################

    #FUNÇÕES DA CLASSE SOFTWARE

    #FUNÇÃO INICIA TELA 1 E DEFINE CONFIGURAÇÕES DE TODAS AS TELAS
    def __init__(self, root):

        self.root = root
        #DEFINE O TITULO DO PROGRAMA
        root.title("PROJETO INTEGRADOR")
        #DEFINE A ESCALA DO PROGRAMA
        root.geometry("900x500")
        #IMPOSIBILITA A REDIMENÇÃO DO PROGRAMA
        root.resizable(False, False)
        #DEFINE A TELA PRINCIAPL
        self.tela_atual = 1
        #EXECUTA A TELA PRINCIPAL
        self.criar_tela1()

################################################ FUNÇÕES CRIAR TELA #############################################################

    #CRIA A TELA 1 (PRINCIPAL)
    def criar_tela1(self):
        
        #PRIMEIRA TELA (INICIO)
        self.tela1 = tk.Frame(self.root)
        self.tela1.pack()

        #FUNÇÃO ENCERRAR PROGRAMA
        def encerrar_programa():
            
            root.destroy()

        #MENSAGEM DE TEXTO TELA 1
        label1 = tk.Label(self.tela1, text="PROJETO INTEGRADOR - DESAFIOS DE PROGRAMAÇÃO", font=('Arial', 16, 'bold'))
        label1.pack(pady=40)

        #BOTAO INICIAR VAI PARA A PROXIMA TELA
        btn_proxima_tela1 = tk.Button(self.tela1, text="INICIAR", command=self.ir_para_tela2, bg='blue', fg='white')
        btn_proxima_tela1.pack(fill="both", expand=True, pady=80)

        #MENSAGEM DE TEXTO TELA 1
        label1 = tk.Label(self.tela1, text="Projeto realizado por:")
        label1.pack(pady=10)

        #LISTAGEM ALUNOS
        alunos = "Matheus Henrique de Oliveira \n Peterson dos Santos Ferreira \n Lenin Misquevis Pellizzoni \n Felipe Albino Rafaldini Oliveira"
        label2 = tk.Label(self.tela1, text=alunos)
        label2.pack()

        #BOTAO ENCERRAR O SOFTWARE
        botao = tk.Button(self.tela1, text="Encerrar", command=encerrar_programa, bg='red', fg='white')
        botao.pack(pady=30, side='bottom')


    #CRIA A TELA 2 (OPÇÕES)
    def criar_tela2(self):

        self.tela2 = tk.Frame(self.root)
        self.tela2.pack()

        #MENSAGEM DE TEXTO TELA 2
        label2 = tk.Label(self.tela2, text="Escolha uma opção",font=('Arial', 14, 'bold'))
        label2.pack(pady=70)
        
        #BOTÃO IR PARA AS PRINCIPAIS FORMULAS
        btn_proxima_tela2 = tk.Button(self.tela2, text='Principais formulas Física 1', command=self.ir_para_tela3)
        btn_proxima_tela2.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela2, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom')

        #BOTÕES CENTRO DA TELA
        botao2 = tk.Button(self.tela2, text="Objetivo do projeto", command=self.ir_para_tela4)
        botao3 = tk.Button(self.tela2, text="Agradecimentos e referencias", command=self.ir_para_tela5)
        botao4 = tk.Button(self.tela2, text="GitHub do projeto", command=self.ir_para_tela6)

        #ALINHANDO NA HORIZONTAL OS BOTÕES
        botao2.pack(side="left")
        botao3.pack(side="left",padx=10)
        botao4.pack(side="left", pady=50)


    #CRIA A TELA 3 (PRINCIPAIS FORMULAS)
    def criar_tela3(self):

        self.tela3 = tk.Frame(self.root)
        self.tela3.pack()

        #MENSAGEM DE TEXTO TELA 3
        label3 = tk.Label(self.tela3, text="SELECIONE UMA FORMULA",font=('Arial', 14, 'bold'))
        label3.pack(pady=10)

        #CRIANDO O FRAME DA PRMEIRA LINHA DE BOTOES
        frame1 = tk.Frame(self.tela3)
        frame1.pack()
        #CRIANDO A PRIMEIRA FILEIRA DE BOTOES
        button1 = tk.Button(frame1, text="Lei de movimento de Newton\n(Segunda lei)\nF = m * a",command=self.ir_para_tela7)
        button2 = tk.Button(frame1, text="Lei da gravitação\n Universal de Newton\nF = G * (m1 * m2) / d^2",command=self.ir_para_tela8)
        #button3 = tk.Button(frame1, text="Lei de Coulomb\n (Lei de Eletrostatica)\nF = k * (|q1 * q2|) / d²",command=self.ir_para_tela9)
        button4 = tk.Button(frame1, text="Energia cinética\nEc = m . v² / 2",command=self.ir_para_tela10)
        button1.pack(side=tk.LEFT,padx=10, pady=10)
        button2.pack(side=tk.LEFT,padx=10, pady=10)
        #button3.pack(side=tk.LEFT,padx=10, pady=10)
        button4.pack(side=tk.LEFT,padx=10, pady=10)

        #CRIANDO O FRAME DA SEGUNDA LINHA DE BOTOES
        frame2 = tk.Frame(self.tela3)
        frame2.pack()
        #CRIANDO O FRAME DA PRMEIRA LINHA DE BOTOES
        button5 = tk.Button(frame2, text="Energia Potencial\n Gravitacional\nEPG = m * g * h",command=self.ir_para_tela11)
        button6 = tk.Button(frame2, text="Lei da conservação\n de Energia Mecânica\nE = K + U",command=self.ir_para_tela12)
        button7 = tk.Button(frame2, text="Lei de Hooke\n (Lei da Elasticidade)\nF = -k * x",command=self.ir_para_tela13)
        #button8 = tk.Button(frame2, text="Lei de Snell\n (Lei da Refração)\nn1.sen(i) = n2.sen(r)",command=self.ir_para_tela14)
        button5.pack(side=tk.LEFT,padx=10, pady=40)
        button6.pack(side=tk.LEFT,padx=10, pady=40)
        button7.pack(side=tk.LEFT,padx=10, pady=40)
        #button8.pack(side=tk.LEFT,padx=10, pady=40)


        #CRIANDO O FRAME DA TERCEIRA LINHA DE BOTOES
        frame3 = tk.Frame(self.tela3)
        frame3.pack()
        #CRIANDO O FRAME DA PRMEIRA LINHA DE BOTOES
        button9 = tk.Button(frame3, text="Lei de Ohm\n (Primeira lei)\nV = I * R",command=self.ir_para_tela15)
        button10 = tk.Button(frame3, text="Movimento Retilíneo\nUniforme\nS(t) = S₀ + v * t",command=self.ir_para_tela16)
        button11 = tk.Button(frame3, text="Velocidade média\nVm = ΔS / Δt",command=self.ir_para_tela17)
        button12 = tk.Button(frame3, text="Densidade\nd = m / v",command=self.ir_para_tela18)
        button9.pack(side=tk.LEFT,padx=10, pady=10)
        button10.pack(side=tk.LEFT,padx=10, pady=10)
        button11.pack(side=tk.LEFT,padx=10, pady=10)
        button12.pack(side=tk.LEFT,padx=10, pady=10)

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela3, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(pady=40)


    #CRIA A TELA 4 (Objetivo do projeto)
    def criar_tela4(self):

        self.tela4 = tk.Frame(self.root)
        self.tela4.pack()

        #TEXTO INFORMATIVO DE TELA
        label4 = tk.Label(self.tela4, text="OBJETIVO DO PROJETO",font=('Arial', 14, 'bold'))
        label4.pack(pady=30)

        #TEXTO TELA OBJETIVO PRINCIPAL
        texto = """
            O objetivo deste projeto é desenvolver um software desktop que permita o usuário recém
        ingressado na faculdade resolver problemas matemáticos mediantes as fórmulas mais utilizadas
        na matéria de Física 1, em conjunto de explicações da utilização e o contexto de cada fórmula.
        A opção escolhida se deve ao fato de que ao desenvolver este software um calouro pode ter um
        melhor desenvolvimento em suas aulas práticas.
        
        Atualmente um novo aluno deve pesquisar por horas em livros ou na internet como resolver um
        determinado problema em Física 1, portanto, o software permitirá ao aluno ter um melhor
        desenvolvimento em suas aulas possibilitando-o compreender melhor o contexto das aulas.
        Espera-se que o software contenha uma tela ao qual o usuário deve, no entanto, selecionar as
        opções dentre elas estará o objetivo do projeto, agradecimentos e referencias, GitHub com o
        código fonte do projeto e as principais fórmulas as quais devem, no entanto, apresentar uma
        contextualização no que cada uma é utilizada.
        """

        #RÓTULO DO TEXTO
        label4_1 = tk.Label(self.tela4, text=texto, justify="center", padx=10, pady=10, font=('Arial', 14))
        label4_1.pack(pady=35)

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela4, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom')


    #CRIA A TELA 5 (Agradecimentos e Refêrencias)
    def criar_tela5(self):

        self.tela5 = tk.Frame(self.root)
        self.tela5.pack()

        #TEXTO INFORMATIVO DE TELA
        label5 = tk.Label(self.tela5, text="AGRADECIMENTOS E REFERÊNCIAS" ,font=('Arial', 14, 'bold'))
        label5.pack(pady=30, side='top', anchor='n')

        #TEXTO TELA AGRADECIMENTOS
        texto = """
        Agradecimentos especiais ao orientador José Roberto Garcia por ter orientado
        o grupo a como realizar o projeto desde seu início.

        Refêrencias para a criação do projeto:

        Curso Python Tkinter - Aula 1 - Criação e configuração da janela - Tutorial.
        Disponível em: <https://youtu.be/RtrZcoVD1WM?si=OMOTKxhMTCHm8hx6>. Acesso em: 22 set. 2023.

        
        Curso Python #01 - Seja um Programador. Disponível em:
        <https://youtu.be/S9uPNppGsGo?si=Gm1UMf9YWbZ97y3h>. Acesso em: 22 set. 2023.

        
        How to add placeholder to an Entry in tkinter? Disponível em:
        <https://stackoverflow.com/questions/27820178/how-to-add-placeholder-to-an-entry-in-tkinter>.
        Acesso em: 22 set. 2023.
        """

        #RÓTULO DO TEXTO
        label5_1 = tk.Label(self.tela5, text=texto, justify="center", padx=10, pady=10)
        label5_1.pack(anchor='n')

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela5, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom')


    #CRIA A TELA 6 (GitHub do projeto)
    def criar_tela6(self):

        self.tela6 = tk.Frame(self.root)
        self.tela6.pack()

        #FUNÇÃO ABRIR LINK DO GITHUB
        def abrir_github():

            webbrowser.open('https://github.com/L1der1um/Projeto-Integrador-Desafios')

        #FUNÇÃO EXIBIR QRCODE NA TELA
        def mostrar_qr_code():

            #DEFININDO A URL DO PROJETO
            url = "https://github.com/L1der1um/Projeto-Integrador-Desafios"
            #DEFININDO A CONFIGURAÇÃO DA IMAGEM
            qr = qrcode.QRCode(box_size=3,border=3)
            qr.add_data(url)
            #CRIANDO NA TELA O QRCODE COM A COR PRETO E BRANCO
            img = qr.make_image(fill_color="black", back_color="white")

            #EXIBIÇÃO DA IMAGEM NA TELA
            img = ImageTk.PhotoImage(img)
            label = tk.Label(self.tela6, image=img)
            label.photo = img
            label.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela6, text="GITHUB DO PROJETO" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=30)

        #BOTÃO PARA ABRIR O GITHUB
        button_github = tk.Button(self.tela6, text="Abrir GitHub", command=abrir_github)
        button_github.pack(pady=30)

        #CAMPO DE TEXTO PARA INFORMAR O USUARIO PARA COPIAR O LINK
        label6_1 = tk.Label(self.tela6, text="Não consegue abrir o link? Copie ele abaixo e cole em seu navegador!",font=('Arial', 14, 'bold'))
        label6_1.pack(pady=5)

        #DEFINE O CAMPO DO TEXTO
        text = Text(self.tela6, height=1, width=70)
        #INSERE O LINK COMO TEXTO
        text.insert('1.0', 'https://github.com/L1der1um/Projeto-Integrador-Desafios')
        #IMPOSSIBILTA A ALTERAÇÃO DO CAMPO DO LINK
        text.config(state="disabled")
        text.pack()

        #BOTÃO PARA EXIBIR O QRCODE NA TELA
        gerar_qr = tk.Button(self.tela6, text="Gerar QR Code", command=mostrar_qr_code)
        gerar_qr.pack(pady=30)

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela6, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=20)


############################################# FUNÇÕES FORMULAS #############################################################

    #CRIA A TELA 7 (Lei de Movimento de Newton (Segunda Lei))
    def criar_tela7(self):

        self.tela7 = tk.Frame(self.root)
        self.tela7.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela7, text="Lei de Movimento de Newton (Segunda Lei)" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=30)

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela7, text="F = m . a")
        label6.pack(pady=5)

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

        #TEXTO MASSA DO CAMPO DE ENTRADA
        label_massa = tk.Label(self.tela7, text="Massa (kg):")
        label_massa.pack()

        entry_massa = ttk.Entry(self.tela7)
        entry_massa.placeholder = "Insira a massa"
        entry_massa.insert(0, entry_massa.placeholder)
        entry_massa.bind("<FocusIn>", remover_placeholder)
        entry_massa.bind("<FocusOut>", restaurar_placeholder)
        entry_massa.pack()

        #TEXTO ACELERAÇÃO DO CAMPO DE ENTRADA
        label_aceleracao = tk.Label(self.tela7, text="Aceleração (m/s²):")
        label_aceleracao.pack()

        entry_aceleracao = ttk.Entry(self.tela7)
        entry_aceleracao.placeholder = "Insira a aceleração"
        entry_aceleracao.insert(0, entry_aceleracao.placeholder)
        entry_aceleracao.bind("<FocusIn>", remover_placeholder)
        entry_aceleracao.bind("<FocusOut>", restaurar_placeholder)
        entry_aceleracao.pack()

        #FUNÇÃO QUE CALCULA A LEI DE MOVIMENTO DE NEWTON
        def calcular():

            try:
                #PEGA OS DADOS INSERIDO PELO USUÁRIO
                massa = float(entry_massa.get())
                aceleracao = float(entry_aceleracao.get())

                forca = massa * aceleracao
                resultado.set(f"Força: {forca:.2f} N")

            except ValueError:

                #INFORMA ERRO DE VALOR NÃO RECONHECIDO
                resultado.set("Insira valores numéricos válidos / Preencha todos os valores")

        #FUNÇÃO LIMPAR OS CAMPOS
        def limpar_campos():
            entry_massa.delete(0, tk.END)
            entry_aceleracao.delete(0, tk.END)
            resultado.set("")  #LIMPA DA CAIXA DE RESULTADO

        #CRIANDO O FRAME PARA BOTOES CALCULAR E LIMPAR FICAREM ALINHADOS
        frame1 = tk.Frame(self.tela7)
        frame1.pack()
        #CRIANDO BOTOES
        botao_calcular = tk.Button(frame1, text="Calcular", command=calcular)
        botao_limpar = tk.Button(frame1, text="Limpar", command=limpar_campos)
        botao_calcular.pack(side=tk.LEFT,padx=10, pady=10)
        botao_limpar.pack(side=tk.LEFT,padx=10, pady=10)

        #TEXTO PARA INFORMAR O RESULTADO DA OPERAÇÃO
        resultado = tk.StringVar()
        label_resultado = tk.Label(self.tela7, textvariable=resultado)
        label_resultado.pack(pady=10)

        #BOTÃO CONTEXTUALIZAÇÃO
        btn_contexto = tk.Button(self.tela7, text="Contextualização da formula", command=self.ir_para_tela19)
        btn_contexto.pack(pady=10)

        #CRIANDO O FRAME PARA BOTOES DE EXEMPLOS PRATICOS
        frame2 = tk.Frame(self.tela7)
        frame2.pack()
        #CRIANDO BOTOES
        botao_tela20 = tk.Button(frame2, text="Exemplo Prático 1", command=self.ir_para_tela20)
        botao_tela21 = tk.Button(frame2, text="Exemplo Prático 2", command=self.ir_para_tela21)
        botao_tela22 = tk.Button(frame2, text="Exemplo Prático 3", command=self.ir_para_tela22)
        botao_tela20.pack(side=tk.LEFT,padx=10, pady=10)
        botao_tela21.pack(side=tk.LEFT,padx=10, pady=10)
        botao_tela22.pack(side=tk.LEFT,padx=10, pady=10)

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela7, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom', pady=20)


    #CRIA A TELA 8 (Lei da gravitação Universal de Newton)
    def criar_tela8(self):

        self.tela8 = tk.Frame(self.root)
        self.tela8.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela8, text="Lei da gravitação Universal de Newton" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=15)

        #TEXTO INFORMATIVO DE TELA
        label6_1 = tk.Label(self.tela8, text="F = G * (m1 * m2) / d^2")
        label6_1.pack(pady=10)

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

        #TEXTO MASSA 1 CAMPO DE ENTRADA
        label_massa1 = tk.Label(self.tela8, text="Massa 1 (kg):")
        label_massa1.pack()

        entry_massa1 = ttk.Entry(self.tela8, width=12)
        entry_massa1.placeholder = "Insira a Massa 1"
        entry_massa1.insert(0, entry_massa1.placeholder)
        entry_massa1.bind("<FocusIn>", remover_placeholder)
        entry_massa1.bind("<FocusOut>", restaurar_placeholder)
        entry_massa1.pack()

        #TEXTO MASSA 2 CAMPO DE ENTRADA
        label_massa2 = tk.Label(self.tela8, text="Massa 2 (kg):")
        label_massa2.pack()

        entry_massa2 = ttk.Entry(self.tela8, width=12)
        entry_massa2.placeholder = "Insira a Massa 2"
        entry_massa2.insert(0, entry_massa2.placeholder)
        entry_massa2.bind("<FocusIn>", remover_placeholder)
        entry_massa2.bind("<FocusOut>", restaurar_placeholder)
        entry_massa2.pack()

        #TEXTO DISTANCIA CAMPO DE ENTRADA
        label_distancia = tk.Label(self.tela8, text="Distância (m):")
        label_distancia.pack()

        entry_distancia = ttk.Entry(self.tela8, width=12)
        entry_distancia.placeholder = "Insira a distância"
        entry_distancia.insert(0, entry_distancia.placeholder)
        entry_distancia.bind("<FocusIn>", remover_placeholder)
        entry_distancia.bind("<FocusOut>", restaurar_placeholder)
        entry_distancia.pack()

        #FUNÇÃO QUE CALCULA A LEI DE MOVIMENTO DE NEWTON
        def calcular():

            try:

                #USUARIO DEVE INSERIR OS VALORES AQUI
                massa1 = float(entry_massa1.get())
                massa2 = float(entry_massa2.get())
                distancia = float(entry_distancia.get())

                #CALCULANDO A FORÇA UTILIZANDO A FORMULA (6.67430 x 10^-11 N(m/kg)^2)
                constante_gravitacional = 0.0000000000667430
                forca = (constante_gravitacional * (massa1 * massa2)) / (distancia ** 2)

                # Exibir o resultado usando a variável de controle resultado
                resultado.set(f"Força ≈ {forca} N")

            except ValueError:
                resultado.set("Por favor, insira valores válidos / Preencha todos os valores.")
       

        #FUNÇÃO LIMPAR OS CAMPOS
        def limpar_campos():

            entry_massa1.delete(0, tk.END)
            entry_massa2.delete(0, tk.END)
            entry_distancia.delete(0, tk.END)
            resultado.set("")  #RESETA O CAMPO

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
        label_resultado = tk.Label(self.tela8, textvariable=resultado, padx=10, pady=10)
        label_resultado.pack()

        #BOTÃO CONTEXTUALIZAÇÃO
        btn_contexto = tk.Button(self.tela8, text="Contextualização da formula", command=self.ir_para_tela23)
        btn_contexto.pack(pady=10)

        #CRIANDO O FRAME PARA BOTOES DE EXEMPLOS PRATICOS
        frame2 = tk.Frame(self.tela8)
        frame2.pack()
        #CRIANDO BOTOES
        botao_tela20 = tk.Button(frame2, text="Exemplo Prático 1", command=self.ir_para_tela24)
        botao_tela21 = tk.Button(frame2, text="Exemplo Prático 2", command=self.ir_para_tela25)
        botao_tela22 = tk.Button(frame2, text="Exemplo Prático 3", command=self.ir_para_tela26)
        botao_tela20.pack(side=tk.LEFT,padx=10, pady=10)
        botao_tela21.pack(side=tk.LEFT,padx=10, pady=10)
        botao_tela22.pack(side=tk.LEFT,padx=10)

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela8, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom', pady=10)


    #CRIA A TELA 9 (Lei de Coulomb - REMOVIDO)
    def criar_tela9(self):

        self.tela9 = tk.Frame(self.root)
        self.tela9.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela9, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=90)


    #CRIA A TELA 10 (Energia cinética)
    def criar_tela10(self):

        self.tela10 = tk.Frame(self.root)
        self.tela10.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela10, text="Energia cinética" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=15)

        #TEXTO INFORMATIVO DE TELA
        label6_1 = tk.Label(self.tela10, text="Ec = m . v² / 2")
        label6_1.pack(pady=10)

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

        #TEXTO MASSA DO CAMPO DE ENTRADA
        label_massa = tk.Label(self.tela10, text="Massa (kg):")
        label_massa.pack()

        entry_massa = ttk.Entry(self.tela10)
        entry_massa.placeholder = "Insira a massa"
        entry_massa.insert(0, entry_massa.placeholder)
        entry_massa.bind("<FocusIn>", remover_placeholder)
        entry_massa.bind("<FocusOut>", restaurar_placeholder)
        entry_massa.pack()

        #TEXTO FORÇA DO CAMPO DE ENTRADA
        entry_velocidade = tk.Label(self.tela10, text="Velocidade (m/s):")
        entry_velocidade.pack()

        entry_velocidade = ttk.Entry(self.tela10)
        entry_velocidade.placeholder = "Insira a força"
        entry_velocidade.insert(0, entry_velocidade.placeholder)
        entry_velocidade.bind("<FocusIn>", remover_placeholder)
        entry_velocidade.bind("<FocusOut>", restaurar_placeholder)
        entry_velocidade.pack()

        # Função para calcular a energia cinética
        def calcular():
            try:
                # Obter valores inseridos pelo usuário
                massa = float(entry_massa.get())
                velocidade = float(entry_velocidade.get())

                # Calcular a energia cinética
                energia_cinetica = 0.5 * massa * (velocidade ** 2)

                # Exibir o resultado na label de resultado
                resultado.set(f"Energia Cinética (Ec): {energia_cinetica:.2f} Joules")

            except ValueError:
                resultado.set("Por favor, insira valores válidos / Preencha todos os campos.")


        #FUNÇÃO LIMPAR OS CAMPOS
        def limpar_campos():
            entry_massa.delete(0, tk.END)
            entry_velocidade.delete(0, tk.END)
            resultado.set("")  # Limpa o resultado

        #CRIANDO O FRAME PARA BOTOES CALCULAR E LIMPAR FICAREM ALINHADOS
        frame1 = tk.Frame(self.tela10)
        frame1.pack()
        #CRIANDO BOTOES
        botao_calcular = tk.Button(frame1, text="Calcular", command=calcular)
        botao_limpar = tk.Button(frame1, text="Limpar", command=limpar_campos)
        botao_calcular.pack(side=tk.LEFT,padx=10)
        botao_limpar.pack(side=tk.LEFT,padx=10, pady=15)

        #TEXTO PARA INFORMAR O RESULTADO DA OPERAÇÃO
        resultado = tk.StringVar()
        label_resultado = tk.Label(self.tela10, textvariable=resultado)
        label_resultado.pack()

        #BOTÃO CONTEXTUALIZAÇÃO
        btn_contexto = tk.Button(self.tela10, text="Contextualização da formula", command=self.ir_para_tela27)
        btn_contexto.pack(pady=15)

        #CRIANDO O FRAME PARA BOTOES DE EXEMPLOS PRATICOS
        frame2 = tk.Frame(self.tela10)
        frame2.pack()
        #CRIANDO BOTOES
        botao_tela20 = tk.Button(frame2, text="Exemplo Prático 1", command=self.ir_para_tela28)
        botao_tela21 = tk.Button(frame2, text="Exemplo Prático 2", command=self.ir_para_tela29)
        botao_tela22 = tk.Button(frame2, text="Exemplo Prático 3", command=self.ir_para_tela30)
        botao_tela20.pack(side=tk.LEFT,padx=10, pady=20)
        botao_tela21.pack(side=tk.LEFT,padx=10, pady=10)
        botao_tela22.pack(side=tk.LEFT,padx=10)

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela10, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=15)


    #CRIA A TELA 11 (Energia Potencial Gravitacional)
    def criar_tela11(self):

        self.tela11 = tk.Frame(self.root)
        self.tela11.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela11, text="Energia Potencial Gravitacional" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=30)

        #TEXTO INFORMATIVO DE TELA
        label6_1 = tk.Label(self.tela11, text='EPG = m * g * h')
        label6_1.pack(pady=15)

        #TEXTO INFORMATIVO DE TELA
        label6_1 = tk.Label(self.tela11, text='Sendo que g pode variar entre 9.8, 9.81 e 10 m/s²')
        label6_1.pack(pady=15)

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

        #TEXTO MASSA DO CAMPO DE ENTRADA
        label_massa = tk.Label(self.tela11, text="[m] Massa (kg):")
        label_massa.pack()

        entry_massa = ttk.Entry(self.tela11)
        entry_massa.placeholder = "Insira a massa (kg)"
        entry_massa.insert(0, entry_massa.placeholder)
        entry_massa.bind("<FocusIn>", remover_placeholder)
        entry_massa.bind("<FocusOut>", restaurar_placeholder)
        entry_massa.pack()

        #TEXTO MASSA DO CAMPO DE ENTRADA
        label_gravidade = tk.Label(self.tela11, text="[g] Aceleração da gravidade (m/s²):")
        label_gravidade.pack()

        entry_gravidade = ttk.Entry(self.tela11)
        entry_gravidade.placeholder = "Insira a gravidade (m/s²)"
        entry_gravidade.insert(0, entry_gravidade.placeholder)
        entry_gravidade.bind("<FocusIn>", remover_placeholder)
        entry_gravidade.bind("<FocusOut>", restaurar_placeholder)
        entry_gravidade.pack()

        #TEXTO FORÇA DO CAMPO DE ENTRADA
        label_altura = tk.Label(self.tela11, text="[h] Altura (m):")
        label_altura.pack()

        entry_altura = ttk.Entry(self.tela11)
        entry_altura.placeholder = "Insira a altura (m)"
        entry_altura.insert(0, entry_altura.placeholder)
        entry_altura.bind("<FocusIn>", remover_placeholder)
        entry_altura.bind("<FocusOut>", restaurar_placeholder)
        entry_altura.pack()

        # Função para calcular a energia potencial gravitacional
        def calcular():
            try:
                # Obter valores inseridos pelo usuário
                massa = float(entry_massa.get())
                altura = float(entry_altura.get())
                gravidade = float(entry_gravidade.get())

                # Calcular a energia potencial gravitacional
                energia_potencial = massa * gravidade * altura

                # Exibir o resultado na label de resultado
                resultado.set(f"Energia Potencial Gravitacional: {energia_potencial:.2f} Joules")

            except ValueError:
                resultado.set("Por favor, insira valores válidos.")


        #FUNÇÃO LIMPAR OS CAMPOS
        def limpar_campos():
            entry_massa.delete(0, tk.END)
            entry_gravidade.delete(0, tk.END)
            entry_altura.delete(0, tk.END)
            resultado.set("")  #RESETA OS CAMPOS

        #CRIANDO O FRAME PARA BOTOES CALCULAR E LIMPAR FICAREM ALINHADOS
        frame1 = tk.Frame(self.tela11)
        frame1.pack()
        #CRIANDO BOTOES
        botao_calcular = tk.Button(frame1, text="Calcular", command=calcular)
        botao_limpar = tk.Button(frame1, text="Limpar", command=limpar_campos)
        botao_calcular.pack(side=tk.LEFT,padx=10, pady=10)
        botao_limpar.pack(side=tk.LEFT,padx=10, pady=10)

        #TEXTO PARA INFORMAR O RESULTADO DA OPERAÇÃO
        resultado = tk.StringVar()
        label_resultado = tk.Label(self.tela11, textvariable=resultado)
        label_resultado.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela11, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=35)


    #CRIA A TELA 12 (Lei da conservação de Energia Mecânica   ALTERAR)
    def criar_tela12(self):

        self.tela12 = tk.Frame(self.root)
        self.tela12.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela12, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=90)


    #CRIA A TELA 13 (Lei de Hooke)
    def criar_tela13(self):

        self.tela13 = tk.Frame(self.root)
        self.tela13.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela13, text="Lei de Hooke" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=30)

        #TEXTO INFORMATIVO DE TELA
        label6_1 = tk.Label(self.tela13, text='F = -k * x')
        label6_1.pack(pady=15)

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

        #TEXTO MASSA DO CAMPO DE ENTRADA
        label_constante_elastica = tk.Label(self.tela13, text="[k] Constante Elástica (N/m):")
        label_constante_elastica.pack()

        entry_constante_elastica = ttk.Entry(self.tela13)
        entry_constante_elastica.placeholder = "Insira a Constante Elástica"
        entry_constante_elastica.insert(0, entry_constante_elastica.placeholder)
        entry_constante_elastica.bind("<FocusIn>", remover_placeholder)
        entry_constante_elastica.bind("<FocusOut>", restaurar_placeholder)
        entry_constante_elastica.pack()

        #TEXTO MASSA DO CAMPO DE ENTRADA
        label_deformacao = tk.Label(self.tela13, text="[x] Deformação (m):")
        label_deformacao.pack()

        entry_deformacao = ttk.Entry(self.tela13)
        entry_deformacao.placeholder = "Insira a Deformação"
        entry_deformacao.insert(0, entry_deformacao.placeholder)
        entry_deformacao.bind("<FocusIn>", remover_placeholder)
        entry_deformacao.bind("<FocusOut>", restaurar_placeholder)
        entry_deformacao.pack()

        # Função para calcular a força de acordo com a Lei de Hooke
        def calcular():
            try:
                # Obter valores inseridos pelo usuário
                constante_elastica = float(entry_constante_elastica.get())
                deformacao = float(entry_deformacao.get())

                # Calcular a força usando a Lei de Hooke
                forca = -constante_elastica * deformacao

                # Exibir o resultado na label de resultado
                resultado.set(f"Força: {forca:.2f} N")

            except ValueError:
                resultado.set("Por favor, insira valores válidos.")

        #FUNÇÃO LIMPAR OS CAMPOS
        def limpar_campos():
            entry_constante_elastica.delete(0, tk.END)
            entry_deformacao.delete(0, tk.END)
            resultado.set("")  #RESETA OS CAMPOS

        #CRIANDO O FRAME PARA BOTOES CALCULAR E LIMPAR FICAREM ALINHADOS
        frame1 = tk.Frame(self.tela13)
        frame1.pack()
        #CRIANDO BOTOES
        botao_calcular = tk.Button(frame1, text="Calcular", command=calcular)
        botao_limpar = tk.Button(frame1, text="Limpar", command=limpar_campos)
        botao_calcular.pack(side=tk.LEFT,padx=10, pady=10)
        botao_limpar.pack(side=tk.LEFT,padx=10, pady=10)

        #TEXTO PARA INFORMAR O RESULTADO DA OPERAÇÃO
        resultado = tk.StringVar()
        label_resultado = tk.Label(self.tela13, textvariable=resultado)
        label_resultado.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela13, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=45)


    #CRIA A TELA 14 (Lei de Snell)
    def criar_tela14(self):

        self.tela14 = tk.Frame(self.root)
        self.tela14.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela14, text="Lei de Snell" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=30)

        #TEXTO INFORMATIVO DE TELA
        label6_1 = tk.Label(self.tela14, text='n1.sen(i) = n2.sen(r)')
        label6_1.pack(pady=15)

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

        #TEXTO MASSA DO CAMPO DE ENTRADA
        label_indice_refracao1 = tk.Label(self.tela14, text="Índice de Refração 1:")
        label_indice_refracao1.pack()

        entry_indice_refracao1 = ttk.Entry(self.tela14)
        entry_indice_refracao1.placeholder = "Insira a Refração 1"
        entry_indice_refracao1.insert(0, entry_indice_refracao1.placeholder)
        entry_indice_refracao1.bind("<FocusIn>", remover_placeholder)
        entry_indice_refracao1.bind("<FocusOut>", restaurar_placeholder)
        entry_indice_refracao1.pack()

        #TEXTO MASSA DO CAMPO DE ENTRADA
        label_indice_refracao2 = tk.Label(self.tela14, text="Índice de Refração 2:")
        label_indice_refracao2.pack()

        entry_indice_refracao2 = ttk.Entry(self.tela14)
        entry_indice_refracao2.placeholder = "Insira a Refração 2"
        entry_indice_refracao2.insert(0, entry_indice_refracao2.placeholder)
        entry_indice_refracao2.bind("<FocusIn>", remover_placeholder)
        entry_indice_refracao2.bind("<FocusOut>", restaurar_placeholder)
        entry_indice_refracao2.pack()

        #TEXTO FORÇA DO CAMPO DE ENTRADA
        label_angulo_incidencia= tk.Label(self.tela14, text="Ângulo de Incidência (graus):")
        label_angulo_incidencia.pack()

        entry_angulo_incidencia = ttk.Entry(self.tela14)
        entry_angulo_incidencia.placeholder = "Insira o Ângulo de Incidência"
        entry_angulo_incidencia.insert(0, entry_angulo_incidencia.placeholder)
        entry_angulo_incidencia.bind("<FocusIn>", remover_placeholder)
        entry_angulo_incidencia.bind("<FocusOut>", restaurar_placeholder)
        entry_angulo_incidencia.pack()

        # Função para calcular o ângulo de refração de acordo com a Lei de Snell
        def calcular():
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

        #FUNÇÃO LIMPAR OS CAMPOS
        def limpar_campos():
            entry_indice_refracao1.delete(0, tk.END)
            entry_indice_refracao2.delete(0, tk.END)
            entry_angulo_incidencia.delete(0, tk.END)
            resultado.set("")  #RESETA OS CAMPOS

        #CRIANDO O FRAME PARA BOTOES CALCULAR E LIMPAR FICAREM ALINHADOS
        frame1 = tk.Frame(self.tela14)
        frame1.pack()
        #CRIANDO BOTOES
        botao_calcular = tk.Button(frame1, text="Calcular", command=calcular)
        botao_limpar = tk.Button(frame1, text="Limpar", command=limpar_campos)
        botao_calcular.pack(side=tk.LEFT,padx=10, pady=10)
        botao_limpar.pack(side=tk.LEFT,padx=10, pady=10)

        #TEXTO PARA INFORMAR O RESULTADO DA OPERAÇÃO
        resultado = tk.StringVar()
        label_resultado = tk.Label(self.tela14, textvariable=resultado)
        label_resultado.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela14, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=35)


    #CRIA A TELA 15 (Lei de Ohm)
    def criar_tela15(self):

        self.tela15 = tk.Frame(self.root)
        self.tela15.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela15, text="Lei de Ohm" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=30)

        #TEXTO INFORMATIVO DE TELA
        label6_1 = tk.Label(self.tela15, text='V = I x R')
        label6_1.pack(pady=15)

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

        #TEXTO MASSA DO CAMPO DE ENTRADA
        label_corrente = tk.Label(self.tela15, text="Corrente (A):")
        label_corrente.pack()

        entry_corrente = ttk.Entry(self.tela15)
        entry_corrente.placeholder = "Insira a Corrente"
        entry_corrente.insert(0, entry_corrente.placeholder)
        entry_corrente.bind("<FocusIn>", remover_placeholder)
        entry_corrente.bind("<FocusOut>", restaurar_placeholder)
        entry_corrente.pack()

        #TEXTO MASSA DO CAMPO DE ENTRADA
        label_resistencia = tk.Label(self.tela15, text="Resistência (Ω):")
        label_resistencia.pack()

        entry_resistencia = ttk.Entry(self.tela15)
        entry_resistencia.placeholder = "Insira a Resistência"
        entry_resistencia.insert(0, entry_resistencia.placeholder)
        entry_resistencia.bind("<FocusIn>", remover_placeholder)
        entry_resistencia.bind("<FocusOut>", restaurar_placeholder)
        entry_resistencia.pack()

        # Função para calcular a tensão elétrica de acordo com a Lei de Ohm
        def calcular():
            try:
                # Obter valores inseridos pelo usuário
                corrente = float(entry_corrente.get())
                resistencia = float(entry_resistencia.get())

                # Calcular a tensão elétrica usando a Lei de Ohm
                tensao = corrente * resistencia

                # Exibir o resultado na label de resultado
                resultado.set(f"Tensão Elétrica (V): {tensao:.2f} V")

            except ValueError:
                resultado.set("Por favor, insira valores válidos.")

        # Função para limpar os campos
        def limpar_campos():
            entry_corrente.delete(0, tk.END)
            entry_resistencia.delete(0, tk.END)
            resultado.set("")  # Resetar o campo de resultado

        #CRIANDO O FRAME PARA BOTOES CALCULAR E LIMPAR FICAREM ALINHADOS
        frame1 = tk.Frame(self.tela15)
        frame1.pack()
        #CRIANDO BOTOES
        botao_calcular = tk.Button(frame1, text="Calcular", command=calcular)
        botao_limpar = tk.Button(frame1, text="Limpar", command=limpar_campos)
        botao_calcular.pack(side=tk.LEFT,padx=10, pady=10)
        botao_limpar.pack(side=tk.LEFT,padx=10, pady=10)

        #TEXTO PARA INFORMAR O RESULTADO DA OPERAÇÃO
        resultado = tk.StringVar()
        label_resultado = tk.Label(self.tela15, textvariable=resultado)
        label_resultado.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela15, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=45)


    #CRIA A TELA 16 (Movimento Retilíneo Uniforme)
    def criar_tela16(self):

        self.tela16 = tk.Frame(self.root)
        self.tela16.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela16, text="Movimento Retilíneo Uniforme" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=30)

        #TEXTO INFORMATIVO DE TELA
        label6_1 = tk.Label(self.tela16, text='S(t) = S₀ + v . t')
        label6_1.pack(pady=15)

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
                
        #TEXTO MASSA DO CAMPO DE ENTRADA
        label_S0 = tk.Label(self.tela16, text="[S₀] Posição Inicial ():")
        label_S0.pack()

        entry_S0 = ttk.Entry(self.tela16)
        entry_S0.placeholder = "Insira a Posição Inicial ()"
        entry_S0.insert(0, entry_S0.placeholder)
        entry_S0.bind("<FocusIn>", remover_placeholder)
        entry_S0.bind("<FocusOut>", restaurar_placeholder)
        entry_S0.pack()

        #TEXTO MASSA DO CAMPO DE ENTRADA
        label_v = tk.Label(self.tela16, text="[] Velocidade (v):")
        label_v.pack()

        entry_v = ttk.Entry(self.tela16)
        entry_v.placeholder = "Insira a Velocidade ()"
        entry_v.insert(0, entry_v.placeholder)
        entry_v.bind("<FocusIn>", remover_placeholder)
        entry_v.bind("<FocusOut>", restaurar_placeholder)
        entry_v.pack()

        #TEXTO FORÇA DO CAMPO DE ENTRADA
        label_t = tk.Label(self.tela16, text="[] Tempo (t):")
        label_t.pack()

        entry_t = ttk.Entry(self.tela16)
        entry_t.placeholder = "Insira o Tempo ()"
        entry_t.insert(0, entry_t.placeholder)
        entry_t.bind("<FocusIn>", remover_placeholder)
        entry_t.bind("<FocusOut>", restaurar_placeholder)
        entry_t.pack()

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
                resultado.set("Insira valores válidos em todas as entradas / Preencha todos os campos")

        #FUNÇÃO LIMPAR OS CAMPOS
        def limpar_campos():
            entry_S0.delete(0, tk.END)
            entry_v.delete(0, tk.END)
            entry_t.delete(0, tk.END)
            resultado.set("")  #RESETA OS CAMPOS

        #CRIANDO O FRAME PARA BOTOES CALCULAR E LIMPAR FICAREM ALINHADOS
        frame1 = tk.Frame(self.tela16)
        frame1.pack()
        #CRIANDO BOTOES
        botao_calcular = tk.Button(frame1, text="Calcular", command=calcular)
        botao_limpar = tk.Button(frame1, text="Limpar", command=limpar_campos)
        botao_calcular.pack(side=tk.LEFT,padx=10, pady=10)
        botao_limpar.pack(side=tk.LEFT,padx=10, pady=10)

        #TEXTO PARA INFORMAR O RESULTADO DA OPERAÇÃO
        resultado = tk.StringVar()
        label_resultado = tk.Label(self.tela16, textvariable=resultado)
        label_resultado.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela16, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=40)


    #CRIA A TELA 17 (Velocidade média)
    def criar_tela17(self):

        self.tela17 = tk.Frame(self.root)
        self.tela17.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela17, text="Velocidade média" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=30)

        #TEXTO INFORMATIVO DE TELA
        label6_1 = tk.Label(self.tela17, text='Vm = ΔS / Δt')
        label6_1.pack(pady=15)

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
                
        #TEXTO MASSA DO CAMPO DE ENTRADA
        label_delta_s = tk.Label(self.tela17, text="[ΔS] Variação de Posição (m):")
        label_delta_s.pack()

        entry_delta_s = ttk.Entry(self.tela17)
        entry_delta_s.placeholder = "Insira a Variação de Posição (m)"
        entry_delta_s.insert(0, entry_delta_s.placeholder)
        entry_delta_s.bind("<FocusIn>", remover_placeholder)
        entry_delta_s.bind("<FocusOut>", restaurar_placeholder)
        entry_delta_s.pack()

        #TEXTO MASSA DO CAMPO DE ENTRADA
        label_delta_t = tk.Label(self.tela17, text="[Δt] Variação de Tempo (s):")
        label_delta_t.pack()

        entry_delta_t = ttk.Entry(self.tela17)
        entry_delta_t.placeholder = "Insira a Variação de Tempo (s)"
        entry_delta_t.insert(0, entry_delta_t.placeholder)
        entry_delta_t.bind("<FocusIn>", remover_placeholder)
        entry_delta_t.bind("<FocusOut>", restaurar_placeholder)
        entry_delta_t.pack()

        #Função para calcular a velocidade média
        def calcular():
            try:
                delta_s = float(entry_delta_s.get())
                delta_t = float(entry_delta_t.get())

                #Validar se o índice de refração 2 é zero
                if delta_t == 0:
                    resultado.set("A Variação de Tempo não pode ser zero (0).")
                    return

                velocidade_media = delta_s / delta_t
                
                resultado.set(f"Velocidade Média: {velocidade_media:.2f} m/s")

            except ValueError:

                resultado.set("Por favor, insira valores válidos / Preencha todos os campos.")

        #FUNÇÃO LIMPAR OS CAMPOS
        def limpar_campos():
            entry_delta_s.delete(0, tk.END)
            entry_delta_t.delete(0, tk.END)
            resultado.set("")  #RESETA OS CAMPOS
            
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
        btn_tela_anterior.pack(side='bottom',pady=40)


    #CRIA A TELA 18 (Densidade)
    def criar_tela18(self):

        self.tela18 = tk.Frame(self.root)
        self.tela18.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela18, text="Densidade" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=30)

        #TEXTO INFORMATIVO DE TELA
        label6_1 = tk.Label(self.tela18, text='d = m / v')
        label6_1.pack(pady=15)

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
                
        #TEXTO MASSA DO CAMPO DE ENTRADA
        label_massa = tk.Label(self.tela18, text="[m] Massa (kg):")
        label_massa.pack()

        entry_massa = ttk.Entry(self.tela18)
        entry_massa.placeholder = "Insira a Massa (kg)"
        entry_massa.insert(0, entry_massa.placeholder)
        entry_massa.bind("<FocusIn>", remover_placeholder)
        entry_massa.bind("<FocusOut>", restaurar_placeholder)
        entry_massa.pack()

        #TEXTO MASSA DO CAMPO DE ENTRADA
        label_delta_t = tk.Label(self.tela18, text="[v] Volume (m³):")
        label_delta_t.pack()

        entry_volume = ttk.Entry(self.tela18)
        entry_volume.placeholder = "Insira o Volume (m³)"
        entry_volume.insert(0, entry_volume.placeholder)
        entry_volume.bind("<FocusIn>", remover_placeholder)
        entry_volume.bind("<FocusOut>", restaurar_placeholder)
        entry_volume.pack()

        # Função para calcular a densidade
        def calcular():
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

        #FUNÇÃO LIMPAR OS CAMPOS
        def limpar_campos():
            entry_massa.delete(0, tk.END)
            entry_volume.delete(0, tk.END)
            resultado.set("")  #RESETA OS CAMPOS

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
        btn_tela_anterior.pack(side='bottom',pady=40)


######################################## TELAS CONTEXTUALIZAÇÃO E EXEMPLOS 1, 2, 3 #############################################################################################################################################################

    #CRIA A TELA 19 (CONTEXTUALIZAÇÃO - Lei de Movimento de Newton (Segunda Lei))
    def criar_tela19(self):

        self.tela19 = tk.Frame(self.root)
        self.tela19.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela19, text="CONTEXTUALIZAÇÃO DA FORMULA" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=20)

        #TEXTO INFORMATIVO DE TELA
        label6_1 = tk.Label(self.tela19, text="F = m . a")
        label6_1.pack(pady=10)

        #TEXTO TELA CONTEXTUALIZAÇÃO
        texto = """
            A Lei do Movimento de Newton, formulada por Isaac Newton no século XVII, é uma 
        fórmula fundamental na física clássica pois descreve a relação entre a força aplicada 
        a um objeto e sua subsequente aceleração. Essa lei é amplamente utilizada em diversos
        contextos, desde a previsão do movimento dos planetas no sistema solar até o projeto
        de espaçonaves e na compreensão dos movimentos de objetos em nosso dia a dia.

            No cotidiano, a segunda lei de Newton é frequentemente aplicada na engenharia, como
        no desenvolvimento de carros, aviões e estruturas construtivas. Ela é essencial para
        calcular como os objetos se moverão sob diferentes influências de forças, como gravidade
        e tração. Além disso, essa lei também é usada na astronomia para prever as órbitas dos
        planetas e nas ciências biológicas para entender o movimento dos corpos e músculos humanos. 
        Portanto, a Lei do Movimento de Newton representa uma ferramenta indispensável para
        compreender e prever os movimentos em diversas áreas da ciência e engenharia.
        """

        #RÓTULO DO TEXTO
        label4_1 = tk.Label(self.tela19, text=texto, justify="center", padx=10, pady=10, font=('Arial', 12))
        label4_1.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela19, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=40)


    #CRIA A TELA 20 (EXEMPLO PRATICO 1 - Lei de Movimento de Newton (Segunda Lei))
    def criar_tela20(self):

        self.tela20 = tk.Frame(self.root)
        self.tela20.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela20, text="EXEMPLO PRÁTICO 1" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=30)

        #TEXTO INFORMATIVO DE TELA
        label6_1 = tk.Label(self.tela20, text="F = m . a")
        label6_1.pack(pady=25)

        #TEXTO TELA OBJETIVO PRINCIPAL
        texto = """
        Qual a força exercida por um carro de 900 kg que é empurrado
        por duas pessoas a uma aceleração de 2 m/s²)?

        Resolução:

        F = 900kg * 2m/s²

        Multiplicando 900 por 2:

        F = 1.800N
        """

        #RÓTULO DO TEXTO
        label4_1 = tk.Label(self.tela20, text=texto, justify="center", padx=10, pady=10, font=('Arial', 12))
        label4_1.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela20, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=40)


    #CRIA A TELA 21 (EXEMPLO PRATICO 2 - Lei de Movimento de Newton (Segunda Lei))
    def criar_tela21(self):

        self.tela21 = tk.Frame(self.root)
        self.tela21.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela21, text="EXEMPLO PRÁTICO 2" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=30)

        #TEXTO INFORMATIVO DE TELA
        label6_1 = tk.Label(self.tela21, text="F = m . a")
        label6_1.pack(pady=25)

        #TEXTO TELA OBJETIVO PRINCIPAL
        texto = """
        Suponhamos que você esteja em um elevador que está subindo com uma aceleração
        de 2 m/s² e sua massa é de 75 kg. Determine a força que você irá sentir.

        Resolução:
    
        F = 75kg * 2m/s²

        Multiplicando 75 * 2:

        F = 150N
        """

        #RÓTULO DO TEXTO
        label4_1 = tk.Label(self.tela21, text=texto, justify="center", padx=10, pady=10, font=('Arial', 12))
        label4_1.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela21, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=40)


    #CRIA A TELA 22 (EXEMPLO PRATICO 3 - Lei de Movimento de Newton (Segunda Lei))
    def criar_tela22(self):

        self.tela22 = tk.Frame(self.root)
        self.tela22.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela22, text="EXEMPLO PRÁTICO 3" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=20)

        #TEXTO INFORMATIVO DE TELA
        label6_1 = tk.Label(self.tela22, text="F = m . a")
        label6_1.pack(pady=15)

        #TEXTO TELA OBJETIVO PRINCIPAL
        texto = """
        Suponhamos que você tenha um trem de carga com uma massa total de 90000 kg
        e ele esteja desacelerando a uma taxa de 2,5 m/s² devido aos freios.
        Determine a força considerando que o trem está desacelerando.

        Resolução:

        F = 90000kg * (-2,5m/s²)

        Multiplicando 90000 por -2,5:

        F = -225.000N
        """

        #RÓTULO DO TEXTO
        label4_1 = tk.Label(self.tela22, text=texto, justify="center", padx=10, pady=10, font=('Arial', 12))
        label4_1.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela22, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=30)


    #CRIA A TELA  23(CONTEXTUALIZAÇÃO - Lei da gravitação Universal de Newton)
    def criar_tela23(self):

        self.tela23 = tk.Frame(self.root)
        self.tela23.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela23, text="CONTEXTUALIZAÇÃO DA FORMULA" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=10)

        #TEXTO INFORMATIVO DE TELA
        label6_1 = tk.Label(self.tela23, text="F = G * (m1 * m2) / d²")
        label6_1.pack(pady=5)

        #TEXTO TELA OBJETIVO PRINCIPAL
        texto = """
            O princípio Lei da Gravitação Universal foi formulada por Isaac Newton em 1687 em seu
        livro "Principia Mathematica". Ela representou uma revolução na compreensão da
        física, pois unificou os movimentos celestes e terrestres sob um único conjunto de leis.
        A fórmula descreve a força de atração gravitacional entre duas massas, m1 e m2, separadas
        por uma distância d. Essa força é representada por F. 
        
            A constante G é uma constante fundamental da física e, na época de Newton, sua precisão
        experimental não era conhecida com detalhes, com o desenvolvimento da ciência, o valor de
        G foi determinado com alta precisão.

            A parte mais notável da Lei da Gravitação Universal é que a força gravitacional entre duas
        massas é inversamente proporcional ao quadrado da distância entre elas (d²). Isso significa
        que, se você dobrar a distância entre as massas, a força gravitacional se tornará um quarto
        do valor original. Destaca-se, a importância da massa na atração gravitacional. Quanto maior
        a massa dos objetos, maior será a força gravitacional entre eles. Isso é especialmente
        evidente em sistemas como o sistema solar, onde a massa do Sol exerce uma atração
        gravitacional sobre os planetas, mantendo-os em órbita. Com a fórmula, se pode descrever
        com precisão os movimentos de corpos celestes, permitindo a previsão de eclipses, trajetórias
        de satélites e o comportamento dos planetas.
        """

        #RÓTULO DO TEXTO
        label4_1 = tk.Label(self.tela23, text=texto, justify="center", padx=10, pady=10, font=('Arial', 12))
        label4_1.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela23, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=10)


    #CRIA A TELA 24 (EXEMPLO PRATICO 1 - Lei da gravitação Universal de Newton)
    def criar_tela24(self):

        self.tela24 = tk.Frame(self.root)
        self.tela24.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela24, text="EXEMPLO PRÁTICO 1" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=30)

        #TEXTO INFORMATIVO DE TELA
        label6_1 = tk.Label(self.tela24, text="F = G * (m1 * m2) / d²")
        label6_1.pack(pady=25)

        #TEXTO TELA OBJETIVO PRINCIPAL
        texto = """
        Qual é a força gravitacional entre a Terra (massa = 5,972 x 10^24 kg) e
        uma maçã (massa = 0,1kg) quando a maçã está a 1 metro da superfície da Terra?

        Resolução:

        F = 6,67430x10^-11 m³/kgs² * (5,972 x 10^24 kg * 0,1 kg) / (1 m)²

        Calculando o resultado:

        F ≈ 0,981 N
        """

        #RÓTULO DO TEXTO
        label4_1 = tk.Label(self.tela24, text=texto, justify="center", padx=10, pady=10, font=('Arial', 12))
        label4_1.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela24, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=40)


    #CRIA A TELA 25 (EXEMPLO PRATICO 2 - Lei da gravitação Universal de Newton))
    def criar_tela25(self):

        self.tela25 = tk.Frame(self.root)
        self.tela25.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela25, text="EXEMPLO PRÁTICO 2" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=30)

        #TEXTO TELA OBJETIVO PRINCIPAL
        texto = """
        Qual é a força gravitacional entre a Lua (massa = 7,342x10^22 kg) e uma nave
        espacial (massa = 1000 kg) quando estão a 384,400,000 m de distância?

        Resolução:

        F = 6,67430x10^-11 m³/kgs² * (7,342x10^22 kg * 1000 kg) / (384.400.000m)²

        Calculando o resultado:

        F ≈ 1,993x10^5 N
        """

        #RÓTULO DO TEXTO
        label4_1 = tk.Label(self.tela25, text=texto, justify="center", padx=10, pady=10, font=('Arial', 12))
        label4_1.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela25, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=40)


    #CRIA A TELA 26 (EXEMPLO PRATICO 3 - Lei da gravitação Universal de Newton))
    def criar_tela26(self):

        self.tela26 = tk.Frame(self.root)
        self.tela26.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela26, text="EXEMPLO PRÁTICO 3" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=30)

        #TEXTO TELA OBJETIVO PRINCIPAL
        texto = """
        Qual é a força gravitacional entre dois carros de 1500 kg cada um, estacionados
        a uma distância de 2 metros um do outro?

        Solução:

        F = 6,67430x10^-11 m³/kgs² * (1500kg * 1500kg) / (2m)²

        Calculando o resultado:

        F ≈ 0.0000375429 N
        """

        #RÓTULO DO TEXTO
        label4_1 = tk.Label(self.tela26, text=texto, justify="center", padx=10, pady=10, font=('Arial', 12))
        label4_1.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela26, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=40)


    #CRIA A TELA 27 (CONTEXTUALIZAÇÃO - Energia cinética)
    def criar_tela27(self):

        self.tela27 = tk.Frame(self.root)
        self.tela27.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela27, text="CONTEXTUALIZAÇÃO DA FORMULA" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=10)

        #TEXTO INFORMATIVO DE TELA
        label6_1 = tk.Label(self.tela27, text="Ec = m . v² / 2")
        label6_1.pack(pady=5)

        #TEXTO TELA OBJETIVO PRINCIPAL
        texto = """
            A cinética de energia é um conceito essencial na física que descreve a energia relacionada ao 
        movimento de um objeto. Essa forma de energia é extremamente importante em várias áreas da ciência e
        da engenharia, especialmente quando se trata de calcular e compreender o comportamento de sistemas em
        movimento. Em termos simples, a energia cinética depende diretamente da massa do objeto e de sua 
        velocidade. Isso significa que quanto mais pesado e mais rápido um objeto estiver se movendo, maior
        será sua energia cinética. Esse princípio é amplamente aplicado em campos como a mecânica, onde é
        utilizado para calcular a energia dos veículos em movimento, resolver problemas de colisão e até
        mesmo no funcionamento diário de veículos e máquinas.

            Além disso, a energia cinética também desempenha um papel crucial na compreensão da transferência de
        energia em sistemas físicos. Ela está intimamente relacionada à Lei da Conservação de Energia, que
        afirma que a quantidade total de energia em um sistema isolado permanece constante. Isso implica que
        a energia cinética pode ser transformada em outras formas de energia, como a potencial gravitacional
        associada à posição do objeto num campo gravitacional. Portanto, a energia em movimento desempenha um
        papel crucial ao examinar situações complicadas, abrangendo desde o funcionamento de máquinas e
        veículos até a explicação do comportamento de partículas em níveis subatômicos. Ela estabelece uma
        base primordial para compreender o mundo físico que nos cerca.
        """

        #RÓTULO DO TEXTO
        label4_1 = tk.Label(self.tela27, text=texto, justify="center", padx=10, pady=10, font=('Arial', 12))
        label4_1.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela27, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=20)


    #CRIA A TELA 28 (EXEMPLO PRATICO 1 - Energia cinética)
    def criar_tela28(self):

        self.tela28 = tk.Frame(self.root)
        self.tela28.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela28, text="EXEMPLO PRÁTICO 1" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=30)

        #TEXTO INFORMATIVO DE TELA
        label6_1 = tk.Label(self.tela28, text="Ec = m . v² / 2")
        label6_1.pack(pady=20)

        #TEXTO TELA OBJETIVO PRINCIPAL
        texto = """
        Imagine um corredor com uma massa de 70 kg correndo a uma velocidade constante de 8 m/s em
        um parque. Calcule a energia cinética do corredor.

        Resolução:

        Ec = 70 kg * (8 m/s)^2 / 2

        Ec = 2240.00J
        """

        #RÓTULO DO TEXTO
        label4_1 = tk.Label(self.tela28, text=texto, justify="left", padx=10, pady=10, font=('Arial', 12))
        label4_1.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela28, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=25)        


    #CRIA A TELA 29 (EXEMPLO PRATICO 2 - Energia cinética)
    def criar_tela29(self):

        self.tela29 = tk.Frame(self.root)
        self.tela29.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela29, text="EXEMPLO PRÁTICO 2" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=30)

        #TEXTO INFORMATIVO DE TELA
        label6_1 = tk.Label(self.tela29, text="Ec = m . v² / 2")
        label6_1.pack(pady=20)

        #TEXTO TELA OBJETIVO PRINCIPAL
        texto = """
        Um carro com uma massa de 1000 kg está viajando a uma velocidade de 25 m/s em
        uma estrada. Calcule a energia cinética do carro.

        Resolução:

        Ec = 1000 kg * (25 m/s)^2 / 2
        Ec = 31250.00J
        """

        #RÓTULO DO TEXTO
        label4_1 = tk.Label(self.tela29, text=texto, justify="left", padx=10, pady=10, font=('Arial', 12))
        label4_1.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela29, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=25) 


    #CRIA A TELA 30 (EXEMPLO PRATICO 3 - Energia cinética)
    def criar_tela30(self):

        self.tela30 = tk.Frame(self.root)
        self.tela30.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela30, text="EXEMPLO PRÁTICO 3" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=30)

        #TEXTO INFORMATIVO DE TELA
        label6_1 = tk.Label(self.tela30, text="Ec = m . v² / 2")
        label6_1.pack(pady=20)

        #TEXTO TELA OBJETIVO PRINCIPAL
        texto = """
        Um carro com uma massa de 1000 kg está viajando a uma velocidade de 25 m/s em
        uma estrada. Calcule a energia cinética do carro.

        Resolução:

        Ec = 1000 kg * (25 m/s)^2 / 2
        Ec = 31250.00J
        """

        #RÓTULO DO TEXTO
        label4_1 = tk.Label(self.tela30, text=texto, justify="left", padx=10, pady=10, font=('Arial', 12))
        label4_1.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela30, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=25) 


    #CRIA A TELA 31 ()
    def criar_tela31(self):

        self.tela31 = tk.Frame(self.root)
        self.tela31.pack()


    #CRIA A TELA 32 ()
    def criar_tela32(self):

        self.tela32 = tk.Frame(self.root)
        self.tela32.pack()


    #CRIA A TELA 33 ()
    def criar_tela33(self):

        self.tela33 = tk.Frame(self.root)
        self.tela33.pack()


    #CRIA A TELA 34  ()
    def criar_tela34(self):

        self.tela34 = tk.Frame(self.root)
        self.tela34.pack()


    #CRIA A TELA 35 ()
    def criar_tela35(self):

        self.tela35 = tk.Frame(self.root)
        self.tela35.pack()


    #CRIA A TELA 36 ()
    def criar_tela36(self):

        self.tela36 = tk.Frame(self.root)
        self.tela36.pack()


    #CRIA A TELA 37 ()
    def criar_tela37(self):

        self.tela37 = tk.Frame(self.root)
        self.tela37.pack()


    #CRIA A TELA 38 ()
    def criar_tela38(self):

        self.tela38 = tk.Frame(self.root)
        self.tela38.pack()


    #CRIA A TELA 39 ()
    def criar_tela39(self):

        self.tela39 = tk.Frame(self.root)
        self.tela39.pack()


    #CRIA A TELA 40 ()
    def criar_tela40(self):

        self.tela40 = tk.Frame(self.root)
        self.tela40.pack()


    #CRIA A TELA  ()
    def criar_tela41(self):

        self.tela41 = tk.Frame(self.root)
        self.tela41.pack()


    #CRIA A TELA  ()
    def criar_tela42(self):

        self.tela42 = tk.Frame(self.root)
        self.tela42.pack()


    #CRIA A TELA  ()
    def criar_tela43(self):

        self.tela43 = tk.Frame(self.root)
        self.tela43.pack()


    #CRIA A TELA 44 ()
    def criar_tela44(self):

        self.tela44 = tk.Frame(self.root)
        self.tela44.pack()

    #CRIA A TELA 45 ()
    def criar_tela45(self):

        self.tela45 = tk.Frame(self.root)
        self.tela45.pack()


    #CRIA A TELA 46 ()
    def criar_tela46(self):

        self.tela46 = tk.Frame(self.root)
        self.tela46.pack()


    #CRIA A TELA 47 ()
    def criar_tela47(self):

        self.tela47 = tk.Frame(self.root)
        self.tela47.pack()


    #CRIA A TELA 48 ()
    def criar_tela48(self):

        self.tela48 = tk.Frame(self.root)
        self.tela48.pack()

########################################## FUNÇÕES IR PARA OUTRA TELA ################################################################
    
    #FUNÇÃO IR PARA TELA 2 (OPÇÕES)
    def ir_para_tela2(self):

        self.tela1.destroy()
        self.criar_tela2()
        self.tela_atual = 2

    #FUNÇÃO IR PARA TELA 3 (PRINCIPAIS FORMULAS)
    def ir_para_tela3(self):

        self.tela2.destroy()
        self.criar_tela3()
        self.tela_atual = 3

    #FUNÇÃO IR PARA TELA 4 (OBJETIVO DO PROJETO)
    def ir_para_tela4(self):

        self.tela2.destroy()
        self.criar_tela4()
        self.tela_atual = 4
    
    #FUNÇÃO IR PARA TELA 5 (AGRADECIMENTOS E REFERENCIAS)
    def ir_para_tela5(self):

        self.tela2.destroy()
        self.criar_tela5()
        self.tela_atual = 5

    #FUNÇÃO IR PARA TELA 6 (GitHub do projeto)
    def ir_para_tela6(self):

        self.tela2.destroy()
        self.criar_tela6()
        self.tela_atual = 6

    #FUNÇÃO IR PARA TELA 7 (Energia Potencial Gravitacional)
    def ir_para_tela7(self):

        self.tela3.destroy()
        self.criar_tela7()
        self.tela_atual = 7

    #FUNÇÃO IR PARA TELA 8 (Lei da gravitação Universal de Newton)
    def ir_para_tela8(self):

        self.tela3.destroy()
        self.criar_tela8()
        self.tela_atual = 8

    #FUNÇÃO IR PARA TELA 9 (Lei de Coulomb)
    def ir_para_tela9(self):

        self.tela3.destroy()
        self.criar_tela9()
        self.tela_atual = 9

    #FUNÇÃO IR PARA TELA 10 (Energia cinética)
    def ir_para_tela10(self):

        self.tela3.destroy()
        self.criar_tela10()
        self.tela_atual = 10

    #FUNÇÃO IR PARA TELA 11 (Energia Potencial Gravitacional)
    def ir_para_tela11(self):

        self.tela3.destroy()
        self.criar_tela11()
        self.tela_atual = 11

    #FUNÇÃO IR PARA TELA 12 (Lei da conservação de Energia Mecânica)
    def ir_para_tela12(self):

        self.tela3.destroy()
        self.criar_tela12()
        self.tela_atual = 12

    #FUNÇÃO IR PARA TELA 13 (Lei de Hooke)
    def ir_para_tela13(self):

        self.tela3.destroy()
        self.criar_tela13()
        self.tela_atual = 13

    #FUNÇÃO IR PARA TELA 14 (Lei de Snell)
    def ir_para_tela14(self):

        self.tela3.destroy()
        self.criar_tela14()
        self.tela_atual = 14

    #FUNÇÃO IR PARA TELA 15 (Lei de Ohm)
    def ir_para_tela15(self):

        self.tela3.destroy()
        self.criar_tela15()
        self.tela_atual = 15

    #FUNÇÃO IR PARA TELA 16 (Distância em Movimento Uniforme)
    def ir_para_tela16(self):

        self.tela3.destroy()
        self.criar_tela16()
        self.tela_atual = 16

    #FUNÇÃO IR PARA TELA 17 (Velocidade média)
    def ir_para_tela17(self):

        self.tela3.destroy()
        self.criar_tela17()
        self.tela_atual = 17

    #FUNÇÃO IR PARA TELA 18 (Densidade)
    def ir_para_tela18(self):

        self.tela3.destroy()
        self.criar_tela18()
        self.tela_atual = 18

    #FUNÇÃO IR PARA TELA 19 (CONTEXUALIZAÇÃO - Lei de Movimento de Newton)
    def ir_para_tela19(self):

        self.tela7.destroy()
        self.criar_tela19()
        self.tela_atual = 19

    #FUNÇÃO IR PARA TELA 20 (EXEMPLO PRATICO 1 - Lei de Movimento de Newton)
    def ir_para_tela20(self):

        self.tela7.destroy()
        self.criar_tela20()
        self.tela_atual = 20

    #FUNÇÃO IR PARA TELA 21 (EXEMPLO PRATICO 2 - Lei de Movimento de Newton)
    def ir_para_tela21(self):

        self.tela7.destroy()
        self.criar_tela21()
        self.tela_atual = 21

    #FUNÇÃO IR PARA TELA 22 (EXEMPLO PRATICO 3 - Lei de Movimento de Newton)
    def ir_para_tela22(self):

        self.tela7.destroy()
        self.criar_tela22()
        self.tela_atual = 22

    #FUNÇÃO IR PARA TELA 23 (CONTEXUALIZAÇÃO - Lei da gravitação Universal de Newton)
    def ir_para_tela23(self):

        self.tela8.destroy()
        self.criar_tela23()
        self.tela_atual = 23

    #FUNÇÃO IR PARA TELA 24 (EXEMPLO PRATICO 1 - Lei da gravitação Universal de Newton)
    def ir_para_tela24(self):

        self.tela8.destroy()
        self.criar_tela24()
        self.tela_atual = 24

    #FUNÇÃO IR PARA TELA 25 (EXEMPLO PRATICO 2 - Lei da gravitação Universal de Newton)
    def ir_para_tela25(self):

        self.tela8.destroy()
        self.criar_tela25()
        self.tela_atual = 25

    #FUNÇÃO IR PARA TELA 26 (EXEMPLO PRATICO 3 - Lei da gravitação Universal de Newton)
    def ir_para_tela26(self):

        self.tela8.destroy()
        self.criar_tela26()
        self.tela_atual = 26

    #FUNÇÃO IR PARA TELA 27 (CONTEXUALIZAÇÃO - Energia cinética)
    def ir_para_tela27(self):

        self.tela10.destroy()
        self.criar_tela27()
        self.tela_atual = 27

    #FUNÇÃO IR PARA TELA 28 (EXEMPLO PRATICO 1 - Energia cinética)
    def ir_para_tela28(self):

        self.tela10.destroy()
        self.criar_tela28()
        self.tela_atual = 28

    #FUNÇÃO IR PARA TELA 29 (EXEMPLO PRATICO 2 - Energia cinética)
    def ir_para_tela29(self):

        self.tela10.destroy()
        self.criar_tela29()
        self.tela_atual = 29

    #FUNÇÃO IR PARA TELA 30 (EXEMPLO PRATICO 3 - Energia cinética)
    def ir_para_tela30(self):

        self.tela10.destroy()
        self.criar_tela30()
        self.tela_atual = 30

    #FUNÇÃO IR PARA TELA 31 ()
    def ir_para_tela31(self):

        self.tela2.destroy()
        self.criar_tela31()
        self.tela_atual = 31

    #FUNÇÃO IR PARA TELA 32 ()
    def ir_para_tela32(self):

        self.tela2.destroy()
        self.criar_tela32()
        self.tela_atual = 32

    #FUNÇÃO IR PARA TELA 33 ()
    def ir_para_tela33(self):

        self.tela2.destroy()
        self.criar_tela33()
        self.tela_atual = 33

    #FUNÇÃO IR PARA TELA 34 ()
    def ir_para_tela34(self):

        self.tela2.destroy()
        self.criar_tela34()
        self.tela_atual = 34

    #FUNÇÃO IR PARA TELA 35 ()
    def ir_para_tela35(self):

        self.tela2.destroy()
        self.criar_tela35()
        self.tela_atual = 35

    #FUNÇÃO IR PARA TELA 36 ()
    def ir_para_tela36(self):

        self.tela2.destroy()
        self.criar_tela36()
        self.tela_atual = 36

    #FUNÇÃO IR PARA TELA 37 ()
    def ir_para_tela37(self):

        self.tela2.destroy()
        self.criar_tela37()
        self.tela_atual = 37

    #FUNÇÃO IR PARA TELA 38 ()
    def ir_para_tela38(self):

        self.tela2.destroy()
        self.criar_tela38()
        self.tela_atual = 38

    #FUNÇÃO IR PARA TELA 39 ()
    def ir_para_tela39(self):

        self.tela2.destroy()
        self.criar_tela39()
        self.tela_atual = 39

    #FUNÇÃO IR PARA TELA 40 ()
    def ir_para_tela40(self):

        self.tela2.destroy()
        self.criar_tela40()
        self.tela_atual = 40

    #FUNÇÃO IR PARA TELA 41 ()
    def ir_para_tela41(self):

        self.tela2.destroy()
        self.criar_tela41()
        self.tela_atual = 41

    #FUNÇÃO IR PARA TELA 42 ()
    def ir_para_tela42(self):

        self.tela2.destroy()
        self.criar_tela42()
        self.tela_atual = 42

    #FUNÇÃO IR PARA TELA 43 ()
    def ir_para_tela43(self):

        self.tela2.destroy()
        self.criar_tela43()
        self.tela_atual = 43

    #FUNÇÃO IR PARA TELA 44 ()
    def ir_para_tela44(self):

        self.tela2.destroy()
        self.criar_tela44()
        self.tela_atual = 44

    #FUNÇÃO IR PARA TELA 45 ()
    def ir_para_tela45(self):

        self.tela2.destroy()
        self.criar_tela45()
        self.tela_atual = 45

    #FUNÇÃO IR PARA TELA 46 ()
    def ir_para_tela46(self):

        self.tela2.destroy()
        self.criar_tela46()
        self.tela_atual = 46

    #FUNÇÃO IR PARA TELA 47 ()
    def ir_para_tela47(self):

        self.tela2.destroy()
        self.criar_tela47()
        self.tela_atual = 47

    #FUNÇÃO IR PARA TELA 48 ()
    def ir_para_tela48(self):

        self.tela2.destroy()
        self.criar_tela48()
        self.tela_atual = 48

########################################## FUNÇÕES VOLTAR TELA ##############################################################

    #FUNÇÃO VOLTAR TELA ANTERIOR
    def voltar_tela(self):
        
        #SE ESTIVER NA TELA 2, VOLTA PARA 1
        if self.tela_atual == 2:
            self.tela2.destroy()
            self.criar_tela1()
            self.tela_atual = 1

        #SE ESTIVER NA TELA 3, VOLTA PARA 2
        elif self.tela_atual == 3:
            self.tela3.destroy()
            self.criar_tela2()
            self.tela_atual = 2

        #SE ESTIVER NA TELA 4, VOLTA PARA 2
        elif self.tela_atual == 4:
            self.tela4.destroy()
            self.criar_tela2()
            self.tela_atual = 2

        #SE ESTIVER NA TELA 5, VOLTA PARA 2
        elif self.tela_atual == 5:
            self.tela5.destroy()
            self.criar_tela2()
            self.tela_atual = 2

        #SE ESTIVER NA TELA 6, VOLTA PARA 2
        elif self.tela_atual == 6:
            self.tela6.destroy()
            self.criar_tela2()
            self.tela_atual = 2

        #SE ESTIVER NA TELA 7, VOLTA PARA 3
        elif self.tela_atual == 7:
            self.tela7.destroy()
            self.criar_tela3()
            self.tela_atual = 3

        #SE ESTIVER NA TELA 8, VOLTA PARA 3
        elif self.tela_atual == 8:
            self.tela8.destroy()
            self.criar_tela3()
            self.tela_atual = 3

        #SE ESTIVER NA TELA 9, VOLTA PARA 3
        elif self.tela_atual == 9:
            self.tela9.destroy()
            self.criar_tela3()
            self.tela_atual = 3

        #SE ESTIVER NA TELA 10, VOLTA PARA 3
        elif self.tela_atual == 10:
            self.tela10.destroy()
            self.criar_tela3()
            self.tela_atual = 3

        #SE ESTIVER NA TELA 11, VOLTA PARA 3
        elif self.tela_atual == 11:
            self.tela11.destroy()
            self.criar_tela3()
            self.tela_atual = 3

        #SE ESTIVER NA TELA 12, VOLTA PARA 3
        elif self.tela_atual == 12:
            self.tela12.destroy()
            self.criar_tela3()
            self.tela_atual = 3

        #SE ESTIVER NA TELA 13, VOLTA PARA 3
        elif self.tela_atual == 13:
            self.tela13.destroy()
            self.criar_tela3()
            self.tela_atual = 3

        #SE ESTIVER NA TELA 14, VOLTA PARA 3
        elif self.tela_atual == 14:
            self.tela14.destroy()
            self.criar_tela3()
            self.tela_atual = 3

        #SE ESTIVER NA TELA 15, VOLTA PARA 3
        elif self.tela_atual == 15:
            self.tela15.destroy()
            self.criar_tela3()
            self.tela_atual = 3

        #SE ESTIVER NA TELA 16, VOLTA PARA 3
        elif self.tela_atual == 16:
            self.tela16.destroy()
            self.criar_tela3()
            self.tela_atual = 3

        #SE ESTIVER NA TELA 17, VOLTA PARA 3
        elif self.tela_atual == 17:
            self.tela17.destroy()
            self.criar_tela3()
            self.tela_atual = 3

        #SE ESTIVER NA TELA 18, VOLTA PARA 3
        elif self.tela_atual == 18:
            self.tela18.destroy()
            self.criar_tela3()
            self.tela_atual = 3

##################################### VOLTAR TELA CONTEXTUALIZAÇÃO E EXEMPLOS ######################################################################################################################################################################################################################################################

        #SE ESTIVER NA TELA 19, VOLTA PARA 7 (Lei de Movimento de Newton)
        elif self.tela_atual == 19:
            self.tela19.destroy()
            self.criar_tela7()
            self.tela_atual = 7

        #SE ESTIVER NA TELA 20, VOLTA PARA 7 (Lei de Movimento de Newton)
        elif self.tela_atual == 20:
            self.tela20.destroy()
            self.criar_tela7()
            self.tela_atual = 7

        #SE ESTIVER NA TELA 21, VOLTA PARA 7 (Lei de Movimento de Newton)
        elif self.tela_atual == 21:
            self.tela21.destroy()
            self.criar_tela7()
            self.tela_atual = 7

        #SE ESTIVER NA TELA 22, VOLTA PARA 7 (Lei de Movimento de Newton)
        elif self.tela_atual == 22:
            self.tela22.destroy()
            self.criar_tela7()
            self.tela_atual = 7

        #SE ESTIVER NA TELA 23, VOLTA PARA 8 (Lei da gravitação Universal de Newton)
        elif self.tela_atual == 23:
            self.tela23.destroy()
            self.criar_tela8()
            self.tela_atual = 8

        #SE ESTIVER NA TELA 24, VOLTA PARA 8 (Lei da gravitação Universal de Newton)
        elif self.tela_atual == 24:
            self.tela24.destroy()
            self.criar_tela8()
            self.tela_atual = 8

        #SE ESTIVER NA TELA 25, VOLTA PARA 8 (Lei da gravitação Universal de Newton)
        elif self.tela_atual == 25:
            self.tela25.destroy()
            self.criar_tela8()
            self.tela_atual = 8

        #SE ESTIVER NA TELA 26, VOLTA PARA 8 (Lei da gravitação Universal de Newton)
        elif self.tela_atual == 26:
            self.tela26.destroy()
            self.criar_tela8()
            self.tela_atual = 8

        #SE ESTIVER NA TELA 27, VOLTA PARA 10 (Energia cinética)
        elif self.tela_atual == 27:
            self.tela27.destroy()
            self.criar_tela10()
            self.tela_atual = 10

        #SE ESTIVER NA TELA 28, VOLTA PARA 10 (Energia cinética)
        elif self.tela_atual == 28:
            self.tela28.destroy()
            self.criar_tela10()
            self.tela_atual = 10

        #SE ESTIVER NA TELA 29, VOLTA PARA 10 (Energia cinética)
        elif self.tela_atual == 29:
            self.tela29.destroy()
            self.criar_tela10()
            self.tela_atual = 10

        #SE ESTIVER NA TELA 30, VOLTA PARA 10 (Energia cinética)
        elif self.tela_atual == 30:
            self.tela30.destroy()
            self.criar_tela10()
            self.tela_atual = 10

####################################################################################################################################################################################################################################################################################################################################

#INICIALIZAÇÃO DA PRIMEIRA JANELA
if __name__ == "__main__":
    root = tk.Tk()
    app = Software(root)
    root.mainloop()
