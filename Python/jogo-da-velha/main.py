import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:

    def __init__(self):
        self.app = tk.Tk()
        self.app.title('Jogo da Velha')

        self.vez = 'X'
        
        self.botoes()
        self.tabuleiro = [[''] * 3 for _ in range(3)]

    def botoes(self):
        self.botao_matrix = [[None] * 3 for _ in range(3)]

        for row in range(3):
            for col in range(3):
                botao = tk.Button(self.app, command=lambda r=row, c=col: self.botao_clicado(r, c), text='', font=('Helvetica', 40), width=5, height=2)
                botao.grid(row=row, column=col, sticky='nsew')
                self.botao_matrix[row][col] = botao

        for i in range(3):
            self.app.columnconfigure(i, weight=1)

        for i in range(3):
            self.app.rowconfigure(i, weight=1)

    def botao_clicado(self, row, col):
        botao = self.botao_matrix[row][col]

        if botao['text'] == '':
            botao.config(text=self.vez)
            self.tabuleiro[row][col] = self.vez

            if self.verificar_vitoria():
                messagebox.showinfo('Vitória', f'O jogador {self.vez} venceu!')
                self.reiniciar_jogo()
            elif self.tabuleiro_cheio():
                messagebox.showinfo('Empate', 'O jogo empatou!')
                self.reiniciar_jogo()
            else:
                self.vez = 'O' if self.vez == 'X' else 'X'

    def verificar_vitoria(self):
        for row in range(3):
            if self.tabuleiro[row][0] == self.tabuleiro[row][1] == self.tabuleiro[row][2] != '':
                return True

        for col in range(3):
            if self.tabuleiro[0][col] == self.tabuleiro[1][col] == self.tabuleiro[2][col] != '':
                return True

        if self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] != '':
            return True

        if self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] != '':
            return True

        return False

    def tabuleiro_cheio(self):
        for row in range(3):
            for col in range(3):
                if self.tabuleiro[row][col] == '':
                    return False
        return True

    def reiniciar_jogo(self):
        for row in range(3):
            for col in range(3):
                self.botao_matrix[row][col].config(text='')
                self.tabuleiro[row][col] = ''
        self.vez = 'X'

    def run(self):
        self.app.mainloop()

if __name__ == '__main__':
    jogo = JogoDaVelha()
    jogo.run()
