import tkinter as tk
root = tk.Tk()
root.title("Welcome To Tic Tac Game")
root.geometry("500x500")
turn = 0
x = 0
y = 0
row = 0
col = 0
apn =0
draw = 0
btn = []
btn_text = []
Xgame = [ [0,0,0],[0,0,0],[0,0,0] ]
Ygame =  [[0,0,0],[0,0,0],[0,0,0]]
while apn < 9:
      btn.append(' ')
      btn_text.append('')
      btn_text[apn] = tk.StringVar()
      apn = apn + 1
def make3DarrayX(y):
    if y >= 0 and y <=2:
       Xgame[0][int(y/1)] = 1
    elif y>=3 and y <=5:
         Xgame[1][y-3] = 1
    elif y>=6 and y<=8:
        Xgame[2][y-6] = 1
def make3DarrayY(y):
    if y >= 0 and y <=2:
       Ygame[0][int(y/1)] = 1
    elif y>=3 and y <=5:
       Ygame[1][y-3] = 1
    elif y>=6 and y<=8:
        Ygame[2][y-6] = 1
def checkifXwon():
    global draw
    draw = draw + 1
    y = 0
    x = 0
    while y < 3:
      while x < 3:
         if Xgame[y][0] == 1 and Xgame[y][1] == 1 and Xgame[y][2] ==1:
             label = tk.Label(root, text="X won")
             label.grid(row=9,column=0)
         if Xgame[0][y] == 1 and Xgame[1][y] == 1 and Xgame[2][y] ==1:
             label = tk.Label(root, text="X won")
             label.grid(row=9,column=0)
         if Xgame[0][0] == 1 and Xgame[1][1] == 1 and Xgame[2][2] ==1:
             label = tk.Label(root, text="X won")
             label.grid(row=9,column=0)
         if Xgame[0][2] == 1 and Xgame[1][1] == 1 and Xgame[2][0] ==1:
             label = tk.Label(root, text="X won")
             label.grid(row=9,column=0)
         x = x+ 1
      if draw == 9:
          label = tk.Label(root, text="DRAW")
          label.grid(row=9,column=0)
          return 0
      x = 0
      y = y+1
def checkifYwon():
    global draw
    draw = draw + 1
    y = 0
    x = 0
    while y < 3:
        while x < 3:
            if Ygame[y][0] == 1 and Ygame[y][1] == 1 and Ygame[y][2] ==1:
                label = tk.Label(root, text="O WON")
                label.grid(row=9,column=0)
            if Ygame[0][y] == 1 and Ygame[1][y] == 1 and Ygame[2][y] ==1:
                label = tk.Label(root, text="O WON")
                label.grid(row=9,column=0)
            if Ygame[0][0] == 1 and Ygame[1][1] == 1 and Ygame[2][2] ==1:
                label = tk.Label(root, text="O WON")
                label.grid(row=9,column=0)
            if Ygame[0][2] == 1 and Ygame[1][1] == 1 and Ygame[2][0] ==1:
                label = tk.Label(root, text="O WON")
                label.grid(row=9,column=0)
            x = x+ 1
        if draw == 9:
            label = tk.Label(root, text="DRAW")
            label.grid(row=9,column=0)
        x = 0
        y = y+1
def update_btn_text(y):
    global turn
    global Xgame
    global Ygame
    turn = turn + 1
    if turn%2==1:
        btn_text[y].set("X")
        make3DarrayX(y)
        checkifXwon()
    if turn%2==0:
       btn_text[y].set("O")
       make3DarrayY(y)
       checkifYwon()
item=0
while y < 9:
     btn[y] = tk.Button(root,text=item, textvariable=btn_text[y], command = lambda s=item: update_btn_text(s),height = 9, width =18)
     btn_text[y].set('')
     item = item + 1
     y = y+1
while row < 3:
    while col < 3:
        btn[x].grid(row = row, column=col, sticky = 'nesw')
        col = col +1
        x = x+1
    col =0
    row = row + 1
label = tk.Label(root, text="")
label.grid(row=9,column=0)
root.mainloop()