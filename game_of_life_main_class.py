################################################################################
#                                                                              #
#                    Coded by Roberto (Tank3) Cruz Lozano                      #
#                                                                              #
################################################################################

################################################################################
#                   MODULES

import tkinter as tk
import tkinter.font
import time

################################################################################
#                   CLASS

class GameOfLife():
    gameMatrix = []
    neigcount = 0
    window = None
    canvasBoard = None

    def __init__(self,window,canvasBoard):
        self.gameMatrix = self.createDashboardMatrix()
        self.window = window
        self.canvasBoard = canvasBoard

    def createDashboardMatrix(self): # Generates and returns the game matrix with the data ID,X1,Y1,X2,Y2,Status
        matrix = []
        x,y,cont = 0,0,0
        for i in range(0,25):
            matrix.append([])
            for j in range(0,25):
                matrix[i].append([cont,x,y,x+20,y+20,0,0])
                x+=20
                cont+=1
            y+=20
            x=0
        return matrix

    def livingCell(self,j):
        self.canvasBoard.create_rectangle(j[1],j[2],j[3],j[4],fill="#FFFFFF",outline="#FFFFFF")
        self.canvasBoard.create_rectangle(j[1]+5,j[2]+5,j[3]-5,j[4]-5,fill="#000000",outline="#000000")

    def deadCell(self,j):
        self.canvasBoard.create_rectangle(j[1],j[2],j[3],j[4],fill="#666B8A",outline="#FFFFFF")
        self.canvasBoard.create_rectangle(j[1]+5,j[2]+5,j[3]-5,j[4]-5,fill="#666B8A",outline="#666B8A")

    def clickMouseButton(self,event): # Color or erase the selected space inside the board
        x,y=event.x,event.y
        for i in self.gameMatrix:
            for j in i:
                if (x > j[1] and x < j[3]) and (y > j[2] and y < j[4]):
                    if j[5] == 0:
                        self.livingCell(j)
                        j[5] = 1
                    else:
                        self.deadCell(j)
                        j[5] = 0

    def countingNeighbors(self,i,j):
        if self.gameMatrix[(i-1)%25][(j-1)%25][5] == 1:
            self.neigcount+=1
        if self.gameMatrix[i%25][(j-1)%25][5] == 1:
            self.neigcount+=1
        if self.gameMatrix[(i+1)%25][(j-1)%25][5] == 1:
            self.neigcount+=1
        if self.gameMatrix[(i-1)%25][j%25][5] == 1:
            self.neigcount+=1
        if self.gameMatrix[(i+1)%25][j%25][5] == 1:
            self.neigcount+=1
        if self.gameMatrix[(i-1)%25][(j+1)%25][5] == 1:
            self.neigcount+=1
        if self.gameMatrix[i%25][(j+1)%25][5] == 1:
            self.neigcount+=1
        if self.gameMatrix[(i+1)%25][(j+1)%25][5] == 1:
            self.neigcount+=1

    def drawGameBoard(self):
        for i in self.gameMatrix:
            for j in i:
                if j[5] == 1:
                    self.livingCell(j)
                else:
                    self.deadCell(j)

    def clickStartButton(self): # Starts the game
        for i in range(0,25):
            for j in range(0,25):
                self.countingNeighbors(i,j)
                if self.gameMatrix[i][j][5]==1:
                    if self.neigcount==2 or self.neigcount==3:
                        self.gameMatrix[i][j][6]=1
                    else:
                        self.gameMatrix[i][j][6]=0
                else:
                    if self.neigcount==3:
                        self.gameMatrix[i][j][6]=1
                    else:
                        self.gameMatrix[i][j][6]=0
                self.neigcount=0
        for i in self.gameMatrix:
            for j in i:
                j[5]=j[6]
                j[6]=0
        self.drawGameBoard()

    def clickCleanButton(self): # Clears the game board
        for i in self.gameMatrix:
            for j in i:
                if j[5] == 1:
                    self.deadCell(j)
                    j[5] = 0

    def clickExitButton(self): # Closes the game
        self.window.destroy()
    
    def __del__(self):
        pass