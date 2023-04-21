import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def show_scores(self):
        score_string = f"X: {self.scores['X']} | O: {self.scores['O']} | Tie: {self.scores['Tie']}\n\nScore History:\n"
        for x_score, o_score, tie_score in self.score_history:
            score_string += f"X: {x_score} | O: {o_score} | Tie: {tie_score}\n"
        messagebox.showinfo("Scores", score_string)
    def __init__(self):
        self.score_history = []
        self.scores = {"X": 0, "O": 0, "Tie": 0}
        self.window = tk.Tk()
        self.score_label = tk.Label(self.window, text="X: 0 | O: 0 | Tie: 0", font=("Arial", 20))
        self.score_label.grid(row=5, column=0, columnspan=3)       
        self.canvas = tk.Canvas(self.window, width=300, height=300, highlightthickness=0)
        self.window.title("Tic Tac Toe")
        self.player = "X"
        self.play_vs_ai = False
        self.ai_difficulty = "Easy"
        self.board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ]
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = tk.Button(self.window, text="", font=("Arial", 60), width=3, height=1, command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
        self.new_game_button = tk.Button(self.window, text="New Game", font=("Arial", 20), command=self.new_game)
        self.new_game_button.grid(row=3, column=0, columnspan=3)
        self.ai_button = tk.Button(self.window, text="Play vs AI", font=("Arial", 20), command=self.toggle_ai)
        self.ai_button.grid(row=4, column=0, columnspan=3)
        difficulty_label = tk.Label(self.window, text="AI Difficulty:", font=("Arial", 20))
        difficulty_label.grid(row=7, column=0)
        difficulty_options = ["Easy", "Medium", "Hard"]
        self.difficulty_var = tk.StringVar(self.window)
        self.difficulty_var.set(difficulty_options[0])
        difficulty_menu = tk.OptionMenu(self.window, self.difficulty_var, *difficulty_options)
        difficulty_menu.grid(row=7, column=1)
        self.show_scores_button = tk.Button(self.window, text="Show Scores", font=("Arial", 20), command=self.show_scores)
        self.show_scores_button.grid(row=6, column=0, columnspan=3)
        self.canvas.grid(row=0, column=0, rowspan=3, columnspan=3)
    
    def make_move(self, i, j):    
        if not self.board[i][j]:
            self.board[i][j] = self.player
            self.buttons[i][j]["text"] = self.player
            if self.player == "X":
                self.buttons[i][j]["fg"] = "red"
                self.player = "O"
            else:
                self.buttons[i][j]["fg"] = "blue"
                self.player = "X"
            winner, winning_coords = self.check_winner()
            if winner:
                x1,y1,x2,y2 = winning_coords
                x1,y1,x2,y2 = x1*100+50,y1*100+50,x2*100+50,y2*100+50
                self.canvas.create_line(x1,y1,x2,y2,width=5, fill="black")
                self.canvas.update()
                print(x1,y1,x2,y2)                
                messagebox.showinfo("Game Over", f"{winner} wins!")
                self.scores[winner] += 1
                self.new_game()
                self.update_score_label()
            elif all(all(row) for row in self.board):
                messagebox.showinfo("Game Over", "It's a tie!")
                self.scores['Tie'] += 1
                self.new_game()
                self.update_score_label()
            elif self.play_vs_ai and self.player == "O":
                self.make_ai_move()
    
    
    def update_score_label(self):
        if self.play_vs_ai:
            score_string = f"Player: {self.scores['X']} | AI: {self.scores['O']} | Tie: {self.scores['Tie']}"
        else:
            score_string = f"X: {self.scores['X']} | O: {self.scores['O']} | Tie: {self.scores['Tie']}"
        self.score_label["text"] = score_string

    from ia import make_ai_move

    def check_winner(self):
        
        for row in range(3):
            if all(self.board[row][col] == "X" for col in range(3)):
                return "X", (row,0,row,2)
            if all(self.board[row][col] == "O" for col in range(3)):
                return "O", (row,0,row,2)
        for col in range(3):
            if all(self.board[row][col] == "X" for row in range(3)):
                return "X", (0,col,2,col)
            if all(self.board[row][col] == "O" for row in range(3)):
                return "O", (0,col,2,col)
        if all(self.board[i][i] == "X" for i in range(3)):
            return "X", (0,0,2,2)
        if all(self.board[i][i] == "O" for i in range(3)):
            return "O", (0,0,2,2)
        if all(self.board[i][2-i] == "X" for i in range(3)):
            return "X", (0,2,2,0)
        if all(self.board[i][2-i] == "O" for i in range(3)):
            return "O", (0,2,2,0)                 
        return None, None

    def new_game(self):
        self.scores = {"X": 0, "O": 0, "Tie": 0}
        self.score_history.append((self.scores["X"], self.scores["O"], self.scores["Tie"]))
        for i in range(3):
            for j in range(3):
                self.board[i][j] = ""
                self.buttons[i][j]["text"] = ""
                self.buttons[i][j]["fg"] = "black"
        self.player = "X"
        self.canvas.delete("all")
        self.update_score_label()
        
    def toggle_ai(self):
        if not self.play_vs_ai:
            self.play_vs_ai = True
            self.ai_button["text"] = "Play vs Player"
        else:
            self.play_vs_ai = False
            self.ai_button["text"] = "Play vs AI"

if __name__ == "__main__":
    game = TicTacToe()
    game.window.mainloop()