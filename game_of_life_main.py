import tkinter as tk
from game_of_life_interface import GameOfLifeInterface
from game_of_life_class import GameOfLifeClass

if __name__ == "__main__":
    root = tk.Tk()
    ui   = GameOfLifeInterface(root)
    game = GameOfLifeClass(ui)
    game.events()
    root.after(100, game.game)
    root.mainloop()
