################################################################################
#                                                                              #
#                    Coded by Roberto (Tank3) Cruz Lozano                      #
#                                                                              #
################################################################################

################################################################################
#                                CLASS

class GameOfLifeClass():
    def __init__(self, app):
        self.app = app
        self.gameMatrix = self.createDashboardMatrix()
        self.neigcount = 0
        self.status = False
    
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
        print("\n\n")

    def clickStartButton(self): # Starts the game
        self.status = True
        
    def clickStopButton(self): # Starts the game
        self.status = False

    def playGame(self):
        self.aliveDead()
        self.updateGameBoard()
        self.drawGameBoard()

    def randHex(self):
        return "#%02x%02x%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def events(self):
        self.app.canvasBoard.bind("<Button-1>", self.clickMouseButton)
        self.app.canvasBoard.bind("<Button-3>", self.clickMouseButton)
        self.app.buttons[0][3].config(command = self.clickStartButton)
        self.app.buttons[1][3].config(command = self.clickStopButton)
        self.app.buttons[2][3].config(command = self.clickCleanButton)
        self.app.buttons[3][3].config(command = self.app.root.destroy)

    def game(self):
        if self.status == True:
            self.playGame()
        self.app.root.after(125, self.game)
        
    def __del__(self):
        return 0
