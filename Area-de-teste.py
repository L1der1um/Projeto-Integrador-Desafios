#IMPORTANDO A BIBLIOTECA TKINTER
import tkinter as tk
from tkinter import *
from tkinter import ttk
#IMPORTANTO BIBLIOTECA WEBBROWSER PARA O LINK DO GITHUB
import webbrowser
#IMPORTANTO BIBLIOTECA MATH PARA CALCULAR RESULTADOS COM SEN E COS
import math
#IMPORTANDO BIBLITOECA QRCODE PARA GERAR O QRCODE DO GITHUB
import qrcode
##IMPORTANDO BIBLIOTECA PIL PARA AUXILAR NA ABERTURA DO QRCODE NA TELA
from PIL import ImageTk

from ttkthemes import ThemedStyle

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
        btn_proxima_tela1 = tk.Button(self.tela1, text="INICIAR", command=self.ir_para_tela2(root, ThemedStyle))
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
        button5 = tk.Button(frame2, text="Energia Potencial\n Gravitacional\nEPG = m * g * h",command=self.ir_para_tela11)
        button6 = tk.Button(frame2, text="Lei da conservação\n de Energia Mecânica\nE = K + U",command=self.ir_para_tela12)
        button7 = tk.Button(frame2, text="Lei de Hooke\n (Lei da Elasticidade)\nF = -k * x",command=self.ir_para_tela13)
        button8 = tk.Button(frame2, text="Lei de Snell\n (Lei da Refração)\nn1.sen(i) = n2.sen(r)",command=self.ir_para_tela14)
        button5.pack(side=tk.LEFT,padx=10, pady=40)
        button6.pack(side=tk.LEFT,padx=10, pady=40)
        button7.pack(side=tk.LEFT,padx=10, pady=40)
        button8.pack(side=tk.LEFT,padx=10, pady=40)


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

        #SE ESTIVER NA TELA 21, VOLTA PARA 7 (Lei de Movimento de Newton)
        elif self.tela_atual == 22:
            self.tela22.destroy()
            self.criar_tela7()
            self.tela_atual = 7

####################################################################################################################################################################################################################################################################################################################################

if __name__ == "__main__":
    root = tk.Tk()
    app = Software(root)
    root.mainloop()
