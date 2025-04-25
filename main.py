import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry


lista_moedas = ['USD', 'EUR', 'JPY', 'GBP']


def pegar_cotacao():
    pass


janela = tk.Tk()

janela.title("Cotação de Moedas")

label_cotacao = tk.Label(text="Cotação de 1 moeda especifica", borderwidth=2, relief="solid")
label_cotacao.grid(row=0, column=0, padx=10, pady=10, sticky="nswe", columnspan=3)

label_selecionarmoeda = tk.Label(text="Selecionar moeda")
label_selecionarmoeda.grid(row=1, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

combobox_selecionarmoeda = ttk.Combobox(values=lista_moedas)
combobox_selecionarmoeda.grid(row=1, column=2, padx=10, pady=10, sticky="nswe")

label_cotacaovarias = tk.Label(text="Selecione o dia que deseje pegar a cotação")
label_cotacaovarias.grid(row=2, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

calendario_moeda = DateEntry(year=2025, locale='pt_BR')
calendario_moeda.grid(row=2, column=2, padx=10, pady=10, sticky="nswe")

label_textocotacao = tk.Label(text="")
label_textocotacao.grid(row=3, column=0, padx=10, pady=10, sticky="nswe", columnspan=2)

botao_pegarcotacao = tk.Button(text="Pegar Cotação", command=pegar_cotacao)
botao_pegarcotacao.grid(row=3, column=2, padx=10, pady=10, sticky="nswe")

label_cotacaovarias = tk.Label(text="Cotação de multiplas moedas", borderwidth=2, relief="solid")
label_cotacaovarias.grid(row=4, column=0, padx=10, pady=10, sticky="nswe", columnspan=3)

janela.mainloop()