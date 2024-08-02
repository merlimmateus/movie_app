import tkinter as tk
from tkinter import messagebox

from models.filme import Filme
from models.lista_filmes import ListaFilmes


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Filmes")
        self.root.geometry("400x400")
        self.root.configure(bg="#f0f0f0")  # Background color

        # Título da Aplicação
        self.title_label = tk.Label(
            root, text="Minha Lista de Filmes", font=("Arial", 16, "bold"), bg="#f0f0f0"
        )
        self.title_label.pack(pady=10)

        self.entry_frame = tk.Frame(root, bg="#f0f0f0")
        self.entry_frame.pack(pady=10)

        # Campo de Título do Filme
        tk.Label(self.entry_frame, text="Nome do Filme:", bg="#f0f0f0").grid(
            row=0, column=0, padx=5, pady=5, sticky=tk.W
        )
        self.entry_titulo = tk.Entry(self.entry_frame)
        self.entry_titulo.grid(row=0, column=1, padx=5, pady=5)

        # Campo de Ano
        tk.Label(self.entry_frame, text="Ano:", bg="#f0f0f0").grid(
            row=1, column=0, padx=5, pady=5, sticky=tk.W
        )
        self.entry_ano = tk.Entry(self.entry_frame)
        self.entry_ano.grid(row=1, column=1, padx=5, pady=5)

        # Campo de Nota
        tk.Label(self.entry_frame, text="Nota:", bg="#f0f0f0").grid(
            row=2, column=0, padx=5, pady=5, sticky=tk.W
        )
        self.entry_nota = tk.Entry(self.entry_frame)
        self.entry_nota.grid(row=2, column=1, padx=5, pady=5)

        # Frame para Botões
        self.button_frame = tk.Frame(root, bg="#f0f0f0")
        self.button_frame.pack(pady=10)

        # Botão Inserir
        self.btn_inserir = tk.Button(
            self.button_frame,
            text="Inserir Filme",
            command=self.inserir_filme,
            bg="#4CAF50",
            fg="white",
            relief=tk.FLAT,
            font=("Arial", 10, "bold"),
        )
        self.btn_inserir.grid(row=0, column=0, padx=5)

        # Botão Atualizar
        self.btn_atualizar = tk.Button(
            self.button_frame,
            text="Atualizar Filme",
            command=self.atualizar_filme,
            bg="#FFC107",
            fg="black",
            relief=tk.FLAT,
            font=("Arial", 10, "bold"),
        )
        self.btn_atualizar.grid(row=0, column=1, padx=5)

        # Botão Remover
        self.btn_remover = tk.Button(
            self.button_frame,
            text="Remover Filme",
            command=self.remover_filme,
            bg="#F44336",
            fg="white",
            relief=tk.FLAT,
            font=("Arial", 10, "bold"),
        )
        self.btn_remover.grid(row=0, column=2, padx=5)

        # Listagem de Filmes
        self.lista_frame = tk.Frame(root)
        self.lista_frame.pack(pady=10)

        self.lb = tk.Listbox(
            self.lista_frame,
            width=50,
            height=10,
            font=("Arial", 10),
            selectbackground="#6C63FF",
            selectforeground="white",
            bg="#f0f0f0",
            relief=tk.FLAT,
        )
        self.lb.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Barra de Rolagem
        self.scrollbar = tk.Scrollbar(self.lista_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.lb.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.lb.yview)

        self.lista_filmes = ListaFilmes()

    def inserir_filme(self):
        titulo = self.entry_titulo.get()
        ano = self.entry_ano.get()
        nota = self.entry_nota.get()
        if titulo and ano and nota:
            try:
                ano = int(ano)
                nota = float(nota)
                filme = Filme(titulo, ano, nota)
                self.lista_filmes.insere_filme(filme)
                self.atualizar_listbox()
                self.limpar_campos()
            except ValueError:
                messagebox.showwarning(
                    "Input Error", "Ano deve ser um número inteiro e nota deve ser um número decimal."
                )
        else:
            messagebox.showwarning("Input Error", "Todos os campos devem ser preenchidos")

    def atualizar_filme(self):
        selecao = self.lb.curselection()
        if selecao:
            index = selecao[0]
            titulo = self.entry_titulo.get()
            ano = self.entry_ano.get()
            nota = self.entry_nota.get()
            if titulo and ano and nota:
                try:
                    ano = int(ano)
                    nota = float(nota)
                    novo_filme = Filme(titulo, ano, nota)
                    self.lista_filmes.atualiza_filme(index, novo_filme)
                    self.atualizar_listbox()
                    self.limpar_campos()
                except ValueError:
                    messagebox.showwarning(
                        "Input Error", "Ano deve ser um número inteiro e nota deve ser um número decimal."
                    )
            else:
                messagebox.showwarning("Input Error", "Todos os campos devem ser preenchidos")
        else:
            messagebox.showwarning("Selection Error", "Nenhum filme selecionado")

    def remover_filme(self):
        selecao = self.lb.curselection()
        if selecao:
            index = selecao[0]
            self.lista_filmes.remove_filme(index)
            self.atualizar_listbox()
        else:
            messagebox.showwarning("Selection Error", "Nenhum filme selecionado")

    def atualizar_listbox(self):
        self.lb.delete(0, tk.END)
        for filme in self.lista_filmes.converte_para_lista():
            self.lb.insert(tk.END, filme)

    def limpar_campos(self):
        self.entry_titulo.delete(0, tk.END)
        self.entry_ano.delete(0, tk.END)
        self.entry_nota.delete(0, tk.END)


def main():
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()


if __name__ == '__main__':
    main()
