import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-Нолики")

        self.player = "X"  # Начальный игрок
        self.buttons = [[None for _ in range(3)] for _ in range(3)]  # Сетка кнопок 3x3

        self.create_buttons()
        self.configure_grid()

    def create_buttons(self):
        # Создание кнопок и размещение их на сетке
        for i in range(3):
            for j in range(3):
                button = tk.Button(self.root, text="", font=('normal', 40),
                                   command=lambda i=i, j=j: self.on_button_click(i, j))
                button.grid(row=i, column=j, sticky="nsew")
                self.buttons[i][j] = button

    def configure_grid(self):
        # Настройка строк и столбцов сетки для растяжения при изменении размера окна
        for i in range(3):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, i, j):
        # Обработка нажатия на кнопку
        if self.buttons[i][j]['text'] == "" and not self.check_winner():
            self.buttons[i][j]['text'] = self.player
            if self.check_winner():
                messagebox.showinfo("Победа!", f"Игрок {self.player} победил!")
                self.reset_board()
            elif self.check_draw():
                messagebox.showinfo("Ничья", "Ничья!")
                self.reset_board()
            else:
                # Смена игрока
                self.player = "O" if self.player == "X" else "X"

    def check_winner(self):
        # Проверка победителя с использованием рекурсии
        for i in range(3):
            if self.check_winner_recursive(i, 0, 0, 1) or self.check_winner_recursive(0, i, 1, 0):
                return True
        if self.check_winner_recursive(0, 0, 1, 1) or self.check_winner_recursive(0, 2, 1, -1):
            return True
        return False

    def check_winner_recursive(self, row, col, row_delta, col_delta, count=0):
        # Рекурсивная проверка победителя
        if row < 0 or row >= 3 or col < 0 or col >= 3:
            return False
        if self.buttons[row][col]['text'] == self.player:
            count += 1
            if count == 3:
                return True
            return self.check_winner_recursive(row + row_delta, col + col_delta, row_delta, col_delta, count)
        return False

    def check_draw(self):
        # Проверка, есть ли ничья
        for row in self.buttons:
            for button in row:
                if button['text'] == "":
                    return False
        return True

    def reset_board(self):
        # Сброс игрового поля для новой игры
        for row in self.buttons:
            for button in row:
                button['text'] = ""
        self.player = "X"  # Возврат начального игрока

if __name__ == "__main__":
    root = tk.Tk()  # Создание основного окна приложения
    game = TicTacToe(root)  # Создание экземпляра игры
    root.mainloop()  # Запуск основного цикла приложения
