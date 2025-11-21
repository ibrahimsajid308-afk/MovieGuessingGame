# Person 1's File
import tkinter as tk

class GameWindow(tk.Tk):
    def __init__(self, game_logic):
        super().__init__()
        self.game_logic = game_logic
        self.title("Movie Guessing Game")
        self.geometry("600x400")
        label = tk.Label(self, text="Person 1 will build the GUI here")
        label.pack()

    def update_display(self):
        pass
    
