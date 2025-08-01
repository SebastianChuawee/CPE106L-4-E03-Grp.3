import tkinter as tk
import tkinter.messagebox as mb
from oxo_logic import Game

top = tk.Tk()
game = Game()

def buildMenu(parent):
    menus = (
        ("File", (("New", evNew),
                  ("Resume", evResume),
                  ("Save", evSave),
                  ("Exit", evExit))),
        ("Help", (("Help", evHelp),
                  ("About", evAbout)))
        )
        
    menubar = tk.Menu(parent)
    for menu in menus:
        m = tk.Menu(parent)
        for item in menu[1]:
            m.add_command(label=item[0], command=item[1])
        menubar.add_cascade(label=menu[0], menu=m)

    return menubar

def evNew():
    global game
    status['text'] = "Playing game"
    game = Game()
    game2cells()

def evResume():     
    global game
    status['text'] = "Playing game"
    game.restore_game()
    game2cells()

def evSave():
    game.save_game()
      
def evExit():
    if status['text'] == "Playing game":
        if mb.askyesno("Quitting","Do you want to save the game before quitting?"):
            evSave()
    top.quit()
      
def evHelp():
    mb.showinfo("Help",'''
    File->New:  starts a new game of tic-tac-toe
    File->Resume: restores the last saved game and commences play
    File->Save: Saves current game.
    File->Exit: quits, prompts to save active game
    Help->Help: shows this page
    Help->About: Shows information about the program and author''')

def evAbout():
    mb.showinfo("About","Tic-tac-toe game GUI demo by Alan Gauld")

def evClick(row,col): 
    global game
    if status['text'] == "Game over":
        mb.showerror("Game over", "Game over!")
        return
        
    index = (3*row) + col
    if game.board[index] == " ":
        result = game.user_move(index)
        game2cells()
        
        if not result:
            result = game.computer_move()
            game2cells()
        if result == "D":
            mb.showinfo("Result", "It's a Draw!")
            status['text'] = "Game over"
        elif result in ["X", "O"]:
            mb.showinfo("Result",  f"The winner is: {result}")
            status['text'] = "Game over"
        
def game2cells():
    table = board.pack_slaves()[0]
    for row in range(3):
        for col in range(3):
            table.grid_slaves(row=row,column=col)[0]['text'] = game.board[3*row+col]

def buildBoard(parent):
    outer = tk.Frame(parent, border=2, relief="sunken")
    inner = tk.Frame(outer)
    inner.pack()
    
    for row in range(3):
        for col in range(3):
            cell = tk.Button(inner, text=" ",  width="5", height="2", 
                                    command=lambda r=row, c=col : evClick(r,c) )
            cell.grid(row=row, column=col)
    return outer

mbar = buildMenu(top)
top["menu"] = mbar

board = buildBoard(top)
board.pack()
status = tk.Label(top, text="Playing game", border=0, background="lightgrey", foreground="red")
status.pack(anchor="s", fill="x", expand=True)

tk.mainloop()