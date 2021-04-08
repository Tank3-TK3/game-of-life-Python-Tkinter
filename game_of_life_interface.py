################################################################################
#                                                                              #
#                    Coded by Roberto (Tank3) Cruz Lozano                      #
#                                                                              #
################################################################################

################################################################################
#                               MODULES

import tkinter as tk
from tkinter import font

################################################################################
#                                CLASS

class GameOfLifeInterface(tk.Frame):
    root = None
    frameOne = None
    txtBoard = None
    fontTitles = None
    fontText = None
    board = None
    canvasBoard = None
    frameButtons = None
    buttons = None
    frameInformation = None
    txtInformation = None

    def __init__(self, root = None):
        tk.Frame.__init__(self, root)
        self.root = self.drawRoot(root)
        self.fontTitles = tk.font.Font(family = "Arial", size = 25)
        self.fontText = tk.font.Font(family = "Arial", size = 15)
        self.frameOne = self.drawFrameOne()
        self.txtBoard = self.drawTextBoard()
        self.board = self.drawBoard()
        self.canvasBoard = self.drawCanvasBoard()
        self.frameButtons = self.drawFrameButtons()
        self.buttons = self.drawButtons()
        self.frameInformation = self.drawFrameInformation()
        self.txtInformation = self.drawTextInformation()

    def drawRoot(self,root):
        root.title("Game of Life (v1.0)")
        root.geometry("600x700+50+50")
        root.iconbitmap("./img/Glider.ico")
        root.config(background = "#FFFFFF")
        root.resizable(width = False, height = False)
        return root

    def drawFrameOne(self):
        frameOne = tk.Frame(self.root, background = "#22232D")
        frameOne.pack_propagate(0)
        frameOne.pack(fill = 'both', side = 'left', expand = 'True')
        return frameOne

    def drawTextBoard(self):
        txtBoard = tk.Label(self.frameOne, foreground = "#FFFFFF", background = "#22232D")
        txtBoard.config(text = "Game of Life", font = self.fontTitles)
        txtBoard.pack_propagate(0)
        txtBoard.pack()
        return txtBoard

    def drawBoard(self):
        board = tk.Frame(self.frameOne,background="#FFFFFF",width="500",height="500",bd=0)
        board.pack_propagate(0)
        board.pack(side='top',padx=0,pady=0)
        return board

    def drawCanvasBoard(self):
        canvasBoard = tk.Canvas(self.board, background = "#666B8A")
        canvasBoard.config(bd = 0, highlightthickness = 1, relief = 'ridge')
        canvasBoard.pack_propagate(0)
        canvasBoard.pack(fill = 'both', side = 'top', expand = 'True')
        for i in range(20, 500, 20):
            canvasBoard.create_line(i, 0, i, 500, fill = "#FFFFFF")
            canvasBoard.create_line(0, i, 500, i, fill = "#FFFFFF")
        return canvasBoard

    def drawFrameButtons(self):
        frameButtons = tk.Frame(self.frameOne, background = "#22232D")
        frameButtons.config(width = "500", height = "100")
        frameButtons.pack_propagate(0)
        frameButtons.pack(side='top',padx=0,pady=10)
        return frameButtons
    
    def drawButtons(self):
        buttons = [["Start", "#6CD987", "#121212"], ["Stop", "#D977B7", "#121212"],
                   ["Clean", "#837ACC", "#121212"], ["Exit", "#D3A16B", "#121212"]]
        for i in buttons:
            i.append(tk.Button(self.frameButtons, text = i[0], font = self.fontText))
            i[3].config(background = i[1], foreground = i[2])
            i[3].pack_propagate(0)
            i[3].pack(fill = 'both', side = 'left', expand = 'True', padx = 5, pady = 20)
        return buttons

    def drawFrameInformation(self):
        frameInformation = tk.Frame(self.frameOne, background = "#22232D")
        frameInformation.config(height = "25")
        frameInformation.pack_propagate(0)
        frameInformation.pack(fill = 'x', side = 'bottom', padx = 0, pady = 0)
        return frameInformation

    def drawTextInformation(self):
        txtInformation = [["v1.0", "right"], ["Coded by Tank3", "left"]]
        for i in txtInformation:
            i.append(tk.Label(self.frameInformation, foreground = "#FFFFFF", background = "#22232D"))
            i[2].config(text = i[0], font = self.fontText)
            i[2].pack_propagate(0)
            i[2].pack(side = i[1])
        return txtInformation

    def aliveCell(self,j):
        if j[7] == None or j[8] == None:
            j[7] = self.canvasBoard.create_rectangle(j[1], j[2], j[3], j[4])
            j[8] = self.canvasBoard.create_rectangle(j[1] + 5, j[2] + 5, j[3] - 5, j[4] - 5)
            self.canvasBoard.itemconfig(j[7], fill = "#FFFFFF", outline = "#FFFFFF")
            self.canvasBoard.itemconfig(j[8], fill = "#000000", outline = "#000000")
        else:
            self.canvasBoard.itemconfig(j[7], fill = "#FFFFFF", outline = "#FFFFFF")
            self.canvasBoard.itemconfig(j[8], fill = "#000000", outline = "#000000")
        j[5] = 1

    def deadCell(self,j):
        self.canvasBoard.itemconfig(j[7], fill = "#666B8A", outline = "#FFFFFF")
        self.canvasBoard.itemconfig(j[8], fill = "#666B8A", outline = "#666B8A")
        j[5] = 0

    def __del__(self):
        return 0
