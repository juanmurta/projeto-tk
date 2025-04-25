# Importação das bibliotecas necessárias
# tkinter: biblioteca para criação de interfaces gráficas
# ttk: módulo do tkinter que fornece widgets com estilo mais moderno
# askopenfilename: função para abrir caixa de diálogo para selecionar arquivos
# pandas: biblioteca para manipulação e análise de dados
import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import pandas as pd

# Configuração da janela principal
janela = tk.Tk()  # Cria a janela principal da aplicação

# Configurações básicas da janela
janela.title("Automação")  # Define o título da janela
janela.rowconfigure(0, minsize=30, weight=1)  # Configura a linha 0 com tamanho mínimo e peso para redimensionamento
janela.columnconfigure([0, 1], minsize=30, weight=1)  # Configura as colunas 0 e 1 para redimensionamento

# Elementos da interface - Cabeçalho
mensagem = tk.Label(text="Sistema de automação", fg="white", bg="#7E40C8", width=35, height=1, font=("Arial", 10))
mensagem.grid(row=0, column=0, columnspan=3, sticky='NSEW')  # Posiciona o cabeçalho ocupando 3 colunas

# Elementos da interface - Seleção de moeda
mensagem2 = tk.Label(text="Digite a moeda", foreground="white", background="blue", width=20, height=1,
                     font=("Arial", 10))
mensagem2.grid(row=1, column=0)  # Posiciona o rótulo na linha 1, coluna 0

# Código comentado - versão anterior usando campo de texto em vez de combobox
# moeda = tk.Entry()
# moeda.grid(row=1, column=1)

# Dicionário com as cotações das moedas
dicionario_cotacao = {
    "Dolar": 5.99,
    "Euro": 7.99,
    "Bitcon": 249000,
}
moedas = list(dicionario_cotacao.keys())  # Lista com os nomes das moedas para o combobox

# Cria um combobox (lista suspensa) com as opções de moedas
moeda = ttk.Combobox(janela, values=moedas)
moeda.grid(row=1, column=1)  # Posiciona o combobox na linha 1, coluna 1

# Função para buscar a cotação de uma única moeda selecionada no combobox
def buscar_cotacao():
    moeda_preenchida = moeda.get()  # Obtém o texto selecionado no combobox
    cotacao_moeda = dicionario_cotacao.get(moeda_preenchida)  # Busca a cotação no dicionário
    mensagem_cotacao = tk.Label(text="Cotacao não encontrada")  # Cria um label com mensagem padrão
    mensagem_cotacao.grid(row=3, column=0, columnspan=2)  # Posiciona o label na interface
    if cotacao_moeda:  # Se encontrou a cotação
        mensagem_cotacao["text"] = f"A cotação do {moeda_preenchida} é {cotacao_moeda}"  # Atualiza o texto do label

# Botão para acionar a busca de cotação
botao = tk.Button(text="Buscar Cotação", command=buscar_cotacao, width=15)  # Cria botão vinculado à função buscar_cotacao
botao.grid(row=2, column=0, columnspan=3)  # Posiciona o botão ocupando 3 colunas

# Seção para busca de múltiplas cotações
mensagem3 = tk.Label(text="Para pegar duas cotações seleciona uma moeda em cada linha")  # Instrução para o usuário
mensagem3.grid(row=4, column=0, columnspan=2)  # Posiciona a instrução ocupando 2 colunas

# Caixa de texto para inserir múltiplas moedas (uma por linha)
caixa_texto = tk.Text(height=5, width=20)  # Cria uma área de texto com 5 linhas de altura
caixa_texto.grid(row=5, column=0, sticky='NSEW')  # Posiciona a caixa de texto com expansão em todas as direções

# Função para buscar cotações de múltiplas moedas
def buscar_cotacoes():
    texto = caixa_texto.get("1.0", tk.END)  # Obtém todo o texto da caixa de texto (da linha 1, caractere 0 até o final)
    lista_moedas = texto.split("\n")  # Divide o texto em linhas, criando uma lista de moedas
    mensagem_cotacoes = []  # Lista para armazenar as mensagens de cotação

    # Itera por cada moeda na lista
    for item in lista_moedas:
        cotacao = dicionario_cotacao.get(item)  # Busca a cotação no dicionário
        if cotacao:  # Se encontrou a cotação
            mensagem_cotacoes.append(f'{item}: {cotacao}')  # Adiciona a mensagem formatada à lista

    # Cria um label com todas as cotações encontradas, separadas por quebra de linha
    mensagem4 = tk.Label(text="\n".join(mensagem_cotacoes))
    mensagem4.grid(row=6, column=1)  # Posiciona o label na interface

    print(texto)  # Exibe o texto completo no console (para depuração)

# Botão para acionar a busca de múltiplas cotações
botao_multi = tk.Button(text="Buscar Cotações", command=buscar_cotacoes, width=15)  # Cria botão vinculado à função buscar_cotacoes
botao_multi.grid(row=5, column=1)  # Posiciona o botão na interface

# Seção de checkbox para aceitar termos
var_promocoes = tk.IntVar()  # Variável para armazenar o estado do checkbox (0 ou 1)
checkbox_promocoes = tk.Checkbutton(text="Concorda com os termos", variable=var_promocoes)  # Cria o checkbox vinculado à variável
checkbox_promocoes.grid(row=6, column=0)  # Posiciona o checkbox na interface

# Função para verificar se o usuário concordou com os termos
def enviar():
    if var_promocoes.get():  # Se o checkbox estiver marcado (valor 1)
        print("Concorda com termos")  # Exibe mensagem no console
    else:  # Se o checkbox não estiver marcado (valor 0)
        print("Não concorda com termos")  # Exibe mensagem no console

# Botão para enviar o formulário
botao_enviar = tk.Button(text="Enviar", command=enviar, width=15)  # Cria botão vinculado à função enviar
botao_enviar.grid(row=6, column=1)  # Posiciona o botão na interface

# Função para exibir a moeda selecionada nos radio buttons
def enviar_radio():
    print(moeda.get())  # Exibe no console o valor da variável moeda (qual radio button está selecionado)

# Seção de radio buttons para seleção de moeda
moeda = tk.StringVar(value="Nada")  # Variável para armazenar o valor do radio button selecionado, com valor inicial "Nada"

# Criação dos radio buttons, todos vinculados à mesma variável (moeda)
botao_dolar = tk.Radiobutton(text="Dolar", value='Dolar', variable=moeda, command=enviar_radio)  # Radio button para Dolar
botao_euro = tk.Radiobutton(text="Euro", value='Euro', variable=moeda, command=enviar_radio)  # Radio button para Euro
botao_bitcoin = tk.Radiobutton(text="Bitcoin", value='Bitcoin', variable=moeda, command=enviar_radio)  # Radio button para Bitcoin

# Posicionamento dos radio buttons na interface
botao_dolar.grid(row=7, column=0)
botao_euro.grid(row=7, column=1)
botao_bitcoin.grid(row=7, column=2)

# Código comentado - botão adicional para enviar a seleção do radio button
# botao_enviar = tk.Button(text="Enviar", command=enviar_radio, width=15)
# botao_enviar.grid(row=8, column=0, columnspan=3)

# Seção para abrir arquivo e ler com pandas
# Abre uma caixa de diálogo para o usuário selecionar um arquivo
caminho_arquivo = askopenfilename(title="Selecione o arquivo")

# Lê o arquivo Excel selecionado usando pandas
df = pd.read_excel(caminho_arquivo)

# Exibe o conteúdo do DataFrame no console
print(df)

# Inicia o loop principal da aplicação
# Esta linha deve ser sempre a última do código, pois mantém a janela aberta e processando eventos
janela.mainloop()
