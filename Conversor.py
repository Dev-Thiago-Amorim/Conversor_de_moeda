import requests
from tkinter import *
import awesometkinter as atk


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']

    texto = f'''
    Cotação do Dólar: R$ {float(cotacao_dolar):.2f}
    Cotação do Euro: R$ {float(cotacao_euro):.2f}'''

    texto_tela["text"] = texto

    if valor_entrada.get().isnumeric():
        resposta = valor_entrada.get()
        res = f'''
        Conversão para Dólar: $ {(float(resposta) / float(cotacao_dolar)):.2f}
        Conversão para Euro: € {(float(resposta) / float(cotacao_euro)):.2f}'''
        texto_conv["text"] = res


largura_janela = 400
altura_janela = 400

janela = Tk()
janela.title("Cotação e Conversão de Moedas")
janela.geometry(f"{largura_janela}x{altura_janela}")
janela.configure(bg='black')

valor_entrada = Entry(janela)
valor_entrada.place(x=110, y=70)
valor_entrada.configure(font=('Arial', 8), width=30)


texto_orientacao = Label(janela, text="Digite o valor a ser convertido (R$)", font=('Arial', 12, "bold"), fg="yellow")
texto_orientacao.place(x=80, y=20)
texto_orientacao.configure(bg='black')

botao = atk.Button3d(janela, text="Buscar", command=pegar_cotacoes, width=10)
botao.place(x=160, y=100)

texto_tela = Label(janela, text="", font=('Arial', 15, "bold"), fg="yellow")
texto_tela.place(x=55, y=150)
texto_tela.configure(bg='black')

texto_conv = Label(janela, text="", font=('Arial', 15, "bold"), fg="yellow")
texto_conv.place(x=15, y=250)
texto_conv.configure(bg='black')

janela.mainloop()
