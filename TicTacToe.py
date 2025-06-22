import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("TIC TAC TOE")
        
        self.current_player = "X"

        # _ - variable that will not be used

        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        # None - Buttons with None value
        
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        for i in range(3):
            for j in range(3):

                # Create a Tkinter Button widget

                # self.root - main window or frame
                # command=lambda i=i, j=j: self.make_move(i, j) - This specifies the function to be called when the button is clicked. It uses a lambda function to capture the current values of i and j and then calls the self.make_move() method with these indices.

                self.buttons[i][j] = tk.Button(self.root, text=' ', font=('Arial', 20), width=5, height=2,command=lambda i=i, j=j: self.make_move(i, j))

                # .grid() method is used to place buttons within parent widgets

                self.buttons[i][j].grid(row=i, column=j)
        
    def make_move(self, i, j):
        if self.board[i][j] == ' ':
            self.board[i][j] = self.current_player

            # .config() method is used to modify the configuration options of a widget

            self.buttons[i][j].config(text=self.current_player)
            
            if self.check_winner():
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Draw", "The game is a draw!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False
    
    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == ' ':
                    return False
        return True
    
    def reset_game(self):
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=' ')
    
    def run(self):
        self.root.mainloop()

# __name__ == "__main__" - Entry point of the script.
# Creates an instance of the TicTacToe class and starts the game if the script is run directly.

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
