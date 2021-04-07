################################################################################
#                                                                              #
#                    Coded by Roberto (Tank3) Cruz Lozano                      #
#                                                                              #
################################################################################

################################################################################
#                   MODULES

import tkinter as tk
import tkinter.font
from game_of_life_main_class import GameOfLife

################################################################################
#                   MAIN

if __name__ == '__main__':

    window=tk.Tk()
    window.title("Game of Life")
    window.geometry("1280x720")
    window.iconbitmap("./img/Glider.ico")
    window.config(background="#FFFFFF")
    window.resizable(width=False,height=False)

    fontTitles = tk.font.Font(family="Arial", size=25)
    fontText = tk.font.Font(family="Arial", size=10)

    frameLeft = tk.Frame(window,background="#22232D")
    frameLeft.pack_propagate(0)
    frameLeft.pack(fill='both',side='left',expand='True')

    txtBoard = tk.Label(frameLeft,foreground="#FFFFFF",background="#22232D",text="Game of Life",font=fontTitles)
    txtBoard.pack_propagate(0)
    txtBoard.pack()

    board = tk.Frame(frameLeft,background="#FFFFFF",width="500",height="500",bd=0)
    board.pack_propagate(0)
    board.pack(side='top',padx=0,pady=0)

    canvasBoard = tk.Canvas(board,background="#666B8A",bd=0)
    canvasBoard.pack_propagate(0)
    canvasBoard.pack(fill='both',side='left',expand='True')
    for i in range(0,500,20):
        canvasBoard.create_line(i,0,i,500,fill="#FFFFFF")
        canvasBoard.create_line(0,i,500,i,fill="#FFFFFF")

    frameLeftOne = tk.Frame(frameLeft,background="#22232D",width="500",height="100")
    frameLeftOne.pack_propagate(0)
    frameLeftOne.pack(side='top',padx=0,pady=20)

    buttonStart = tk.Button(frameLeftOne,text="Start",font=fontText,background="#419A61",foreground="#FFFFFF")
    buttonStart.pack_propagate(0)
    buttonStart.pack(fill='both',side='left',expand='True',padx=5,pady=10)

    buttonStop = tk.Button(frameLeftOne,text="Stop",font=fontText,background="#615391",foreground="#FFFFFF")
    buttonStop.pack_propagate(0)
    buttonStop.pack(fill='both',side='left',expand='True',padx=5,pady=10)

    buttonClean = tk.Button(frameLeftOne,text="Clean",font=fontText,background="#756FA1",foreground="#FFFFFF")
    buttonClean.pack_propagate(0)
    buttonClean.pack(fill='both',side='left',expand='True',padx=5,pady=10)

    buttonExit = tk.Button(frameLeftOne,text="Exit",font=fontText,background="#FE90CD",foreground="#000000")
    buttonExit.pack_propagate(0)
    buttonExit.pack(fill='both',side='left',expand='True',padx=5,pady=10)

    #frameRight = tk.Frame(window,background="#282A36")
    #frameRight.pack_propagate(0)
    #frameRight.pack(fill='both',side='right',expand='True')

    gol = GameOfLife(window,canvasBoard)
    
    ################################################################################
    #                   EVENTS

    canvasBoard.bind("<Button-1>",gol.clickMouseButton)
    canvasBoard.bind("<Button-3>",gol.clickMouseButton)
    buttonStart.config(command=gol.clickStartButton)
    buttonClean.config(command=gol.clickCleanButton)
    buttonExit.config(command=gol.clickExitButton)

    window.mainloop()
