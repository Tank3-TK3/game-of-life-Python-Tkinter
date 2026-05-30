################################################################################
#                                                                              #
#                    Coded by Roberto (Tank3) Cruz Lozano                      #
#                                                                              #
################################################################################

################################################################################
#                               MODULES

import tkinter as tk
from game_of_life_interface import GameOfLifeInterface
from game_of_life_class import GameOfLifeClass

################################################################################
#                                 MAIN

if __name__ == '__main__':
    root = tk.Tk()
    app = GameOfLifeInterface(root)
    logi = GameOfLifeClass(app)
    logi.events()
    root.after(125, logi.game)
    root.mainloop()
