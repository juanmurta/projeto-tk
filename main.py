import tkinter as tk


janela = tk.Tk()

janela.title("Automação")
janela.rowconfigure(0, minsize=30, weight=1)
janela.columnconfigure([0, 1], minsize=30, weight=1)

mensagem = tk.Label(text="Sistema de automação", fg="white", bg="#7E40C8", width=35, height=1, font=("Arial", 10))
mensagem.grid(row=0, column=0, columnspan=2, sticky='NSEW')

mensagem2 = tk.Label(text="Digite seu nome", foreground="white", background="blue", width=20, height=1,
                     font=("Arial", 10))
mensagem2.grid(row=1, column=0)

nome = tk.Entry()
nome.grid(row=1, column=1)


def buscar_nome():
    print(nome.get())


botao = tk.Button(text="Enviar", command=buscar_nome, width=10)
botao.grid(row=2, column=0, columnspan=2)

janela.mainloop()
