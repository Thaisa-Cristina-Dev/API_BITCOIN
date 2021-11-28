from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

from pip._vendor import requests
import json


# cores ---------------
cor0 = "#444466"  # Preta 
cor1 = "#feffff"  # branca 
cor2 = "#6f9fbd"  # azul 
fundo = "#484f60" #background

janela=Tk()
janela.geometry("320x350")
janela.title('')
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)


frame_cima = Frame(janela, width=320, height=50,  padx=0, pady=0, bg=cor1, relief='flat')
frame_cima.grid(row=1, column=0)

frame_baixo = Frame(janela, width=320, height=300,  padx=0, pady=0, bg=fundo, relief='flat')
frame_baixo.grid(row=2, column=0, sticky=NW)

#API

def info():
    api_link = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,AOA,BRL'

    response = requests.get(api_link) 

    #convertendo dados
    dados = response.json()
    print(dados)


    # valor em USD
    valor_usd = float(dados['USD'])
    valor_formato_usd = "${:,.3f}".format(valor_usd)
    l_p_usd['text'] = valor_formato_usd
    
    # valor em EURO
    valor_euro = float(dados['EUR'])
    valor_formato_usd = "{:,.3f}".format(valor_euro)
    l_p_euro['text'] = 'Em Euro é : € ' +valor_formato_usd
    
    # valor em BRL
    valor_reais = float(dados['BRL'])
    valor_formato_reais = "{:,.3f}".format(valor_reais)
    l_p_reais['text'] = 'Em Reais é : R$ ' +valor_formato_reais 

    # valor em AOA
    valor_Kz = float(dados['AOA'])
    valor_formato_Kz = "{:,.3f}".format(valor_Kz)
    l_p_Kz['text'] = 'Em Kwanzas é : AOA ' + valor_formato_Kz

    frame_baixo.after(1000, info)


imagem = Image.open('imagem/bitcoin.png')
imagem = imagem.resize((30,30), Image.ANTIALIAS)
imagem = ImageTk.PhotoImage(imagem)

l_icon = Label(frame_cima, image=imagem, compound=LEFT, bg=cor1, relief=FLAT)
l_icon.place(x=10, y=10)

l_nome = Label(frame_cima, text='Bitcoin Price Tracker', bg=cor1, relief=FLAT, anchor=CENTER, font=('Arial 19 bold'))
l_nome.place(x=50, y=5)


l_p_usd = Label(frame_baixo, text= '', bg=fundo, fg=cor2, relief=FLAT, anchor=CENTER, font=('Arial 30 bold'))
l_p_usd.place(x=50, y=50)

l_p_euro = Label(frame_baixo, text='', bg=fundo, fg=cor2, relief=FLAT, anchor=CENTER, font=('Arial 13 bold'))
l_p_euro.place(x=10, y=130)

l_p_reais = Label(frame_baixo, text='', bg=fundo, fg=cor2, relief=FLAT, anchor=CENTER, font=('Arial 13 bold'))
l_p_reais.place(x=10, y=160)

l_p_Kz = Label(frame_baixo, text='', bg=fundo, fg=cor2, relief=FLAT, anchor=CENTER, font=('Arial 13 bold'))
l_p_Kz.place(x=10, y=190)

info()

janela.mainloop()