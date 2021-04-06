import tkinter as tk
import tkinter.font
import random

def randHex():
    hex_number = "#%02x%02x%02x" % (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    return hex_number

def createDashboardMatrix(): #ID,X1,Y1,X2,Y2,Status
    matrix = []
    x,y,cont = 0,0,0
    for i in range(0,25):
        matrix.append([])
        for j in range(0,25):
            matrix[i].append([cont,x,y,x+20,y+20,0])
            x+=20
            cont+=1
        y+=20
        x=0
    return matrix

def clickMouseButton(event):
    x,y=event.x,event.y
    for i in gameMatrix:
        for j in i:
            if (x > j[1] and x < j[3]) and (y > j[2] and y < j[4]):
                if j[5] == 0:
                    canvasBoard.create_rectangle(j[1],j[2],j[3],j[4],fill=randHex(),outline="#FFFFFF")
                    canvasBoard.create_rectangle(j[1]+5,j[2]+5,j[3]-5,j[4]-5,fill="#000000",outline="#000000")
                    j[5] = 1
                else:
                    canvasBoard.create_rectangle(j[1],j[2],j[3],j[4],fill="#666B8A",outline="#FFFFFF")
                    canvasBoard.create_rectangle(j[1]+5,j[2]+5,j[3]-5,j[4]-5,fill="#666B8A",outline="#666B8A")
                    j[5] = 0

def clickStartButton():
    print("HOLO")

def clickCleanButton():
    for i in gameMatrix:
        for j in i:
            if j[5] == 1:
                canvasBoard.create_rectangle(j[1],j[2],j[3],j[4],fill="#666B8A",outline="#FFFFFF")
                canvasBoard.create_rectangle(j[1]+5,j[2]+5,j[3]-5,j[4]-5,fill="#666B8A",outline="#666B8A")
                j[5] = 0

def clickExitButton():
    window.destroy()

if __name__ == '__main__':
    gameMatrix = createDashboardMatrix()
        
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
    canvasBoard.bind("<Button-1>", clickMouseButton)
    canvasBoard.bind("<Button-3>", clickMouseButton)

    frameLeftOne = tk.Frame(frameLeft,background="#22232D",width="500",height="100")
    frameLeftOne.pack_propagate(0)
    frameLeftOne.pack(side='top',padx=0,pady=20)

    buttonStart = tk.Button(frameLeftOne,text="Start",font=fontText,background="#419A61",foreground="#FFFFFF")
    buttonStart.config(command=clickStartButton)
    buttonStart.pack_propagate(0)
    buttonStart.pack(fill='both',side='left',expand='True',padx=5,pady=10)

    buttonStop = tk.Button(frameLeftOne,text="Stop",font=fontText,background="#615391",foreground="#FFFFFF")
    buttonStop.pack_propagate(0)
    buttonStop.pack(fill='both',side='left',expand='True',padx=5,pady=10)

    buttonClean = tk.Button(frameLeftOne,text="Clean",font=fontText,background="#756FA1",foreground="#FFFFFF")
    buttonClean.config(command=clickCleanButton)
    buttonClean.pack_propagate(0)
    buttonClean.pack(fill='both',side='left',expand='True',padx=5,pady=10)

    buttonExit = tk.Button(frameLeftOne,text="Exit",font=fontText,background="#FE90CD",foreground="#000000")
    buttonExit.config(command=clickExitButton)
    buttonExit.pack_propagate(0)
    buttonExit.pack(fill='both',side='left',expand='True',padx=5,pady=10)

    #frameRight = tk.Frame(window,background="#282A36")
    #frameRight.pack_propagate(0)
    #frameRight.pack(fill='both',side='right',expand='True')

    window.mainloop()