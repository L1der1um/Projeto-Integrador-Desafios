#IMPORTANDO A BIBLIOTECA TKINTER
import tkinter as tk
from tkinter import *
from tkinter import ttk
#IMPRTANTO BIBLIOTECA WEBBROWSER PARA O LINK DO GITHUB
import webbrowser

#CRIANDO A CLASSE SOFTWARE
class Software:

    ############################################################################################################

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

    ############################################################################################################

    #CRIA A TELA 1 (PRINCIPAL)
    def criar_tela1(self):
        
        #PRIMEIRA TELA (INICIO)
        self.tela1 = tk.Frame(self.root)
        self.tela1.pack()

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
        botao = tk.Button(self.tela1, text="Encerrar", command=self.encerrar_programa, bg='red', fg='white')
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
        button1 = tk.Button(frame1, text="Lei de movimento de Newton\n(Segunda lei)\nF = m . a",command=self.ir_para_tela7)
        button2 = tk.Button(frame1, text="Lei da gravitação\n Universal de Newton\nP = m .g",command=self.ir_para_tela8)
        button3 = tk.Button(frame1, text="Lei de Coulomb\n (Lei de Eletrostatica)\nF = k * (|q1 * q2|) / d²",command=self.ir_para_tela9)
        button4 = tk.Button(frame1, text="Energia cinética\nEc = m . v² / 2",command=self.ir_para_tela10)
        button1.pack(side=tk.LEFT,padx=10, pady=10)
        button2.pack(side=tk.LEFT,padx=10, pady=10)
        button3.pack(side=tk.LEFT,padx=10, pady=10)
        button4.pack(side=tk.LEFT,padx=10, pady=10)

        #CRIANDO O FRAME DA SEGUNDA LINHA DE BOTOES
        frame2 = tk.Frame(self.tela3)
        frame2.pack()
        #CRIANDO O FRAME DA PRMEIRA LINHA DE BOTOES
        button5 = tk.Button(frame2, text="Energia Potencial\n Gravitacional\nEPG = m ⋅g ⋅h",command=self.ir_para_tela11)
        button6 = tk.Button(frame2, text="Lei da conservação\n de Energia Mecânica\nE = K + U",command=self.ir_para_tela12)
        button7 = tk.Button(frame2, text="Lei de Hooke\n (Lei da Elasticidade)\nF = -k . x",command=self.ir_para_tela13)
        button8 = tk.Button(frame2, text="Lei de Snell\n (Lei da Refração)\nn1.sen(i) = n2.sen(r)",command=self.ir_para_tela14)
        button5.pack(side=tk.LEFT,padx=10, pady=40)
        button6.pack(side=tk.LEFT,padx=10, pady=40)
        button7.pack(side=tk.LEFT,padx=10, pady=40)
        button8.pack(side=tk.LEFT,padx=10, pady=40)


        #CRIANDO O FRAME DA TERCEIRA LINHA DE BOTOES
        frame3 = tk.Frame(self.tela3)
        frame3.pack()
        #CRIANDO O FRAME DA PRMEIRA LINHA DE BOTOES
        button9 = tk.Button(frame3, text="Lei de Ohm\n (Primeira lei)\nV = A x Ω",command=self.ir_para_tela15)
        button10 = tk.Button(frame3, text="Distância em Movimento\n Uniforme\nS(t) = S₀ + v . t",command=self.ir_para_tela16)
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
        label4.pack(pady=10)

        #TEXTO TELA OBJETIVO PRINCIPAL
        texto = """
        O objetivo principal deste software é de auxiliar
        o novos alunos recem ingresados na universidade os
        quais possuem a matéria de Fisica 1 eu sua grade
        afim de auxiliá-los em sua aprendizagem ao longo
        de seu curso atual na UNISO mediante a explicação
        do contexto e utilização das principais formulas
        desta matéria incluindo calculadora para cada uma
        das formulas mais importantes desta matéria.
        """

        #RÓTULO DO TEXTO
        label4_1 = tk.Label(self.tela4, text=texto, justify="center", padx=10, pady=10)
        label4_1.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela4, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom')

    #CRIA A TELA 5 (Agradecimentos e Referencias)
    def criar_tela5(self):

        self.tela5 = tk.Frame(self.root)
        self.tela5.pack()

        #TEXTO INFORMATIVO DE TELA
        label5 = tk.Label(self.tela5, text="AGRADECIMENTOS E REFERÊNCIAS" ,font=('Arial', 14, 'bold'))
        label5.pack(pady=10, side='top', anchor='n')

        #TEXTO TELA AGRADECIMENTOS
        texto = """
        (TEXTO)
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

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela6, text="GITHUB DO PROJETO" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=10)

        #BOTÃO PARA ABRIR O GITHUB
        button_github = tk.Button(self.tela6, text="Abrir GitHub", command=self.abrir_github)
        button_github.pack(pady=60)

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

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela6, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=90)

    #CRIA A TELA 7 (Lei de Movimento de Newton (Segunda Lei))
    def criar_tela7(self):

        self.tela7 = tk.Frame(self.root)
        self.tela7.pack()

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela7, text="Lei de Movimento de Newton (Segunda Lei)" ,font=('Arial', 14, 'bold'))
        label6.pack(pady=40)

        #TEXTO INFORMATIVO DE TELA
        label6 = tk.Label(self.tela7, text="Insira zero (0) dentro do dado que você deseja calcular")
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

        #TEXTO FORÇA DO CAMPO DE ENTRADA
        label_forca = tk.Label(self.tela7, text="Força (N):")
        label_forca.pack()

        entry_forca = ttk.Entry(self.tela7)
        entry_forca.placeholder = "Insira a força"
        entry_forca.insert(0, entry_forca.placeholder)
        entry_forca.bind("<FocusIn>", remover_placeholder)
        entry_forca.bind("<FocusOut>", restaurar_placeholder)
        entry_forca.pack()

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
                forca = float(entry_forca.get())
                massa = float(entry_massa.get())
                aceleracao = float(entry_aceleracao.get())

                #CALCULA A FORÇA
                if forca == 0:

                    forca = massa * aceleracao
                    resultado.set(f"Força: {forca} N")

                #CALCULA A MASSA
                elif massa == 0:

                    massa = forca / aceleracao
                    resultado.set(f"Massa: {massa} kg")

                #CALCULA A ACELERAÇÃO
                elif aceleracao == 0:

                    aceleracao = forca / massa
                    resultado.set(f"Aceleração: {aceleracao} m/s²")

                else:
                    #SOLICITA PARA O USUÁRIO INSERIR DOIS VALORES E UM ZERO O DADO QUE DESEJA CALCULAR
                    resultado.set("Preencha dois valores e deixe um campo com um zero (0) para calcular.")

            except ValueError:
                #INFORMA ERRO DE VALOR NÃO RECONHECIDO
                resultado.set("Insira valores numéricos válidos.")

        #FUNÇÃO LIMPAR OS CAMPOS
        def limpar_campos():
            entry_forca.delete(0, tk.END)
            entry_massa.delete(0, tk.END)
            entry_aceleracao.delete(0, tk.END)
            resultado.set("")  # Limpa o resultado

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
        label_resultado.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela7, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom', pady=20)


    #CRIA A TELA 8 (Lei da gravitação Universal de Newton)
    def criar_tela8(self):

        self.tela8 = tk.Frame(self.root)
        self.tela8.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela8, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=90)

    #CRIA A TELA 9 (Lei de Coulomb)
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

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela10, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=90)

    #CRIA A TELA 11 (Energia Potencial Gravitacional)
    def criar_tela11(self):

        self.tela11 = tk.Frame(self.root)
        self.tela11.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela11, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=90)

    #CRIA A TELA 12 (Lei da conservação de Energia Mecânica)
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

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela13, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=90)

    #CRIA A TELA 14 (Lei de Snell)
    def criar_tela14(self):

        self.tela14 = tk.Frame(self.root)
        self.tela14.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela14, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=90)

    #CRIA A TELA 15 (Lei de Ohm)
    def criar_tela15(self):

        self.tela15 = tk.Frame(self.root)
        self.tela15.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela15, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=90)

    #CRIA A TELA 16 (Distância em Movimento Uniforme)
    def criar_tela16(self):

        self.tela16 = tk.Frame(self.root)
        self.tela16.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela16, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=90)

    #CRIA A TELA 17 (Velocidade média)
    def criar_tela17(self):

        self.tela17 = tk.Frame(self.root)
        self.tela17.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela17, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=90)

    #CRIA A TELA 18 (Densidade)
    def criar_tela18(self):

        self.tela18 = tk.Frame(self.root)
        self.tela18.pack()

        #BOTÃO VOLTAR TELA
        btn_tela_anterior = tk.Button(self.tela18, text="Voltar", command=self.voltar_tela)
        btn_tela_anterior.pack(side='bottom',pady=90)

    #CRIA A TELA 19 ()
    def criar_tela19(self):

        self.tela19 = tk.Frame(self.root)
        self.tela19.pack()

    #CRIA A TELA 20 ()
    def criar_tela20(self):

        self.tela20 = tk.Frame(self.root)
        self.tela20.pack()

    #CRIA A TELA 21 ()
    def criar_tela21(self):

        self.tela21 = tk.Frame(self.root)
        self.tela21.pack()

    ############################################################################################################

    #FUNÇÃO ENCERRAR PROGRAMA
    def encerrar_programa(self):
        
        root.destroy()


    #FUNÇÃO ABRIR LINK DO GITHUB
    def abrir_github(self):

        webbrowser.open('https://github.com/L1der1um/Projeto-Integrador-Desafios')

    ############################################################################################################
    
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

    #FUNÇÃO IR PARA TELA 19 ()
    def ir_para_tela19(self):

        self.tela2.destroy()
        self.criar_tela19()
        self.tela_atual = 19

    #FUNÇÃO IR PARA TELA 20 ()
    def ir_para_tela20(self):

        self.tela2.destroy()
        self.criar_tela20()
        self.tela_atual = 20

    ############################################################################################################

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
####################################################################################################################################################################################################################################################################################################################################

if __name__ == "__main__":
    root = tk.Tk()
    app = Software(root)
    root.mainloop()
