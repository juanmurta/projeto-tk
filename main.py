import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename

import numpy as np
from tkcalendar import DateEntry
import pandas as pd
import requests
from datetime import datetime


requisicao = requests.get("https://economia.awesomeapi.com.br/json/all")
dicionario_moedas = requisicao.json()

lista_moedas = list(dicionario_moedas.keys())


def pegar_cotacao():
    moeda = combobox_selecionarmoeda.get()
    data_cotacao = calendario_moeda.get()
    ano = data_cotacao[-4:]
    mes = data_cotacao[3:5]
    dia = data_cotacao[:2]
    link = f'https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/?start_date={ano}{mes}{dia}&end_date={ano}{mes}{dia}'
    requisicao_moeda = requests.get(link)
    cotacao = requisicao_moeda.json()
    valor_moeda = cotacao[0]['bid']
    label_textocotacao['text'] = f'A cotação de {moeda} no dia {data_cotacao} é de R$ {valor_moeda}'


def selecionar_arquivo():
    caminho_arquivo = askopenfilename(title="Selecione o arquivo em excel")
    var_caminhoarquivo.set(caminho_arquivo)
    if caminho_arquivo:
        label_arquivoselecionado['text'] = f"Arquivo Selecionado: {caminho_arquivo}"


def atualizar_cotacoes():
    try:
        df = pd.read_excel(var_caminhoarquivo.get())
        moedas = df.iloc[:, 0]

        for moeda in moedas:
            link = f'https://economia.awesomeapi.com.br/json/daily/{moeda}-BRL/15'
            requisicao_moeda = requests.get(link)
            cotacoes = requisicao_moeda.json()

            for cotacao in cotacoes:
                timestamp = int(cotacao['timestamp'])
                bid = float(cotacao['bid'])
                data = datetime.fromtimestamp(timestamp)
                data = data.strftime('%d/%m/%Y')
                if data not in df:
                    df[data] = np.nan
                df.loc[df.iloc[:, 0] == moeda, data] = bid

            df.to_excel("Teste.xlsx", index=False)
            label_atualizarcotacoes['text'] = "Atualização concluída com sucesso!"
    except:
        label_atualizarcotacoes['text'] = "Verifique o arquivo e tente novamente."


janela = tk.Tk()

janela.title("Cotação de Moedas")

label_cotacao = tk.Label(text="Cotação de 1 moeda especifica", borderwidth=2, relief="solid")
label_cotacao.grid(row=0, column=0, padx=10, pady=10, sticky="nswe", columnspan=3)

label_selecionarmoeda = tk.Label(text="Selecionar moeda", anchor='e')
label_selecionarmoeda.grid(row=1, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

combobox_selecionarmoeda = ttk.Combobox(values=lista_moedas)
combobox_selecionarmoeda.grid(row=1, column=2, padx=10, pady=10, sticky="nswe")

label_selecionardia = tk.Label(text="Selecione o dia que deseje pegar a cotação", anchor='e')
label_selecionardia.grid(row=2, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

calendario_moeda = DateEntry(year=2025, locale='pt_BR')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky="nswe")

label_textocotacao = tk.Label(text="")
label_textocotacao.grid(row=3, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

botao_pegarcotacao = tk.Button(text="Pegar Cotação", command=pegar_cotacao)
botao_pegarcotacao.grid(row=3, column=2, padx=10, pady=10, sticky="nswe")

label_cotacaovarias = tk.Label(text="Cotação de 15 dias multiplas moedas", borderwidth=2, relief="solid")
label_cotacaovarias.grid(row=4, column=0, padx=10, pady=10, sticky="nswe", columnspan=3)

label_selecionararquivo = tk.Label(text="Selecione o arquivo em excel", anchor='e')
label_selecionararquivo.grid(row=5, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

var_caminhoarquivo = tk.StringVar()

botao_selecionararquivo = tk.Button(text="Clique para Selecionar", command=selecionar_arquivo)
botao_selecionararquivo.grid(row=5, column=2, padx=10, pady=10, sticky="nswe")

label_arquivoselecionado = tk.Label(text="Nenhum arquivo Selecionado", anchor='e')
label_arquivoselecionado.grid(row=6, column=0, padx=10, pady=10, sticky="nswe", columnspan=3)

botao_atualizarcotacoes = tk.Button(text="Atualizar Cotação", command=atualizar_cotacoes)
botao_atualizarcotacoes.grid(row=9, column=0, padx=10, pady=10, sticky="nswe")

label_atualizarcotacoes = tk.Label(text="")
label_atualizarcotacoes.grid(row=9, column=1, padx=10, pady=10, sticky="nswe", columnspan=2)

botao_fechar = tk.Button(text="Fechar", command=janela.quit)
botao_fechar.grid(row=10, column=2, padx=10, pady=10, sticky="nswe")

janela.mainloop()
