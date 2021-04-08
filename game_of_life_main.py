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

def events():
    app.canvasBoard.bind("<Button-1>",logi.clickMouseButton)
    app.canvasBoard.bind("<Button-3>",logi.clickMouseButton)
    app.buttons[0][3].config(command = logi.clickStartButton)
    app.buttons[2][3].config(command = logi.clickCleanButton)
    app.buttons[3][3].config(command = root.destroy)

if __name__ == '__main__':
    root = tk.Tk()
    app = GameOfLifeInterface(root)
    logi = GameOfLifeClass(app)
    events()
    root.mainloop()