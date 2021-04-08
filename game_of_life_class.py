################################################################################
#                                                                              #
#                    Coded by Roberto (Tank3) Cruz Lozano                      #
#                                                                              #
################################################################################

################################################################################
#                               MODULES

import tkinter as tk

################################################################################
#                                CLASS

class GameOfLifeClass():
    app = None
    gameMatrix = None
    neigcount = None

    def __init__(self, app):
        self.app = app
        self.gameMatrix = self.createDashboardMatrix()
        self.neigcount = 0
    
    def createDashboardMatrix(self): # Generates and returns the game matrix
        matrix = []
        x, y, cont = 0, 0, 0
        for i in range(0, 25):
            matrix.append([])
            for j in range(0, 25):
                #ID, X1, Y1, X2, Y2, ASTATUS, PSTATUS, CANVE, CANVI - STATUS: 1 = alive, 0 = dead
                matrix[i].append([cont, x, y, x + 20, y + 20, 0, 0, None, None])
                x += 20
                cont += 1
            y += 20
            x = 0
        return matrix

    def clickMouseButton(self, event): # Color or erase the selected space inside the board
        x, y = event.x, event.y
        for i in self.gameMatrix:
            for j in i:
                if (x > j[1] and x < j[3]) and (y > j[2] and y < j[4]):
                    if j[5] == 0:
                        self.app.aliveCell(j)
                    else:
                        self.app.deadCell(j)

    def clickCleanButton(self): # Clears the game board
        for i in self.gameMatrix:
            for j in i:
                if j[5] == 1:
                    self.app.deadCell(j)

    def countingNeighbors(self, i, j):
        if self.gameMatrix[(i - 1) % 25][(j - 1) % 25][5] == 1:
            self.neigcount += 1
        if self.gameMatrix[i % 25][(j - 1) % 25][5] == 1:
            self.neigcount += 1
        if self.gameMatrix[(i + 1) % 25][(j - 1) % 25][5] == 1:
            self.neigcount += 1
        if self.gameMatrix[(i - 1) % 25][j % 25][5] == 1:
            self.neigcount += 1
        if self.gameMatrix[(i + 1) % 25][j % 25][5] == 1:
            self.neigcount += 1
        if self.gameMatrix[(i - 1) % 25][(j + 1) % 25][5] == 1:
            self.neigcount += 1
        if self.gameMatrix[i % 25][(j + 1) % 25][5] == 1:
            self.neigcount += 1
        if self.gameMatrix[(i + 1) % 25][(j + 1) % 25][5] == 1:
            self.neigcount += 1
        return self.neigcount

    def aliveDead(self):
        for i in range(0, 25):
            for j in range(0, 25):
                self.neigcount = self.countingNeighbors(i, j)
                if self.gameMatrix[i][j][5] == 1:
                    if self.neigcount == 2 or self.neigcount == 3:
                        self.gameMatrix[i][j][6] = 1
                    else:
                        self.gameMatrix[i][j][6] = 0
                else:
                    if self.neigcount == 3:
                        self.gameMatrix[i][j][6] = 1
                    else:
                        self.gameMatrix[i][j][6] = 0
                self.neigcount = 0

    def updateGameBoard(self):
        for i in self.gameMatrix:
            for j in i:
                j[5] = j[6]
                j[6] = 0

    def drawGameBoard(self):
        for i in self.gameMatrix:
            for j in i:
                if j[5] == 1:
                    self.app.aliveCell(j)
                else:
                    self.app.deadCell(j)

    def printGameBoard(self):
        for i in self.gameMatrix:
            for j in i:
                print("[",j[5],j[6],"]",end="")
            print()
        print()
        print()

    def clickStartButton(self): # Starts the game
        self.aliveDead()
        self.updateGameBoard()
        self.drawGameBoard()
        

    def __del__(self):
        return 0
